"""Tests for the ParametersPage calculation screen."""

import csv
from pathlib import Path

import pytest
from conftest import element_button, select_elements, table_rows, tree_rows
from PyQt6 import QtCore, QtWidgets
from pytestqt.wait_signal import SignalBlocker

from HEACalculator.app import ParametersPage
from HEACalculator.core.hea import HEACalculator

EQUIMOLAR_ELEMENTS = ("Fe", "Co", "Cr", "Ni")
EQUIMOLAR_FORMULA = "Co25Cr25Fe25Ni25"

TREE_HEADERS = [
    "Formula",
    "Density",
    "δ",
    "δ (CN12)",
    "Δχ (Allen)",
    "Δχ (Pauling)",
    "Omega",
    "Gamma",
    "Lambda",
    "Phi",
    "VEC",
    "e/a",
    "Mixing Enthalpy",
    "Mixing Entropy",
    "Formation Enthalpy",
    "Min. Formation Enthalpy",
    "Melting Temperature",
    "Crystal Structure",
    "Model 1",
    "Model 2",
    "Model 3",
    "Model 4",
    "Model 5",
    "Model 6",
    "Model 7",
    "Model 8",
]

ERROR_CLASSIFICATION_CASES = [
    (
        KeyError("The requested pair does not exist in the formation enthalpy database."),
        "Calculation failed because formation enthalpy data is missing for one or more selected element pairs.",
    ),
    (
        KeyError("The requested pair does not exist in the mixing enthalpy database."),
        "Calculation failed because mixing enthalpy data is missing for one or more selected element pairs.",
    ),
    (
        KeyError("The requested element does not exist in the elements database."),
        "Calculation failed because one or more selected elements are not available in the database.",
    ),
    (
        ValueError("Some extra letters were detected in the formula."),
        "Calculation failed because the selected composition could not be parsed as a valid formula.",
    ),
    (TypeError("unsupported operand"), "Calculation failed."),
]

FORMULA_FORMAT_CASES = [
    ("Fe25Co25Cr25Ni25", "Fe<sub>25</sub>Co<sub>25</sub>Cr<sub>25</sub>Ni<sub>25</sub>"),
    ("FeCoCrNi", "FeCoCrNi"),
    ("Al0.5CoCrFeNi", "Al<sub>0.5</sub>CoCrFeNi"),
    ("Fe<25", "Fe&lt;<sub>25</sub>"),
]


def _calculate(qtbot, page: ParametersPage) -> None:
    """Press the Calculate button.

    Args:
        qtbot: The pytest-qt bot used to deliver the click.
        page: The parameters page under test.
    """
    qtbot.mouseClick(page.parametersPage.CalculatePushButton, QtCore.Qt.MouseButton.LeftButton)


def _set_amount(page: ParametersPage, row: int, value: str) -> None:
    """Type a new percentage into the composition table, as a user edit would.

    Args:
        page: The parameters page under test.
        row: Table row to edit.
        value: New amount text.
    """
    item = page.parametersPage.tableWidget.item(row, 1)
    assert item is not None
    item.setText(value)


def _last_notification(blocker: SignalBlocker) -> tuple[str, str]:
    """Return the (message, severity) pair captured by a waitSignal blocker.

    Args:
        blocker: A pytest-qt SignalBlocker that has already fired.

    Returns:
        The message and severity emitted with notificationRequested.
    """
    assert blocker.args is not None
    message, severity = blocker.args
    return message, severity


