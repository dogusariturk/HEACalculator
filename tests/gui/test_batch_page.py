"""Tests for the BatchCalculationsPage composition screener."""

import csv
from pathlib import Path

import pytest
from conftest import element_button, select_elements, tree_rows
from PyQt6 import QtCore

from HEACalculator.core.hea import HEACalculator

ROW_A = ["Fe50Ni50"] + [str(index) for index in range(1, 26)]
ROW_B = ["Fe25Ni75"] + [str(index) for index in range(26, 51)]


def _search(qtbot, page) -> None:
    """Press the Search button.

    Args:
        qtbot: The pytest-qt bot used to deliver the click.
        page: The batch page under test.
    """
    qtbot.mouseClick(page.ui.btnSearch, QtCore.Qt.MouseButton.LeftButton)


def _clear(qtbot, page) -> None:
    """Press the Clear button.

    Args:
        qtbot: The pytest-qt bot used to deliver the click.
        page: The batch page under test.
    """
    qtbot.mouseClick(page.ui.btnClear, QtCore.Qt.MouseButton.LeftButton)


def _stub_worker_results(monkeypatch, results: list[tuple[list | None, str | None]]) -> None:
    """Make the range worker return canned rows instead of calculating.

    Args:
        monkeypatch: The pytest monkeypatch fixture.
        results: One ``(row, error)`` tuple per alloy, cycled if shorter.
    """
    pending = list(results)

    def _worker(_formula: str) -> tuple[list | None, str | None]:
        return pending.pop(0) if pending else (None, "exhausted")

    monkeypatch.setattr("HEACalculator.utils._range_worker", _worker)


def _run_search(qtbot, page, monkeypatch, results: list[tuple[list | None, str | None]]) -> None:
    """Drive a full stubbed search to completion.

    Args:
        qtbot: The pytest-qt bot.
        page: The batch page under test.
        monkeypatch: The pytest monkeypatch fixture.
        results: Canned ``(row, error)`` tuples for the worker.
    """
    _stub_worker_results(monkeypatch, results)
    # Element buttons toggle, so only click the ones that are not already selected.
    select_elements(qtbot, page, *[symbol for symbol in ("Fe", "Ni") if symbol not in page.selectedElements])
    page.ui.stepSpinBox.setValue(50.0)

    with qtbot.waitSignal(page.notificationRequested, timeout=5000):
        _search(qtbot, page)
    qtbot.waitUntil(page.ui.btnSearch.isEnabled, timeout=10000)


class TestInitialState:
    """Tests for the page's state before any interaction."""

    def test_no_elements_are_selected(self, batch_page):
        """Nothing is picked on a fresh page."""
        assert batch_page.selectedElements == []

    def test_results_tree_is_empty(self, batch_page):
        """No screening has run yet."""
        assert batch_page.ui.resultsTreeWidget.topLevelItemCount() == 0

    def test_save_starts_disabled(self, batch_page):
        """There is nothing to export before a search."""
        assert not batch_page.ui.btnSave.isEnabled()

    def test_search_starts_enabled(self, batch_page):
        """The user can start a search immediately."""
        assert batch_page.ui.btnSearch.isEnabled()

    @pytest.mark.parametrize(
        "spinbox,value",
        [("startSpinBox", 0.0), ("endSpinBox", 100.0), ("stepSpinBox", 5.0)],
        ids=["start", "end", "step"],
    )
    def test_range_defaults(self, batch_page, spinbox, value):
        """The range controls default to a full 0-100% sweep in 5% steps."""
        assert getattr(batch_page.ui, spinbox).value() == pytest.approx(value)

    @pytest.mark.parametrize("spinbox", ["startSpinBox", "endSpinBox", "stepSpinBox"])
    def test_range_controls_show_percent_suffix(self, batch_page, spinbox):
        """Each range control is labelled as a percentage."""
        assert getattr(batch_page.ui, spinbox).suffix() == " %"

    def test_step_is_rounded_to_one_decimal(self, batch_page):
        """setDecimals(1) runs after setRange, so the nominal 0.01 floor becomes 0.0."""
        assert batch_page.ui.stepSpinBox.decimals() == 1
        assert batch_page.ui.stepSpinBox.minimum() == pytest.approx(0.0)


