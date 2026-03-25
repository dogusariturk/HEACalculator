"""Tests for app.py GUI module.

All tests are skipped when PyQt5 is not installed or no display is available.
"""

import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import MagicMock, mock_open, patch

import pytest

PyQt5 = pytest.importorskip("PyQt5", reason="PyQt5 not installed")

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from HEACalculator.app import AlignDelegate, HEACalculatorMainWindow, ItemDelegate, NotificationBar, ParametersPage, run


class TestAppImportGuard(TestCase):
    """Tests for the PyQt5 availability guard at module import time."""

    def test_missing_pyqt5_raises_system_exit(self):
        """Importing app.py without PyQt5 available raises SystemExit."""
        root_dir = Path(__file__).resolve().parents[1]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(root_dir / "src")

        result = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "import sys;"
                    "sys.modules['PyQt5']=None;"
                    "sys.modules['PyQt5.QtCore']=None;"
                    "sys.modules['PyQt5.QtGui']=None;"
                    "sys.modules['PyQt5.QtWidgets']=None;"
                    "import HEACalculator.app"
                ),
            ],
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )

        assert result.returncode != 0
        assert "PyQt5 is required for GUI mode." in result.stderr


class TestHEACalculatorMainWindowConstants(TestCase):
    """Tests for compile-time color constants on HEACalculatorMainWindow."""

    def test_highlighted_color_constant_contains_hex(self):
        """The highlighted button color constant contains a valid hex color string."""
        assert "#3E5C76" in HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_HIGHLIGHTED

    def test_default_color_constant_contains_hex(self):
        """The default button color constant contains a valid hex color string."""
        assert "#1D2D44" in HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_DEFAULT

    def test_color_constants_are_different(self):
        """The highlighted and default color constants are distinct values."""
        assert HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_HIGHLIGHTED != HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_DEFAULT


class TestRunFunction(TestCase):
    """Tests for the run() entry point function."""

    def test_run_creates_qapplication(self):
        """run() instantiates QApplication and calls show() on the main window."""
        mock_app = MagicMock()
        mock_desktop = MagicMock()
        mock_desktop.availableGeometry.return_value.width.return_value = 1920
        mock_desktop.availableGeometry.return_value.height.return_value = 1080
        mock_window = MagicMock()
        mock_window.width.return_value = 800
        mock_window.height.return_value = 600
        mock_app.exec_.return_value = 0

        with (
            patch("HEACalculator.app.QtWidgets.QApplication", return_value=mock_app),
            patch("HEACalculator.app.HEACalculatorMainWindow", return_value=mock_window),
            patch("HEACalculator.app.QtWidgets.QDesktopWidget", return_value=mock_desktop),
            patch("HEACalculator.app.QtGui.QPixmap"),
            patch("HEACalculator.app.QtGui.QIcon"),
            patch("sys.exit"),
        ):
            run()
            mock_window.show.assert_called_once()


class TestNotificationBar(TestCase):
    """Tests for the in-window notification banner."""

    def test_show_message_sets_style_text_and_timer(self):
        """Showing a message updates styling, text, visibility, and auto-dismiss."""
        notification_bar = SimpleNamespace(
            STYLES=NotificationBar.STYLES,
            AUTO_DISMISS_MS=NotificationBar.AUTO_DISMISS_MS,
            setStyleSheet=MagicMock(),
            messageLabel=MagicMock(),
            setVisible=MagicMock(),
            dismissTimer=MagicMock(),
        )

        NotificationBar.show_message(notification_bar, "Calculation failed.", "error")

        style_sheet = notification_bar.setStyleSheet.call_args.args[0]
        assert "#6E4651" in style_sheet
        notification_bar.messageLabel.setText.assert_called_once_with("Calculation failed.")
        notification_bar.setVisible.assert_called_once_with(True)
        notification_bar.dismissTimer.start.assert_called_once_with(NotificationBar.AUTO_DISMISS_MS)

    def test_show_message_rejects_unknown_severity(self):
        """Unknown severities raise a ValueError."""
        notification_bar = SimpleNamespace(
            STYLES=NotificationBar.STYLES,
            AUTO_DISMISS_MS=NotificationBar.AUTO_DISMISS_MS,
            setStyleSheet=MagicMock(),
            messageLabel=MagicMock(),
            setVisible=MagicMock(),
            dismissTimer=MagicMock(),
        )

        with pytest.raises(ValueError):
            NotificationBar.show_message(notification_bar, "Saved results.", "debug")

    def test_hide_message_stops_timer_and_hides_banner(self):
        """Hiding a message stops the timer and hides the banner."""
        notification_bar = SimpleNamespace(
            dismissTimer=MagicMock(),
            setVisible=MagicMock(),
        )

        NotificationBar.hide_message(notification_bar)

        notification_bar.dismissTimer.stop.assert_called_once_with()
        notification_bar.setVisible.assert_called_once_with(False)