class TestElementSelection:
    """Tests for the periodic-table button wiring and percentage redistribution."""

    def test_selecting_one_element_fills_the_table(self, qtbot, parameters_page):
        """A single element takes the whole composition."""
        select_elements(qtbot, parameters_page, "Fe")

        assert parameters_page.selectedElements == {"Fe": 100.0}
        assert table_rows(parameters_page.parametersPage.tableWidget) == [["Fe", "100.00"]]

    def test_selecting_two_elements_splits_them_evenly(self, qtbot, parameters_page):
        """Adding a second element redistributes both to 50%."""
        select_elements(qtbot, parameters_page, "Fe", "Co")

        assert parameters_page.selectedElements == {"Fe": 50.0, "Co": 50.0}
        assert table_rows(parameters_page.parametersPage.tableWidget) == [["Fe", "50.00"], ["Co", "50.00"]]

    def test_selecting_four_elements_gives_equimolar_quarters(self, qtbot, parameters_page):
        """A four-element alloy defaults to 25% each."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)

        assert parameters_page.selectedElements == dict.fromkeys(EQUIMOLAR_ELEMENTS, 25.0)
        assert [row[1] for row in table_rows(parameters_page.parametersPage.tableWidget)] == ["25.00"] * 4

    def test_element_cell_is_not_editable(self, qtbot, parameters_page):
        """Only the percentage column accepts edits."""
        select_elements(qtbot, parameters_page, "Fe")
        item = parameters_page.parametersPage.tableWidget.item(0, 0)

        assert item is not None
        assert item.flags() == QtCore.Qt.ItemFlag.ItemIsEnabled

    def test_element_cell_is_centered(self, qtbot, parameters_page):
        """Symbols are centered in their cell."""
        select_elements(qtbot, parameters_page, "Fe")
        item = parameters_page.parametersPage.tableWidget.item(0, 0)

        assert item is not None
        expected = QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        assert item.textAlignment() == expected.value

    def test_deselecting_removes_the_row_and_redistributes(self, qtbot, parameters_page):
        """Unchecking an element hands its share to the survivors."""
        select_elements(qtbot, parameters_page, "Fe", "Co")
        select_elements(qtbot, parameters_page, "Co")

        assert parameters_page.selectedElements == {"Fe": 100.0}
        assert table_rows(parameters_page.parametersPage.tableWidget) == [["Fe", "100.00"]]

    def test_deselecting_the_last_element_empties_the_table(self, qtbot, parameters_page):
        """Removing every element leaves no rows and no selection."""
        select_elements(qtbot, parameters_page, "Fe")
        select_elements(qtbot, parameters_page, "Fe")

        assert parameters_page.selectedElements == {}
        assert parameters_page.parametersPage.tableWidget.rowCount() == 0

    def test_neodymium_button_is_reachable_despite_its_object_name(self, qtbot, parameters_page):
        """The Nd button is misnamed 'ebtnAnd' but must still select neodymium."""
        assert element_button(parameters_page, "Nd").objectName() == "ebtnAnd"

        select_elements(qtbot, parameters_page, "Nd")

        assert parameters_page.selectedElements == {"Nd": 100.0}

    def test_redistribution_keeps_full_precision_for_existing_rows(self, qtbot, parameters_page):
        """blockSignals stops the 2-decimal cell text from overwriting exact percentages.

        Without the guard in handleElementClicked, writing "33.33" into each existing
        row re-enters handleAmountChanged and truncates the stored value.
        """
        select_elements(qtbot, parameters_page, "Fe", "Co", "Cr")

        assert parameters_page.selectedElements["Fe"] == pytest.approx(100 / 3)
        assert parameters_page.selectedElements["Co"] == pytest.approx(100 / 3)

    def test_newly_added_element_stores_the_rounded_display_value(self, qtbot, parameters_page):
        """Known quirk: the new row's cell is written before blockSignals is engaged.

        handleElementClicked calls setItem() for the new row outside the guarded
        block, so handleAmountChanged runs for it and stores the 2-decimal text.
        """
        select_elements(qtbot, parameters_page, "Fe", "Co", "Cr")

        assert parameters_page.selectedElements["Cr"] == pytest.approx(33.33)

    def test_deselection_keeps_full_precision_for_survivors(self, qtbot, parameters_page):
        """Removing an element rewrites the remaining cells without truncating them."""
        select_elements(qtbot, parameters_page, "Fe", "Co", "Cr", "Ni")

        select_elements(qtbot, parameters_page, "Ni")

        assert parameters_page.selectedElements["Fe"] == pytest.approx(100 / 3)
        assert parameters_page.selectedElements["Cr"] == pytest.approx(100 / 3)

    def test_redistribution_emits_no_notifications(self, qtbot, parameters_page):
        """Programmatic cell writes never surface as user-facing messages."""
        select_elements(qtbot, parameters_page, "Fe", "Co")

        with qtbot.assertNotEmitted(parameters_page.notificationRequested):
            select_elements(qtbot, parameters_page, "Cr")


class TestTotalLabel:
    """Tests for the running composition total indicator."""

    def test_label_is_blank_with_no_selection(self, parameters_page):
        """Nothing is shown before any element is picked."""
        assert parameters_page.totalLabel.text() == ""

    def test_label_shows_the_running_total(self, qtbot, parameters_page):
        """An equimolar selection totals 100%."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)

        assert parameters_page.totalLabel.text() == "Total: 100.00%"

    def test_total_at_one_hundred_is_green(self, qtbot, parameters_page):
        """A valid total is styled with the success color."""
        select_elements(qtbot, parameters_page, "Fe", "Co")

        assert "#7FB685" in parameters_page.totalLabel.styleSheet()

    def test_total_off_one_hundred_is_red(self, qtbot, parameters_page):
        """An invalid total is styled with the warning color."""
        select_elements(qtbot, parameters_page, "Fe", "Co")
        _set_amount(parameters_page, 0, "60")

        assert parameters_page.totalLabel.text() == "Total: 110.00%"
        assert "#C94040" in parameters_page.totalLabel.styleSheet()