class TestElementSelection:
    """Tests for the periodic-table selection list."""

    def test_clicking_adds_an_element(self, qtbot, batch_page):
        """A checked button appends its symbol."""
        select_elements(qtbot, batch_page, "Fe")

        assert batch_page.selectedElements == ["Fe"]

    def test_selection_preserves_click_order(self, qtbot, batch_page):
        """Elements accumulate in the order the user picked them."""
        select_elements(qtbot, batch_page, "Ni", "Fe", "Cr")

        assert batch_page.selectedElements == ["Ni", "Fe", "Cr"]

    def test_clicking_again_removes_the_element(self, qtbot, batch_page):
        """Unchecking a button drops its symbol."""
        select_elements(qtbot, batch_page, "Fe", "Ni")
        select_elements(qtbot, batch_page, "Fe")

        assert batch_page.selectedElements == ["Ni"]

    def test_neodymium_button_is_reachable_despite_its_object_name(self, qtbot, batch_page):
        """The Nd button is misnamed 'ebtnAnd' here too."""
        assert element_button(batch_page, "Nd").objectName() == "ebtnAnd"

        select_elements(qtbot, batch_page, "Nd")

        assert batch_page.selectedElements == ["Nd"]


class TestSearchValidation:
    """Tests for the input checks that run before a search starts."""

    def test_no_elements_warns(self, qtbot, batch_page):
        """Screening needs at least a binary system."""
        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            _search(qtbot, batch_page)

        assert tuple(blocker.args) == ("Select at least two elements using the periodic table.", "warning")

    def test_single_element_warns(self, qtbot, batch_page):
        """One element cannot produce a composition range."""
        select_elements(qtbot, batch_page, "Fe")

        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            _search(qtbot, batch_page)

        assert tuple(blocker.args)[1] == "warning"

    def test_start_above_end_errors(self, qtbot, batch_page):
        """An inverted range is rejected."""
        select_elements(qtbot, batch_page, "Fe", "Ni")
        batch_page.ui.startSpinBox.setValue(80.0)
        batch_page.ui.endSpinBox.setValue(20.0)

        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            _search(qtbot, batch_page)

        assert tuple(blocker.args) == ("Start % must not exceed End %.", "error")

    def test_enumeration_failure_errors(self, qtbot, batch_page, monkeypatch):
        """A crash while enumerating compositions is reported, not raised."""
        select_elements(qtbot, batch_page, "Fe", "Ni")

        def _raise(*_args: object) -> None:
            raise ValueError("bad formula")

        monkeypatch.setattr("HEACalculator.app.find_all_comps", _raise)

        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            _search(qtbot, batch_page)

        message, severity = tuple(blocker.args)
        assert severity == "error"
        assert message == "Could not enumerate compositions. bad formula"

    def test_empty_composition_set_warns(self, qtbot, batch_page, monkeypatch):
        """A range yielding nothing tells the user rather than silently finishing."""
        select_elements(qtbot, batch_page, "Fe", "Ni")
        monkeypatch.setattr("HEACalculator.app.find_all_comps", lambda *_args: ({"Fe": 0, "Ni": 0}, set()))

        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            _search(qtbot, batch_page)

        assert tuple(blocker.args) == ("No valid compositions found for the given range.", "warning")

    @pytest.mark.parametrize(
        "setup",
        ["none", "single", "inverted"],
        ids=["no_elements", "one_element", "start_above_end"],
    )
    def test_rejected_search_starts_no_worker(self, qtbot, batch_page, setup):
        """Validation failures leave the Search button usable and spawn no thread."""
        if setup == "single":
            select_elements(qtbot, batch_page, "Fe")
        elif setup == "inverted":
            select_elements(qtbot, batch_page, "Fe", "Ni")
            batch_page.ui.startSpinBox.setValue(80.0)
            batch_page.ui.endSpinBox.setValue(20.0)

        _search(qtbot, batch_page)

        assert batch_page._search_worker is None
        assert batch_page.ui.btnSearch.isEnabled()