class TestParametersPageNotifications(TestCase):
    """Tests for ParametersPage notification behavior."""

    def test_formula_notification_format_uses_subscripts(self):
        """Formula fragments in notifications are formatted with HTML subscripts."""
        assert (
            ParametersPage._format_formula_for_notification("Fe25Co25Cr25Ni25")
            == "Fe<sub>25</sub>Co<sub>25</sub>Cr<sub>25</sub>Ni<sub>25</sub>"
        )

    def test_calculate_failure_emits_error_notification(self):
        """Calculation errors are emitted as error notifications."""
        notifications = []
        parameters_page = SimpleNamespace(
            parametersPage=SimpleNamespace(
                resultsTreeWidget=MagicMock(),
                SavePushButton=MagicMock(),
            ),
            _show_notification=lambda message, severity: notifications.append((message, severity)),
            _format_formula_for_notification=ParametersPage._format_formula_for_notification,
        )
        parameters_page.parametersPage.resultsTreeWidget.findItems.return_value = []
        parameters_page._clean_error_message = ParametersPage._clean_error_message
        parameters_page._ERROR_PREFIXES = ParametersPage._ERROR_PREFIXES
        parameters_page._format_calculation_error = lambda error: ParametersPage._format_calculation_error(parameters_page, error)

        with patch(
            "HEACalculator.app.HEACalculator",
            side_effect=KeyError("The requested pair does not exist in the formation enthalpy database."),
        ):
            ParametersPage.calculate(parameters_page, "Sm50Fe50")

        assert notifications == [
            (
                "Calculation failed because formation enthalpy data is missing for "
                "one or more selected element pairs. The requested pair does not "
                "exist in the formation enthalpy database.",
                "error",
            )
        ]
        parameters_page.parametersPage.SavePushButton.setEnabled.assert_not_called()

    def test_duplicate_calculation_emits_warning_notification(self):
        """Recalculating the same formula shows a warning notification."""
        notifications = []
        parameters_page = SimpleNamespace(
            parametersPage=SimpleNamespace(
                resultsTreeWidget=MagicMock(),
                SavePushButton=MagicMock(),
            ),
            _show_notification=lambda message, severity: notifications.append((message, severity)),
            _format_formula_for_notification=ParametersPage._format_formula_for_notification,
        )
        parameters_page.parametersPage.resultsTreeWidget.findItems.return_value = [object()]

        ParametersPage.calculate(parameters_page, "FeCoCrNi")

        assert notifications == [("FeCoCrNi has already been calculated.", "warning")]

    def test_duplicate_calculation_formats_formula_with_subscripts(self):
        """Duplicate-calculation notifications render formula numbers as subscripts."""
        notifications = []
        parameters_page = SimpleNamespace(
            parametersPage=SimpleNamespace(
                resultsTreeWidget=MagicMock(),
                SavePushButton=MagicMock(),
            ),
            _show_notification=lambda message, severity: notifications.append((message, severity)),
        )
        parameters_page.parametersPage.resultsTreeWidget.findItems.return_value = [object()]
        parameters_page._format_formula_for_notification = ParametersPage._format_formula_for_notification

        ParametersPage.calculate(parameters_page, "Fe25Co25")

        assert notifications == [
            (
                "Fe<sub>25</sub>Co<sub>25</sub> has already been calculated.",
                "warning",
            )
        ]

    def test_success_notification_formats_formula_with_subscripts(self):
        """Success notifications render formula numbers as subscripts."""
        notifications = []
        parameters_page = SimpleNamespace(
            parametersPage=SimpleNamespace(
                resultsTreeWidget=MagicMock(),
                SavePushButton=MagicMock(),
            ),
            _show_notification=lambda message, severity: notifications.append((message, severity)),
            _format_formula_for_notification=ParametersPage._format_formula_for_notification,
        )
        parameters_page.parametersPage.resultsTreeWidget.findItems.return_value = []

        calculator = MagicMock()
        calculator.get_list.return_value = ["Fe25Co25"]

        with (
            patch("HEACalculator.app.HEACalculator", return_value=calculator),
            patch("HEACalculator.app.QtWidgets.QTreeWidgetItem"),
        ):
            ParametersPage.calculate(parameters_page, "Fe25Co25")

        assert notifications == [("Fe<sub>25</sub>Co<sub>25</sub> calculation completed.", "info")]

    def test_save_failure_emits_error_notification(self):
        """Save errors are emitted as error notifications."""
        notifications = []
        results_tree = MagicMock()
        results_tree.topLevelItemCount.return_value = 1
        results_tree.columnCount.return_value = 1
        results_tree.headerItem.return_value.text.return_value = "Formula"
        parameters_page = SimpleNamespace(
            parametersPage=SimpleNamespace(resultsTreeWidget=results_tree),
            _show_notification=lambda message, severity: notifications.append((message, severity)),
        )
        parameters_page._clean_error_message = ParametersPage._clean_error_message
        parameters_page._format_save_error = lambda error: ParametersPage._format_save_error(parameters_page, error)

        with (
            patch(
                "HEACalculator.app.QtWidgets.QFileDialog.getSaveFileName",
                return_value=("/tmp/results.csv", True),
            ),
            patch("builtins.open", side_effect=OSError("Permission denied")),
        ):
            ParametersPage.handleSaveButton(parameters_page)

        assert notifications == [("Could not save the results file. Permission denied", "error")]