class TestActionButtonState:
    """Tests for enabling and disabling the Clear/Calculate/Save buttons."""

    def test_all_actions_disabled_before_any_selection(self, parameters_page):
        """A fresh page offers nothing to clear, calculate or save."""
        assert not parameters_page.parametersPage.ClearAllPushButton.isEnabled()
        assert not parameters_page.parametersPage.CalculatePushButton.isEnabled()
        assert not parameters_page.parametersPage.SavePushButton.isEnabled()

    def test_selection_enables_clear_and_calculate(self, qtbot, parameters_page):
        """Picking an element unlocks the clear and calculate actions."""
        select_elements(qtbot, parameters_page, "Fe")

        assert parameters_page.parametersPage.ClearAllPushButton.isEnabled()
        assert parameters_page.parametersPage.CalculatePushButton.isEnabled()

    def test_selection_alone_does_not_enable_save(self, qtbot, parameters_page):
        """Save stays locked until there is a result row."""
        select_elements(qtbot, parameters_page, "Fe")

        assert not parameters_page.parametersPage.SavePushButton.isEnabled()

    def test_a_result_enables_save(self, qtbot, parameters_page):
        """A completed calculation unlocks CSV export."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        assert parameters_page.parametersPage.SavePushButton.isEnabled()


class TestAmountEditing:
    """Tests for manual percentage edits in the composition table."""

    def test_editing_an_amount_updates_the_model(self, qtbot, parameters_page):
        """A user edit is synced back into selectedElements."""
        select_elements(qtbot, parameters_page, "Fe", "Co")

        _set_amount(parameters_page, 0, "60")

        assert parameters_page.selectedElements == {"Fe": 60.0, "Co": 50.0}

    def test_editing_the_symbol_column_is_ignored(self, qtbot, parameters_page):
        """Only column 1 feeds back into the model."""
        select_elements(qtbot, parameters_page, "Fe")

        parameters_page.parametersPage.tableWidget.item(0, 0).setText("Zz")

        assert parameters_page.selectedElements == {"Fe": 100.0}

    def test_zero_is_rejected_and_reverted(self, qtbot, parameters_page):
        """A 0% entry snaps back to the previous value."""
        select_elements(qtbot, parameters_page, "Fe", "Co")

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            _set_amount(parameters_page, 0, "0")

        assert _last_notification(blocker) == ("Atomic percentage cannot be 0%.", "warning")
        assert parameters_page.parametersPage.tableWidget.item(0, 1).text() == "50.00"
        assert parameters_page.selectedElements == {"Fe": 50.0, "Co": 50.0}

    def test_unknown_element_row_is_ignored(self, qtbot, parameters_page):
        """A row whose symbol is not tracked does not corrupt the model."""
        select_elements(qtbot, parameters_page, "Fe")
        parameters_page.parametersPage.tableWidget.item(0, 0).setText("Zz")

        _set_amount(parameters_page, 0, "42")

        assert parameters_page.selectedElements == {"Fe": 100.0}


class TestCalculate:
    """Tests for running a calculation and populating the results tree."""

    def test_total_below_one_hundred_is_refused(self, qtbot, parameters_page):
        """Calculating an under-specified alloy warns instead of running."""
        select_elements(qtbot, parameters_page, "Fe", "Co")
        _set_amount(parameters_page, 0, "10")

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            _calculate(qtbot, parameters_page)

        message, severity = _last_notification(blocker)
        assert severity == "warning"
        assert "60.00%" in message
        assert parameters_page.parametersPage.resultsTreeWidget.topLevelItemCount() == 0

    def test_total_above_one_hundred_is_refused(self, qtbot, parameters_page):
        """Calculating an over-specified alloy warns instead of running."""
        select_elements(qtbot, parameters_page, "Fe", "Co")
        _set_amount(parameters_page, 0, "80")

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            _calculate(qtbot, parameters_page)

        message, severity = _last_notification(blocker)
        assert severity == "warning"
        assert "130.00%" in message

    def test_valid_composition_adds_one_result_row(self, qtbot, parameters_page):
        """A complete composition produces exactly one tree row."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)

        _calculate(qtbot, parameters_page)

        assert parameters_page.parametersPage.resultsTreeWidget.topLevelItemCount() == 1

    def test_result_row_matches_the_core_calculation(self, qtbot, parameters_page):
        """The displayed row is exactly HEACalculator.get_list() for the sorted formula."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)

        _calculate(qtbot, parameters_page)

        expected = [str(value) for value in HEACalculator(EQUIMOLAR_FORMULA).get_list()]
        assert tree_rows(parameters_page.parametersPage.resultsTreeWidget) == [expected]

    def test_formula_uses_alphabetically_sorted_symbols(self, qtbot, parameters_page):
        """Selection order does not change the generated formula."""
        select_elements(qtbot, parameters_page, "Ni", "Fe", "Cr", "Co")

        _calculate(qtbot, parameters_page)

        assert parameters_page.parametersPage.resultsTreeWidget.topLevelItem(0).text(0) == EQUIMOLAR_FORMULA

    def test_success_notification_subscripts_the_formula(self, qtbot, parameters_page):
        """The success message renders stoichiometry as subscripts."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            _calculate(qtbot, parameters_page)

        message, severity = _last_notification(blocker)
        assert severity == "info"
        assert message == "Co<sub>25</sub>Cr<sub>25</sub>Fe<sub>25</sub>Ni<sub>25</sub> calculation completed."

    def test_duplicate_calculation_is_refused(self, qtbot, parameters_page):
        """Recalculating the same formula warns and adds no second row."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            _calculate(qtbot, parameters_page)

        message, severity = _last_notification(blocker)
        assert severity == "warning"
        assert "has already been calculated." in message
        assert parameters_page.parametersPage.resultsTreeWidget.topLevelItemCount() == 1

    @pytest.mark.parametrize(
        "error,expected_prefix",
        ERROR_CLASSIFICATION_CASES,
        ids=["formation_enthalpy", "mixing_enthalpy", "elements_database", "extra_letters", "unclassified"],
    )
    def test_calculation_errors_are_classified(self, qtbot, parameters_page, monkeypatch, error, expected_prefix):
        """Known failure modes get a tailored explanation; others fall back."""

        def _raise(_formula: str) -> None:
            raise error

        monkeypatch.setattr("HEACalculator.app.HEACalculator", _raise)
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            _calculate(qtbot, parameters_page)

        message, severity = _last_notification(blocker)
        assert severity == "error"
        assert message.startswith(expected_prefix)

    def test_failed_calculation_leaves_save_disabled(self, qtbot, parameters_page, monkeypatch):
        """A failure must not pretend there is something to export."""

        def _raise(_formula: str) -> None:
            raise ValueError("boom")

        monkeypatch.setattr("HEACalculator.app.HEACalculator", _raise)
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)

        _calculate(qtbot, parameters_page)

        assert not parameters_page.parametersPage.SavePushButton.isEnabled()
        assert parameters_page.parametersPage.resultsTreeWidget.topLevelItemCount() == 0


class TestErrorMessageHelpers:
    """Tests for the static error-message formatting helpers."""

    def test_string_first_argument_is_used_verbatim(self):
        """An exception carrying a message string exposes it directly."""
        assert ParametersPage._clean_error_message(ValueError("boom")) == "boom"

    def test_non_string_first_argument_falls_back_to_str(self):
        """A non-string payload is rendered with str()."""
        assert ParametersPage._clean_error_message(ValueError(42)) == "42"

    def test_argument_free_exception_falls_back_to_str(self):
        """An exception with no args still yields a printable detail."""
        assert ParametersPage._clean_error_message(ValueError()) == ""

    def test_save_error_is_prefixed(self, parameters_page):
        """Save failures get a consistent user-facing prefix."""
        message = parameters_page._format_save_error(OSError("Permission denied"))

        assert message == "Could not save the results file. Permission denied"

    @pytest.mark.parametrize("formula,expected", FORMULA_FORMAT_CASES, ids=[case[0] for case in FORMULA_FORMAT_CASES])
    def test_formula_is_escaped_then_subscripted(self, formula, expected):
        """Digits become subscripts and markup characters are escaped first."""
        assert ParametersPage._format_formula_for_notification(formula) == expected


class TestClearAll:
    """Tests for the Clear All action and its confirmation dialog."""

    def test_clearing_without_results_skips_the_dialog(self, qtbot, parameters_page, confirm_clear):
        """There is nothing to lose, so no confirmation is asked."""
        select_elements(qtbot, parameters_page, "Fe")

        qtbot.mouseClick(parameters_page.parametersPage.ClearAllPushButton, QtCore.Qt.MouseButton.LeftButton)

        assert confirm_clear.calls == 0
        assert parameters_page.selectedElements == {}

    def test_clearing_with_results_asks_for_confirmation(self, qtbot, parameters_page, confirm_clear):
        """Discarding calculated results requires a confirmation."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        qtbot.mouseClick(parameters_page.parametersPage.ClearAllPushButton, QtCore.Qt.MouseButton.LeftButton)

        assert confirm_clear.calls == 1

    def test_confirmed_clear_resets_everything(self, qtbot, parameters_page, confirm_clear):
        """Answering Yes empties the table, the tree and the selection."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        qtbot.mouseClick(parameters_page.parametersPage.ClearAllPushButton, QtCore.Qt.MouseButton.LeftButton)

        assert parameters_page.selectedElements == {}
        assert parameters_page.parametersPage.tableWidget.rowCount() == 0
        assert parameters_page.parametersPage.resultsTreeWidget.topLevelItemCount() == 0
        assert parameters_page.totalLabel.text() == ""

    def test_confirmed_clear_unchecks_every_element_button(self, qtbot, parameters_page, confirm_clear):
        """The periodic table returns to its unselected state."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        qtbot.mouseClick(parameters_page.parametersPage.ClearAllPushButton, QtCore.Qt.MouseButton.LeftButton)

        assert not any(element_button(parameters_page, symbol).isChecked() for symbol in EQUIMOLAR_ELEMENTS)

    def test_confirmed_clear_disables_the_action_buttons(self, qtbot, parameters_page, confirm_clear):
        """After clearing there is nothing to clear, calculate or save."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        qtbot.mouseClick(parameters_page.parametersPage.ClearAllPushButton, QtCore.Qt.MouseButton.LeftButton)

        assert not parameters_page.parametersPage.ClearAllPushButton.isEnabled()
        assert not parameters_page.parametersPage.CalculatePushButton.isEnabled()
        assert not parameters_page.parametersPage.SavePushButton.isEnabled()

    def test_cancelled_clear_changes_nothing(self, qtbot, parameters_page, cancel_clear):
        """Answering No leaves the results and selection intact."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        qtbot.mouseClick(parameters_page.parametersPage.ClearAllPushButton, QtCore.Qt.MouseButton.LeftButton)

        assert cancel_clear.calls == 1
        assert parameters_page.selectedElements == dict.fromkeys(EQUIMOLAR_ELEMENTS, 25.0)
        assert parameters_page.parametersPage.resultsTreeWidget.topLevelItemCount() == 1