class TestSearchExecution:
    """Tests for a search driven through a stubbed process pool."""

    def test_results_populate_the_tree(self, qtbot, batch_page, monkeypatch, stub_process_pool):
        """Each successful worker result becomes a tree row."""
        _run_search(qtbot, batch_page, monkeypatch, [(ROW_A, None)])

        assert tree_rows(batch_page.ui.resultsTreeWidget) == [ROW_A]

    def test_failed_rows_are_skipped(self, qtbot, batch_page, monkeypatch, stub_process_pool):
        """Alloys the core cannot calculate are dropped, not shown blank."""
        _run_search(qtbot, batch_page, monkeypatch, [(None, "missing data")])

        assert batch_page.ui.resultsTreeWidget.topLevelItemCount() == 0

    def test_search_button_is_disabled_while_running(self, qtbot, batch_page, monkeypatch, stub_process_pool):
        """The user cannot launch a second search on top of the first."""
        _stub_worker_results(monkeypatch, [(ROW_A, None)])
        select_elements(qtbot, batch_page, "Fe", "Ni")
        batch_page.ui.stepSpinBox.setValue(50.0)

        states = []
        batch_page.notificationRequested.connect(lambda *_: states.append(batch_page.ui.btnSearch.isEnabled()))

        _search(qtbot, batch_page)
        qtbot.waitUntil(batch_page.ui.btnSearch.isEnabled, timeout=10000)

        assert states[0] is False

    def test_completion_reenables_search(self, qtbot, batch_page, monkeypatch, stub_process_pool):
        """The page returns to an interactive state when the worker finishes."""
        _run_search(qtbot, batch_page, monkeypatch, [(ROW_A, None)])

        assert batch_page.ui.btnSearch.isEnabled()

    def test_completion_enables_save(self, qtbot, batch_page, monkeypatch, stub_process_pool):
        """A non-empty result set unlocks CSV export."""
        _run_search(qtbot, batch_page, monkeypatch, [(ROW_A, None)])

        assert batch_page.ui.btnSave.isEnabled()

    def test_a_new_search_clears_previous_results(self, qtbot, batch_page, monkeypatch, stub_process_pool):
        """Results do not accumulate across searches."""
        _run_search(qtbot, batch_page, monkeypatch, [(ROW_A, None)])
        _run_search(qtbot, batch_page, monkeypatch, [(ROW_B, None)])

        assert tree_rows(batch_page.ui.resultsTreeWidget) == [ROW_B]

    def test_search_uses_the_stubbed_executor(self, qtbot, batch_page, monkeypatch, stub_process_pool):
        """The worker really does go through ProcessPoolExecutor."""
        _run_search(qtbot, batch_page, monkeypatch, [(ROW_A, None)])

        assert len(stub_process_pool.instances) == 1


class TestSearchFinishedNotifications:
    """Tests for the messages emitted when a search completes."""

    def test_zero_results_warns(self, qtbot, batch_page):
        """An all-failed screen explains why nothing appeared."""
        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            batch_page._on_search_finished(0)

        expected = ("No compositions could be calculated (missing database entries).", "warning")
        assert tuple(blocker.args) == expected

    def test_zero_results_leaves_save_disabled(self, qtbot, batch_page):
        """There is still nothing to export."""
        batch_page._on_search_finished(0)

        assert not batch_page.ui.btnSave.isEnabled()

    def test_successful_completion_reports_the_count(self, qtbot, batch_page):
        """The confirmation names how many compositions were calculated."""
        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            batch_page._on_search_finished(42)

        assert tuple(blocker.args) == ("Search completed. 42 compositions calculated.", "info")

    def test_result_ready_appends_one_row(self, batch_page):
        """Each emitted result becomes exactly one top-level item."""
        batch_page._on_result_ready(ROW_A)
        batch_page._on_result_ready(ROW_B)

        assert tree_rows(batch_page.ui.resultsTreeWidget) == [ROW_A, ROW_B]