class TestMainWindowNotifications(TestCase):
    """Tests for notification routing in the main window."""

    def test_show_notification_routes_to_banner(self):
        """The main window forwards notifications to the banner widget."""
        window = SimpleNamespace(notificationBar=MagicMock())

        HEACalculatorMainWindow.show_notification(window, "Saved results.", "info")

        window.notificationBar.show_message.assert_called_once_with("Saved results.", "info")


@pytest.fixture(scope="session")
def qapp():
    """Session-scoped QApplication for widget-level tests."""
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    yield app


class TestCleanErrorMessage(TestCase):
    """Tests for the ParametersPage._clean_error_message static method."""

    def test_string_first_arg_returns_that_string(self):
        """A string first argument is returned verbatim."""
        assert ParametersPage._clean_error_message(KeyError("missing key")) == "missing key"

    def test_non_string_first_arg_returns_str_representation(self):
        """A non-string first argument is converted with str()."""
        assert ParametersPage._clean_error_message(KeyError(42)) == "42"

    def test_no_args_returns_str_of_exception(self):
        """An exception with no arguments returns str() of the exception."""
        error = ValueError()
        assert ParametersPage._clean_error_message(error) == str(error)


class TestFormatCalculationError(TestCase):
    """Tests for the _format_calculation_error instance method."""

    def _make_page(self):
        p = SimpleNamespace()
        p._ERROR_PREFIXES = ParametersPage._ERROR_PREFIXES
        p._clean_error_message = ParametersPage._clean_error_message
        p._format_calculation_error = lambda e: ParametersPage._format_calculation_error(p, e)
        return p

    def test_formation_enthalpy_keyword_uses_its_prefix(self):
        """Errors mentioning the formation enthalpy database use the formation enthalpy prefix."""
        p = self._make_page()
        result = p._format_calculation_error(KeyError("pair not in formation enthalpy database."))
        assert "formation enthalpy data is missing" in result

    def test_mixing_enthalpy_keyword_uses_its_prefix(self):
        """Errors mentioning the mixing enthalpy database use the mixing enthalpy prefix."""
        p = self._make_page()
        result = p._format_calculation_error(KeyError("not found in mixing enthalpy database"))
        assert "mixing enthalpy data is missing" in result

    def test_elements_database_keyword_uses_its_prefix(self):
        """Errors mentioning the elements database use the elements database prefix."""
        p = self._make_page()
        result = p._format_calculation_error(KeyError("missing in elements database"))
        assert "not available in the database" in result

    def test_extra_letters_keyword_uses_its_prefix(self):
        """Errors about extra letters use the formula-parsing prefix."""
        p = self._make_page()
        result = p._format_calculation_error(ValueError("extra letters were detected in formula"))
        assert "could not be parsed" in result

    def test_unrecognized_error_uses_fallback_prefix(self):
        """Errors without a recognized keyword fall back to the generic prefix."""
        p = self._make_page()
        result = p._format_calculation_error(RuntimeError("unexpected problem"))
        assert result.startswith("Calculation failed.")
        assert "unexpected problem" in result


class TestFormatSaveError(TestCase):
    """Tests for the _format_save_error instance method."""

    def test_os_error_produces_user_friendly_message(self):
        """An OSError is wrapped into a user-facing save-error message."""
        p = SimpleNamespace()
        p._clean_error_message = ParametersPage._clean_error_message
        p._format_save_error = lambda e: ParametersPage._format_save_error(p, e)
        assert p._format_save_error(OSError("Permission denied")) == "Could not save the results file. Permission denied"