class TestSave:
    """Tests for exporting the results tree to CSV."""

    def test_saving_with_no_results_warns(self, qtbot, parameters_page, cancelled_save):
        """Export is refused before anything has been calculated."""
        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            parameters_page.handleSaveButton()

        assert _last_notification(blocker) == ("There are no calculated results to save.", "warning")
        assert cancelled_save.calls == []

    def test_cancelling_the_dialog_writes_nothing(self, qtbot, parameters_page, cancelled_save, tmp_path):
        """Backing out of the save dialog leaves the filesystem untouched."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        parameters_page.handleSaveButton()

        assert len(cancelled_save.calls) == 1
        assert list(tmp_path.iterdir()) == []

    def test_successful_save_writes_the_file(self, qtbot, parameters_page, save_path):
        """Accepting the dialog produces a CSV on disk."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        parameters_page.handleSaveButton()

        assert save_path.exists()

    def test_saved_csv_has_the_core_headers_and_the_result_row(self, qtbot, parameters_page, save_path):
        """Row 0 is HEACalculator.get_headers(); row 1 is the tree content."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        parameters_page.handleSaveButton()

        with save_path.open(newline="") as handle:
            rows = list(csv.reader(handle))

        assert rows[0] == HEACalculator.get_headers()
        assert rows[1] == tree_rows(parameters_page.parametersPage.resultsTreeWidget)[0]
        assert len(rows) == 2

    def test_successful_save_notifies_with_the_file_name(self, qtbot, parameters_page, save_path):
        """The confirmation names the file, not the full path."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            parameters_page.handleSaveButton()

        assert _last_notification(blocker) == (f"Saved results to {save_path.name}.", "info")

    def test_dialog_opens_in_the_home_directory(self, qtbot, parameters_page, save_dialog_spy):
        """The save dialog starts somewhere portable across platforms."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        parameters_page.handleSaveButton()

        _parent, title, directory, file_filter = save_dialog_spy.calls[0]
        assert title == "Save CSV"
        assert directory == str(Path.home())
        assert file_filter == "CSV(*.csv)"

    def test_write_failure_notifies_the_user(self, qtbot, parameters_page, save_path, monkeypatch):
        """An unwritable destination reports the OS error instead of crashing."""
        select_elements(qtbot, parameters_page, *EQUIMOLAR_ELEMENTS)
        _calculate(qtbot, parameters_page)

        def _raise(*_args: object, **_kwargs: object) -> None:
            raise OSError("Permission denied")

        monkeypatch.setattr("builtins.open", _raise)

        with qtbot.waitSignal(parameters_page.notificationRequested) as blocker:
            parameters_page.handleSaveButton()

        assert _last_notification(blocker) == ("Could not save the results file. Permission denied", "error")


class TestResultsTreeContract:
    """Tests pinning the results tree to the core calculation payload."""

    def test_column_count_matches_the_calculation_payload(self, parameters_page):
        """Every value returned by get_list() has a column to live in."""
        tree = parameters_page.parametersPage.resultsTreeWidget

        assert tree.columnCount() == len(HEACalculator("CoCrFeMnNi").get_list())

    def test_displayed_headers_are_the_expected_short_labels(self, parameters_page):
        """The tree shows abbreviated headers, distinct from the CSV ones."""
        tree = parameters_page.parametersPage.resultsTreeWidget

        assert [tree.headerItem().text(index) for index in range(tree.columnCount())] == TREE_HEADERS

    def test_csv_headers_line_up_with_the_tree_columns(self, parameters_page):
        """The exported header row has one entry per displayed column."""
        assert len(HEACalculator.get_headers()) == parameters_page.parametersPage.resultsTreeWidget.columnCount()


class TestPageComposition:
    """Tests for widgets ParametersPage builds beyond the generated UI."""

    def test_total_label_is_right_aligned(self, parameters_page):
        """The running total sits flush against the table's right edge."""
        expected = QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter

        assert parameters_page.totalLabel.alignment() == expected

    def test_page_exposes_a_notification_signal(self, parameters_page):
        """The page delegates all user messaging to its parent window."""
        assert isinstance(parameters_page, QtWidgets.QWidget)
        assert hasattr(parameters_page, "notificationRequested")