class TestClear:
    """Tests for the Clear action and its confirmation dialog."""

    def test_clearing_an_untouched_page_skips_the_dialog(self, qtbot, batch_page, confirm_clear):
        """With nothing selected and nothing found, no confirmation is needed."""
        _clear(qtbot, batch_page)

        assert confirm_clear.calls == 0

    def test_clearing_a_selection_asks_for_confirmation(self, qtbot, batch_page, confirm_clear):
        """Discarding a selection requires a confirmation."""
        select_elements(qtbot, batch_page, "Fe", "Ni")

        _clear(qtbot, batch_page)

        assert confirm_clear.calls == 1

    def test_confirmed_clear_resets_selection_and_results(self, qtbot, batch_page, confirm_clear):
        """Answering Yes empties both the selection and the tree."""
        select_elements(qtbot, batch_page, "Fe", "Ni")
        batch_page._on_result_ready(ROW_A)

        _clear(qtbot, batch_page)

        assert batch_page.selectedElements == []
        assert batch_page.ui.resultsTreeWidget.topLevelItemCount() == 0

    def test_confirmed_clear_unchecks_element_buttons(self, qtbot, batch_page, confirm_clear):
        """The periodic table returns to its unselected state."""
        select_elements(qtbot, batch_page, "Fe", "Ni")

        _clear(qtbot, batch_page)

        assert not element_button(batch_page, "Fe").isChecked()
        assert not element_button(batch_page, "Ni").isChecked()

    def test_confirmed_clear_disables_save(self, qtbot, batch_page, confirm_clear):
        """Clearing removes the thing Save would have exported."""
        batch_page._on_result_ready(ROW_A)
        batch_page.ui.btnSave.setEnabled(True)

        _clear(qtbot, batch_page)

        assert not batch_page.ui.btnSave.isEnabled()

    def test_cancelled_clear_changes_nothing(self, qtbot, batch_page, cancel_clear):
        """Answering No preserves the selection and results."""
        select_elements(qtbot, batch_page, "Fe", "Ni")
        batch_page._on_result_ready(ROW_A)

        _clear(qtbot, batch_page)

        assert cancel_clear.calls == 1
        assert batch_page.selectedElements == ["Fe", "Ni"]
        assert batch_page.ui.resultsTreeWidget.topLevelItemCount() == 1


class TestSave:
    """Tests for exporting screening results to CSV."""

    def test_saving_with_no_results_warns(self, qtbot, batch_page, cancelled_save):
        """Export is refused before a search has produced anything."""
        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            batch_page._handle_save()

        assert tuple(blocker.args) == ("No results to save.", "warning")
        assert cancelled_save.calls == []

    def test_cancelling_the_dialog_writes_nothing(self, qtbot, batch_page, cancelled_save, tmp_path):
        """Backing out leaves the filesystem untouched."""
        batch_page._on_result_ready(ROW_A)

        batch_page._handle_save()

        assert len(cancelled_save.calls) == 1
        assert list(tmp_path.iterdir()) == []

    def test_saved_csv_has_headers_and_rows(self, qtbot, batch_page, save_path):
        """Row 0 is the core header list; the rest are the screened alloys."""
        batch_page._on_result_ready(ROW_A)
        batch_page._on_result_ready(ROW_B)

        batch_page._handle_save()

        with save_path.open(newline="") as handle:
            rows = list(csv.reader(handle))

        assert rows == [HEACalculator.get_headers(), ROW_A, ROW_B]

    def test_successful_save_notifies_with_the_file_name(self, qtbot, batch_page, save_path):
        """The confirmation names the file, not the full path."""
        batch_page._on_result_ready(ROW_A)

        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            batch_page._handle_save()

        assert tuple(blocker.args) == (f"Saved results to {save_path.name}.", "info")

    def test_dialog_opens_in_the_home_directory(self, qtbot, batch_page, save_dialog_spy):
        """The save dialog starts somewhere portable across platforms."""
        batch_page._on_result_ready(ROW_A)

        batch_page._handle_save()

        _parent, title, directory, file_filter = save_dialog_spy.calls[0]
        assert title == "Save CSV"
        assert directory == str(Path.home())
        assert file_filter == "CSV(*.csv)"

    def test_write_failure_notifies_the_user(self, qtbot, batch_page, save_path, monkeypatch):
        """An unwritable destination reports the OS error instead of crashing."""
        batch_page._on_result_ready(ROW_A)

        def _raise(*_args: object, **_kwargs: object) -> None:
            raise OSError("Permission denied")

        monkeypatch.setattr("builtins.open", _raise)

        with qtbot.waitSignal(batch_page.notificationRequested) as blocker:
            batch_page._handle_save()

        assert tuple(blocker.args) == ("Could not save the results file. Permission denied", "error")