class TestUpdateActionButtons(TestCase):
    """Tests for ParametersPage._update_action_buttons."""

    def _call(self, selected_elements, tree_count):
        tree = MagicMock()
        tree.topLevelItemCount.return_value = tree_count
        p = SimpleNamespace(
            selectedElements=selected_elements,
            parametersPage=SimpleNamespace(
                resultsTreeWidget=tree,
                ClearAllPushButton=MagicMock(),
                CalculatePushButton=MagicMock(),
                SavePushButton=MagicMock(),
            ),
        )
        ParametersPage._update_action_buttons(p)
        return p

    def test_no_elements_no_results_disables_all_action_buttons(self):
        """All action buttons are disabled when there are no elements and no results."""
        p = self._call({}, 0)
        p.parametersPage.ClearAllPushButton.setEnabled.assert_called_once_with(False)
        p.parametersPage.CalculatePushButton.setEnabled.assert_called_once_with(False)
        p.parametersPage.SavePushButton.setEnabled.assert_called_once_with(False)

    def test_has_elements_enables_clear_and_calculate(self):
        """ClearAll and Calculate are enabled when at least one element is selected."""
        p = self._call({"Fe": 100.0}, 0)
        p.parametersPage.ClearAllPushButton.setEnabled.assert_called_once_with(True)
        p.parametersPage.CalculatePushButton.setEnabled.assert_called_once_with(True)

    def test_has_results_enables_save(self):
        """Save is enabled when the results tree contains at least one row."""
        p = self._call({"Fe": 100.0}, 1)
        p.parametersPage.SavePushButton.setEnabled.assert_called_once_with(True)

    def test_no_elements_with_results_disables_clear_and_calculate_enables_save(self):
        """Save stays enabled even when no elements are selected (results persist)."""
        p = self._call({}, 3)
        p.parametersPage.ClearAllPushButton.setEnabled.assert_called_once_with(False)
        p.parametersPage.CalculatePushButton.setEnabled.assert_called_once_with(False)
        p.parametersPage.SavePushButton.setEnabled.assert_called_once_with(True)


class TestHandleAmountChanged(TestCase):
    """Tests for ParametersPage.handleAmountChanged."""

    def _make_page(self, selected_elements, row_values):
        """row_values: list of (element, amount_str) tuples indexed by row."""

        def table_item(row, col):
            item = MagicMock()
            item.text.return_value = row_values[row][col]
            return item

        table = MagicMock()
        table.item.side_effect = table_item
        p = SimpleNamespace(
            selectedElements=dict(selected_elements),
            _update_total_label=MagicMock(),
            _show_notification=MagicMock(),
            parametersPage=SimpleNamespace(tableWidget=table),
        )
        return p

    def test_column_1_edit_updates_element_percentage(self):
        """Editing the amount column (1) syncs the new value into selectedElements."""
        p = self._make_page({"Fe": 50.0, "Co": 50.0}, [("Fe", "75.0")])
        ParametersPage.handleAmountChanged(p, 0, 1)
        assert p.selectedElements["Fe"] == 75.0

    def test_column_0_edit_does_not_update_selected_elements(self):
        """Changes to the element-name column (0) are ignored."""
        p = self._make_page({"Fe": 50.0}, [("Fe", "50.0")])
        ParametersPage.handleAmountChanged(p, 0, 0)
        p.parametersPage.tableWidget.item.assert_not_called()
        assert p.selectedElements["Fe"] == 50.0

    def test_element_not_in_selected_elements_is_ignored(self):
        """An edit for an element absent from selectedElements has no effect."""
        p = self._make_page({"Co": 100.0}, [("Fe", "30.0")])
        ParametersPage.handleAmountChanged(p, 0, 1)
        assert "Fe" not in p.selectedElements
        assert p.selectedElements["Co"] == 100.0


class TestHandleCalculateButton(TestCase):
    """Tests for ParametersPage.handleCalculateButton."""

    def _make_page(self, selected_elements):
        notifications = []
        calculate_calls = []
        p = SimpleNamespace(
            selectedElements=dict(selected_elements),
            _show_notification=lambda msg, sev: notifications.append((msg, sev)),
            calculate=calculate_calls.append,
        )
        p._notifications = notifications
        p._calculate_calls = calculate_calls
        return p

    def test_percentages_below_100_emits_warning_with_actual_total(self):
        """A sum below 100% emits a warning that includes the computed total."""
        p = self._make_page({"Fe": 50.0, "Co": 25.0})
        ParametersPage.handleCalculateButton(p)
        assert p._notifications == [("Element percentages sum to 75.00% (expected 100%). Adjust before calculating.", "warning")]

    def test_percentages_above_100_emits_warning(self):
        """A sum above 100% also emits a warning."""
        p = self._make_page({"Fe": 60.0, "Co": 60.0})
        ParametersPage.handleCalculateButton(p)
        assert p._notifications[0][1] == "warning"

    def test_percentages_exactly_100_triggers_calculate(self):
        """When the sum equals 100%, calculate() is called and no warning is shown."""
        p = self._make_page({"Fe": 50.0, "Co": 50.0})
        ParametersPage.handleCalculateButton(p)
        assert len(p._calculate_calls) == 1
        assert not p._notifications

    def test_formula_uses_alphabetically_sorted_elements(self):
        """The formula string passed to calculate() has elements in alphabetical order."""
        p = self._make_page({"Ni": 25.0, "Co": 25.0, "Fe": 25.0, "Cr": 25.0})
        ParametersPage.handleCalculateButton(p)
        assert p._calculate_calls[0] == "Co25Cr25Fe25Ni25"

    def test_empty_selection_emits_sum_zero_warning(self):
        """An empty element selection (sum=0) emits a warning indicating 0%."""
        p = self._make_page({})
        ParametersPage.handleCalculateButton(p)
        assert p._notifications[0][1] == "warning"
        assert "0.00%" in p._notifications[0][0]


class TestHandleElementClicked(TestCase):
    """Tests for ParametersPage.handleElementClicked."""

    def _make_page(self, selected_elements=None, row_count=0):
        table = MagicMock()
        table.rowCount.return_value = row_count
        p = SimpleNamespace(
            selectedElements=dict(selected_elements or {}),
            _update_total_label=MagicMock(),
            parametersPage=SimpleNamespace(
                tableWidget=table,
                resultsTreeWidget=MagicMock(),
                ClearAllPushButton=MagicMock(),
                CalculatePushButton=MagicMock(),
                SavePushButton=MagicMock(),
            ),
            _update_action_buttons=MagicMock(),
        )
        return p

    def test_check_true_new_element_adds_to_selected_elements_at_100_percent(self):
        """Checking the first element sets it to 100% in selectedElements."""
        p = self._make_page()
        with patch("HEACalculator.app.QtWidgets.QTableWidgetItem", return_value=MagicMock()):
            ParametersPage.handleElementClicked(p, "Fe", True)
        assert p.selectedElements == {"Fe": pytest.approx(100.0)}

    def test_check_true_second_element_redistributes_to_50_percent_each(self):
        """Adding a second element redistributes both elements to 50%."""
        p = self._make_page({"Fe": 100.0}, row_count=1)
        with patch("HEACalculator.app.QtWidgets.QTableWidgetItem", return_value=MagicMock()):
            ParametersPage.handleElementClicked(p, "Co", True)
        assert p.selectedElements["Fe"] == pytest.approx(50.0)
        assert p.selectedElements["Co"] == pytest.approx(50.0)

    def test_check_true_already_selected_element_does_nothing(self):
        """Checking an element that is already selected has no effect."""
        p = self._make_page({"Fe": 100.0}, row_count=1)
        ParametersPage.handleElementClicked(p, "Fe", True)
        assert len(p.selectedElements) == 1
        p.parametersPage.tableWidget.insertRow.assert_not_called()

    def test_check_false_removes_element_from_selected_elements(self):
        """Unchecking an element removes it from selectedElements."""
        p = self._make_page({"Fe": 50.0, "Co": 50.0}, row_count=1)
        mock_item = MagicMock()
        mock_item.row.return_value = 0
        p.parametersPage.tableWidget.findItems.return_value = [mock_item]
        ParametersPage.handleElementClicked(p, "Fe", False)
        assert "Fe" not in p.selectedElements

    def test_check_false_redistributes_remaining_element_to_100_percent(self):
        """After removing one of two elements the remaining element gets 100%."""
        p = self._make_page({"Fe": 50.0, "Co": 50.0}, row_count=0)
        mock_item = MagicMock()
        mock_item.row.return_value = 0
        p.parametersPage.tableWidget.findItems.return_value = [mock_item]
        ParametersPage.handleElementClicked(p, "Fe", False)
        assert p.selectedElements["Co"] == pytest.approx(100.0)

    def test_check_false_element_not_in_selected_elements_does_nothing(self):
        """Unchecking an element that was never selected has no effect."""
        p = self._make_page({"Co": 100.0})
        original = dict(p.selectedElements)
        ParametersPage.handleElementClicked(p, "Fe", False)
        assert p.selectedElements == original
        p.parametersPage.tableWidget.removeRow.assert_not_called()

    def test_check_true_calls_update_action_buttons(self):
        """Adding an element triggers a button-state refresh."""
        p = self._make_page()
        with patch("HEACalculator.app.QtWidgets.QTableWidgetItem", return_value=MagicMock()):
            ParametersPage.handleElementClicked(p, "Fe", True)
        p._update_action_buttons.assert_called_once()


class TestHandleClearAllButton(TestCase):
    """Tests for ParametersPage.handleClearAllButton."""

    def _make_page(self, selected_elements=None, tree_count=0):
        tree = MagicMock()
        tree.topLevelItemCount.return_value = tree_count
        p = SimpleNamespace(
            selectedElements=dict(selected_elements or {}),
            _update_total_label=MagicMock(),
            _element_buttons=[MagicMock(), MagicMock()],
            parametersPage=SimpleNamespace(
                tableWidget=MagicMock(),
                resultsTreeWidget=tree,
                ClearAllPushButton=MagicMock(),
                CalculatePushButton=MagicMock(),
                SavePushButton=MagicMock(),
            ),
            _update_action_buttons=MagicMock(),
        )
        return p

    def test_no_results_clears_without_showing_dialog(self):
        """When the results tree is empty, ClearAll clears immediately with no confirmation dialog."""
        p = self._make_page({"Fe": 100.0}, tree_count=0)
        with patch("HEACalculator.app.QMessageBox") as mock_cls:
            ParametersPage.handleClearAllButton(p)
            mock_cls.assert_not_called()
        assert p.selectedElements == {}
        p.parametersPage.tableWidget.setRowCount.assert_called_once_with(0)

    def test_with_results_user_confirms_yes_clears_everything(self):
        """Confirming the dialog clears elements, table, and results tree."""
        p = self._make_page({"Fe": 50.0, "Co": 50.0}, tree_count=1)
        yes_value = QMessageBox.Yes
        with patch("HEACalculator.app.QMessageBox") as mock_cls:
            mock_box = MagicMock()
            mock_cls.return_value = mock_box
            mock_cls.Yes = yes_value
            mock_box.exec_.return_value = yes_value
            ParametersPage.handleClearAllButton(p)
        assert p.selectedElements == {}
        p.parametersPage.resultsTreeWidget.clear.assert_called_once()
        p.parametersPage.tableWidget.setRowCount.assert_called_once_with(0)

    def test_with_results_user_cancels_no_does_not_clear(self):
        """Dismissing the dialog with No leaves selectedElements and the tree untouched."""
        p = self._make_page({"Fe": 100.0}, tree_count=1)
        original = dict(p.selectedElements)
        yes_value = QMessageBox.Yes
        with patch("HEACalculator.app.QMessageBox") as mock_cls:
            mock_box = MagicMock()
            mock_cls.return_value = mock_box
            mock_cls.Yes = yes_value
            mock_box.exec_.return_value = QMessageBox.No
            ParametersPage.handleClearAllButton(p)
        assert p.selectedElements == original
        p.parametersPage.tableWidget.setRowCount.assert_not_called()


class TestHandleSaveButton(TestCase):
    """Tests for ParametersPage.handleSaveButton."""

    def _make_page(self, tree_count, notifications=None):
        if notifications is None:
            notifications = []
        tree = MagicMock()
        tree.topLevelItemCount.return_value = tree_count
        tree.columnCount.return_value = 1
        tree.headerItem.return_value.text.return_value = "Formula"
        mock_row_item = MagicMock()
        mock_row_item.text.return_value = "FeCoCrNi"
        tree.topLevelItem.return_value = mock_row_item
        p = SimpleNamespace(
            parametersPage=SimpleNamespace(resultsTreeWidget=tree),
            _show_notification=lambda msg, sev: notifications.append((msg, sev)),
        )
        p._clean_error_message = ParametersPage._clean_error_message
        p._format_save_error = lambda e: ParametersPage._format_save_error(p, e)
        p._notifications = notifications
        return p

    def test_empty_tree_emits_warning_notification(self):
        """Clicking Save with no results emits a warning instead of opening a dialog."""
        p = self._make_page(0)
        ParametersPage.handleSaveButton(p)
        assert p._notifications == [("There are no calculated results to save.", "warning")]

    def test_dialog_cancelled_does_not_write_file(self):
        """Cancelling the save dialog writes nothing and emits no notification."""
        p = self._make_page(1)
        with (
            patch("HEACalculator.app.QtWidgets.QFileDialog.getSaveFileName", return_value=("", False)),
            patch("builtins.open", mock_open()) as m,
        ):
            ParametersPage.handleSaveButton(p)
            m.assert_not_called()
        assert not p._notifications

    def test_successful_save_emits_info_notification_with_filename(self):
        """A successful save emits an info notification that includes the file name."""
        p = self._make_page(1)
        with (
            patch("HEACalculator.app.QtWidgets.QFileDialog.getSaveFileName", return_value=("/tmp/out.csv", True)),
            patch("builtins.open", mock_open()),
        ):
            ParametersPage.handleSaveButton(p)
        assert any(sev == "info" and "out.csv" in msg for msg, sev in p._notifications)

    def test_os_error_during_write_emits_error_notification(self):
        """An OSError while writing emits an error notification with the OS message."""
        p = self._make_page(1)
        with (
            patch("HEACalculator.app.QtWidgets.QFileDialog.getSaveFileName", return_value=("/tmp/out.csv", True)),
            patch("builtins.open", side_effect=OSError("Disk full")),
        ):
            ParametersPage.handleSaveButton(p)
        assert p._notifications == [("Could not save the results file. Disk full", "error")]


class TestCalculateAdditional(TestCase):
    """Additional tests for ParametersPage.calculate."""

    def _make_page(self, notifications=None):
        if notifications is None:
            notifications = []
        p = SimpleNamespace(
            parametersPage=SimpleNamespace(
                resultsTreeWidget=MagicMock(),
                SavePushButton=MagicMock(),
            ),
            _show_notification=lambda msg, sev: notifications.append((msg, sev)),
            _format_formula_for_notification=ParametersPage._format_formula_for_notification,
        )
        p._clean_error_message = ParametersPage._clean_error_message
        p._ERROR_PREFIXES = ParametersPage._ERROR_PREFIXES
        p._format_calculation_error = lambda e: ParametersPage._format_calculation_error(p, e)
        p.parametersPage.resultsTreeWidget.findItems.return_value = []
        p._notifications = notifications
        return p

    def test_successful_calculation_enables_save_button(self):
        """A successful calculation enables the Save button."""
        p = self._make_page()
        calculator = MagicMock()
        calculator.get_list.return_value = ["FeCoCrNi"]
        with (
            patch("HEACalculator.app.HEACalculator", return_value=calculator),
            patch("HEACalculator.app.QtWidgets.QTreeWidgetItem"),
        ):
            ParametersPage.calculate(p, "FeCoCrNi")
        p.parametersPage.SavePushButton.setEnabled.assert_called_once_with(True)

    def test_type_error_during_calculation_emits_error_notification(self):
        """A TypeError raised by HEACalculator is reported as an error notification."""
        p = self._make_page()
        with patch("HEACalculator.app.HEACalculator", side_effect=TypeError("bad type")):
            ParametersPage.calculate(p, "FeCoCrNi")
        assert p._notifications[0][1] == "error"

    def test_value_error_with_extra_letters_emits_parsed_error_notification(self):
        """A ValueError about extra letters maps to the formula-parsing prefix."""
        p = self._make_page()
        with patch("HEACalculator.app.HEACalculator", side_effect=ValueError("extra letters were detected")):
            ParametersPage.calculate(p, "FeCoCrNi")
        assert p._notifications[0][1] == "error"
        assert "could not be parsed" in p._notifications[0][0]


class TestBtnParametersClicked(TestCase):
    """Tests for HEACalculatorMainWindow.btn_parameters_clicked."""

    def _make_window(self):
        w = SimpleNamespace(
            BTN_BACKGROUND_COLOR_HIGHLIGHTED=HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_HIGHLIGHTED,
            BTN_BACKGROUND_COLOR_DEFAULT=HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_DEFAULT,
            ui=SimpleNamespace(
                stackedWidget=MagicMock(),
                btnParameters=MagicMock(),
                btnBatchAmount=MagicMock(),
                btnMDL=MagicMock(),
            ),
            parametersPage=MagicMock(),
        )
        return w

    def test_switches_stacked_widget_to_parameters_page(self):
        """Clicking Parameters navigates the stacked widget to the parameters page."""
        w = self._make_window()
        HEACalculatorMainWindow.btn_parameters_clicked(w)
        w.ui.stackedWidget.setCurrentWidget.assert_called_once_with(w.parametersPage)

    def test_sets_parameters_button_to_highlighted_style(self):
        """The Parameters button receives the highlighted stylesheet."""
        w = self._make_window()
        HEACalculatorMainWindow.btn_parameters_clicked(w)
        w.ui.btnParameters.setStyleSheet.assert_called_once_with(HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_HIGHLIGHTED)

    def test_sets_mdl_button_to_default_style(self):
        """The MDL button is reset to the default stylesheet."""
        w = self._make_window()
        HEACalculatorMainWindow.btn_parameters_clicked(w)
        w.ui.btnMDL.setStyleSheet.assert_called_once_with(HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_DEFAULT)


class TestMouseEvents(TestCase):
    """Tests for frameless-window drag-to-move mouse event handlers."""

    def test_mouse_press_records_global_position(self):
        """mousePressEvent stores the current global cursor position in oldPos."""
        w = SimpleNamespace(oldPos=None)
        event = MagicMock()
        event.globalPos.return_value = "pos_sentinel"
        HEACalculatorMainWindow.mousePressEvent(w, event)
        assert w.oldPos == "pos_sentinel"

    def test_mouse_move_moves_window_by_delta(self):
        """mouseMoveEvent moves the window by the delta between old and new positions."""
        mock_delta = MagicMock()
        mock_delta.x.return_value = 10
        mock_delta.y.return_value = -5

        new_pos = MagicMock()
        w = SimpleNamespace(oldPos=MagicMock())
        w.x = MagicMock(return_value=200)
        w.y = MagicMock(return_value=100)
        w.move = MagicMock()

        event = MagicMock()
        event.globalPos.return_value = new_pos

        with patch("HEACalculator.app.QtCore.QPoint", return_value=mock_delta):
            HEACalculatorMainWindow.mouseMoveEvent(w, event)

        w.move.assert_called_once_with(210, 95)

    def test_mouse_move_updates_old_pos_to_new_position(self):
        """mouseMoveEvent updates oldPos to the event's globalPos for the next drag step."""
        mock_delta = MagicMock()
        mock_delta.x.return_value = 0
        mock_delta.y.return_value = 0

        new_pos = object()
        w = SimpleNamespace(oldPos=MagicMock())
        w.x = MagicMock(return_value=0)
        w.y = MagicMock(return_value=0)
        w.move = MagicMock()

        event = MagicMock()
        event.globalPos.return_value = new_pos

        with patch("HEACalculator.app.QtCore.QPoint", return_value=mock_delta):
            HEACalculatorMainWindow.mouseMoveEvent(w, event)

        assert w.oldPos is new_pos


class TestNotificationBarSeverityStyles(TestCase):
    """Tests for warning and info notification color schemes."""

    def _make_bar(self):
        return SimpleNamespace(
            STYLES=NotificationBar.STYLES,
            AUTO_DISMISS_MS=NotificationBar.AUTO_DISMISS_MS,
            setStyleSheet=MagicMock(),
            messageLabel=MagicMock(),
            setVisible=MagicMock(),
            dismissTimer=MagicMock(),
        )

    def test_warning_severity_applies_warning_background_color(self):
        """The warning severity uses the #6C5B3B background color."""
        bar = self._make_bar()
        NotificationBar.show_message(bar, "Low sum.", "warning")
        style = bar.setStyleSheet.call_args.args[0]
        assert "#6C5B3B" in style

    def test_info_severity_applies_info_background_color(self):
        """The info severity uses the #3E5C76 background color."""
        bar = self._make_bar()
        NotificationBar.show_message(bar, "Done.", "info")
        style = bar.setStyleSheet.call_args.args[0]
        assert "#3E5C76" in style


class TestNotificationBarInit:
    """Tests for NotificationBar widget initialization."""

    def test_notification_bar_is_initially_hidden(self, qapp):
        """A freshly constructed NotificationBar is not visible."""
        bar = NotificationBar()
        assert not bar.isVisible()

    def test_dismiss_timer_is_single_shot(self, qapp):
        """The auto-dismiss timer fires only once per activation."""
        bar = NotificationBar()
        assert bar.dismissTimer.isSingleShot()

    def test_close_button_label_is_x(self, qapp):
        """The manual-dismiss button is labelled 'x'."""
        bar = NotificationBar()
        assert bar.closeButton.text() == "x"

    def test_message_label_supports_word_wrap(self, qapp):
        """The message label wraps long text rather than clipping it."""
        bar = NotificationBar()
        assert bar.messageLabel.wordWrap()


class TestItemDelegate:
    """Tests for ItemDelegate cell editor creation."""

    def test_create_editor_returns_line_edit(self, qapp):
        """createEditor returns a QLineEdit widget."""
        delegate = ItemDelegate()
        parent = QtWidgets.QWidget()
        editor = delegate.createEditor(parent, None, None)
        assert isinstance(editor, QtWidgets.QLineEdit)

    def test_create_editor_line_edit_has_double_validator(self, qapp):
        """The returned QLineEdit has a QDoubleValidator attached."""
        from PyQt5 import QtGui

        delegate = ItemDelegate()
        parent = QtWidgets.QWidget()
        editor = delegate.createEditor(parent, None, None)
        assert isinstance(editor.validator(), QtGui.QDoubleValidator)


class TestAlignDelegate:
    """Tests for AlignDelegate text alignment initialization."""

    def test_init_style_option_sets_align_center(self, qapp):
        """initStyleOption overrides the display alignment to AlignCenter."""
        delegate = AlignDelegate()
        option = QtWidgets.QStyleOptionViewItem()
        index = QtCore.QModelIndex()
        delegate.initStyleOption(option, index)
        assert option.displayAlignment == QtCore.Qt.AlignCenter
