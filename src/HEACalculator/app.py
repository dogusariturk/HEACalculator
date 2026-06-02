"""PyQt6 GUI application for HEACalculator.

Defines the main window, parameters page, and notification bar widgets used
when the application is launched in GUI mode.
"""

import csv
import html
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import Any

try:
    from PyQt6 import QtCore, QtGui, QtWidgets
    from PyQt6.QtWidgets import QMessageBox
except ImportError:
    raise SystemExit(
        'PyQt6 is required for GUI mode. Install with: uv add "HEACalculator[gui]" or pip install "HEACalculator[gui]"'
    ) from None

from HEACalculator.utils import find_all_comps
from HEACalculator.core.hea import HEACalculator, __version__
from HEACalculator.exceptions import ElementNotFoundError, MissingFormationEnthalpyError, MissingMixingEnthalpyError
from HEACalculator.gui.HEACalculatorMain import Ui_HEACalculator
from HEACalculator.gui.batchCalculationsPage import Ui_BatchCalculationsPage
from HEACalculator.gui.parametersPage import Ui_ParametersPage


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    """Item delegate that centers text in table/tree view cells."""

    def initStyleOption(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        """Set display alignment to center before the option is used for painting."""
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class ItemDelegate(QtWidgets.QStyledItemDelegate):
    """Item delegate that restricts table cell editing to doubles in [0.0, 100.0] with 3 decimal places."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the delegate and force the C locale for decimal parsing."""
        super().__init__(*args, **kwargs)
        QtCore.QLocale.setDefault(QtCore.QLocale(QtCore.QLocale.Language.C))

    def createEditor(
        self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex
    ) -> QtWidgets.QWidget:
        """Return a QLineEdit that only accepts doubles in the range [0.0, 100.0].

        Returns:
            Configured line edit used for in-place table editing.
        """
        lineEdt = QtWidgets.QLineEdit(parent)
        lineEdt.setValidator(QtGui.QDoubleValidator(0.0, 100.0, 3))
        return lineEdt


class BatchAmountDelegate(QtWidgets.QStyledItemDelegate):
    """Item delegate that restricts converter input table to positive doubles with extended range."""

    def createEditor(
        self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex
    ) -> QtWidgets.QWidget:
        """Return a QLineEdit that only accepts doubles in the range (0, 999999].

        Returns:
            Configured line edit used for batch amount editing.
        """
        editor = QtWidgets.QLineEdit(parent)
        editor.setValidator(QtGui.QDoubleValidator(0.0001, 999999.0, 4))
        return editor


def configure_results_tree_header(tree_widget: QtWidgets.QTreeWidget) -> None:
    """Apply consistent initial column sizing to a results tree widget."""
    header = tree_widget.header()
    default_width = header.defaultSectionSize()
    header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
    header.setStretchLastSection(False)
    header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeMode.Interactive)
    header.resizeSection(7, default_width)


class NotificationBar(QtWidgets.QFrame):
    """Dismissible notification banner displayed above page content.

    Supports three severity levels (error, warning, info) with distinct color
    schemes and auto-dismisses after AUTO_DISMISS_MS milliseconds.
    """

    AUTO_DISMISS_MS = 5000
    STYLES = {
        "error": {
            "background": "#6E4651",
            "foreground": "#F0EBD8",
        },
        "warning": {
            "background": "#6C5B3B",
            "foreground": "#F0EBD8",
        },
        "info": {
            "background": "#3E5C76",
            "foreground": "#F0EBD8",
        },
    }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Create the notification bar widgets and configure auto-dismiss behavior."""
        super().__init__(*args, **kwargs)

        self.setVisible(False)
        self.dismissTimer = QtCore.QTimer(self)
        self.dismissTimer.setSingleShot(True)
        self.dismissTimer.timeout.connect(self.hide_message)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(16, 8, 8, 8)
        layout.setSpacing(8)

        self.messageLabel = QtWidgets.QLabel(self)
        self.messageLabel.setWordWrap(True)

        self.closeButton = QtWidgets.QPushButton("x", self)
        self.closeButton.setFixedSize(24, 24)
        self.closeButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.closeButton.clicked.connect(self.hide_message)

        layout.addWidget(self.messageLabel, 1)
        layout.addWidget(self.closeButton, 0, QtCore.Qt.AlignmentFlag.AlignTop)

    def hide_message(self) -> None:
        """Stop the auto-dismiss timer and hide the notification bar."""
        self.dismissTimer.stop()
        self.setVisible(False)

    def show_message(self, message: str, severity: str) -> None:
        """Display a styled notification message and start the auto-dismiss timer.

        Args:
            message: Text to display in the notification bar.
            severity: One of "error", "warning", or "info".

        Raises:
            ValueError: If severity is not a recognized key in STYLES.
        """
        if severity not in self.STYLES:
            raise ValueError(f"Unsupported notification severity: {severity}")

        colors = self.STYLES[severity]
        self.setStyleSheet(
            f"""
            QFrame {{
                background-color: {colors["background"]};
                border: none;
            }}
            QLabel {{
                color: {colors["foreground"]};
                font-weight: bold;
            }}
            QPushButton {{
                background: transparent;
                border: none;
                color: {colors["foreground"]};
                font-weight: bold;
            }}
            QPushButton:hover {{
                background: rgba(13, 19, 33, 40);
            }}
            """
        )
        self.messageLabel.setText(message)
        self.setVisible(True)
        self.dismissTimer.start(self.AUTO_DISMISS_MS)


_MSGBOX_STYLESHEET = """
QMessageBox {
    background-color: #0D1321;
}
QMessageBox QLabel {
    color: #F0EBD8;
    font-size: 13px;
}
QMessageBox QPushButton {
    background-color: #1D2D44;
    color: #F0EBD8;
    border: none;
    padding: 6px 20px;
    min-width: 60px;
}
QMessageBox QPushButton:hover {
    background-color: #3E5C76;
}
QMessageBox QPushButton:pressed {
    background-color: #748CAB;
}
"""


class RangeSearchWorker(QtCore.QThread):
    """Background worker that parallelizes range search calculations.

    Runs HEACalculator on a list of alloy formula strings using a
    ProcessPoolExecutor, emitting results back to the main thread via signals
    so that Qt widgets are only ever touched from the main thread.

    Args:
        alloys: List of alloy formula strings to calculate.
    """

    result_ready = QtCore.pyqtSignal(list)
    finished_with_count = QtCore.pyqtSignal(int)

    def __init__(self, alloys: list[str], parent: QtCore.QObject | None = None) -> None:
        """Store the alloy list for use in ``run``."""
        super().__init__(parent)
        self._alloys = alloys

    def run(self) -> None:
        """Calculate all alloys in parallel and emit results to the main thread."""
        from HEACalculator.utils import _range_worker

        workers = min(os.cpu_count() or 1, len(self._alloys))
        chunksize = max(1, len(self._alloys) // (workers * 4))
        count = 0
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for result, _err in executor.map(_range_worker, self._alloys, chunksize=chunksize):
                if result is not None:
                    self.result_ready.emit(result)
                    count += 1
        self.finished_with_count.emit(count)


class BatchCalculationsPage(QtWidgets.QWidget):
    """Batch composition screener page.

    Lets users specify elements and a composition range, then screens all
    valid compositions that sum to 100% and displays their HEA parameters.
    Equivalent to the CLI ``range`` command.
    """

    notificationRequested = QtCore.pyqtSignal(str, str)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the batch page UI, element button wiring, and range controls."""
        super().__init__(*args, **kwargs)
        self.ui = Ui_BatchCalculationsPage()
        self.ui.setupUi(self)
        self.selectedElements: list[str] = []
        self._search_worker: RangeSearchWorker | None = None
        configure_results_tree_header(self.ui.resultsTreeWidget)

        self._element_buttons = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("ebtn")]
        for btn in self._element_buttons:
            btn.clicked.connect(partial(self._handle_element_clicked, btn.text()))

        self.ui.btnSearch.clicked.connect(self._handle_search)
        self.ui.btnClear.clicked.connect(self._handle_clear)
        self.ui.btnSave.clicked.connect(self._handle_save)

        _spinbox_palette = QtGui.QPalette()
        _spinbox_palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor("#1D2D44"))
        _spinbox_palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor("#F0EBD8"))
        _spinbox_palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor("#3E5C76"))
        _spinbox_palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor("#F0EBD8"))
        _spinbox_palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#1D2D44"))
        _fusion = QtWidgets.QStyleFactory.create("Fusion")
        for sb in (self.ui.startSpinBox, self.ui.endSpinBox, self.ui.stepSpinBox):
            sb.setStyle(_fusion)
            sb.setPalette(_spinbox_palette)
            sb.setStyleSheet("")

    def _handle_element_clicked(self, symbol: str, checked: bool) -> None:
        """Add or remove an element from the selected list when its button is toggled."""
        if checked and symbol not in self.selectedElements:
            self.selectedElements.append(symbol)
        elif not checked and symbol in self.selectedElements:
            self.selectedElements.remove(symbol)

    def _handle_search(self) -> None:
        """Validate inputs, enumerate compositions, and launch a parallel background search."""
        if len(self.selectedElements) < 2:
            self.notificationRequested.emit("Select at least two elements using the periodic table.", "warning")
            return

        start = self.ui.startSpinBox.value()
        end = self.ui.endSpinBox.value()
        step = self.ui.stepSpinBox.value()

        if start > end:
            self.notificationRequested.emit("Start % must not exceed End %.", "error")
            return

        elements_formula = "".join(self.selectedElements)

        try:
            formula, composition_set = find_all_comps(elements_formula, start, end, step)
        except Exception as error:
            self.notificationRequested.emit(f"Could not enumerate compositions. {error}", "error")
            return

        if not composition_set:
            self.notificationRequested.emit("No valid compositions found for the given range.", "warning")
            return

        alloys = [
            "".join(f"{k}{v}" for k, v in {**formula, **dict(zip(formula.keys(), composition, strict=False))}.items() if v != 0)
            for composition in composition_set
        ]

        self.ui.resultsTreeWidget.clear()
        self.ui.btnSearch.setEnabled(False)
        self.notificationRequested.emit(f"Searching {len(alloys)} compositions...", "info")

        self._search_worker = RangeSearchWorker(alloys, parent=self)
        self._search_worker.result_ready.connect(self._on_result_ready)
        self._search_worker.finished_with_count.connect(self._on_search_finished)
        self._search_worker.finished.connect(self._search_worker.deleteLater)
        self._search_worker.start()

    def _on_result_ready(self, result: list) -> None:
        """Add a single calculation result as a row in the results tree."""
        QtWidgets.QTreeWidgetItem(self.ui.resultsTreeWidget, result)

    def _on_search_finished(self, count: int) -> None:
        """Re-enable the Search button and report the final result count."""
        self.ui.btnSearch.setEnabled(True)
        if count == 0:
            self.notificationRequested.emit("No compositions could be calculated (missing database entries).", "warning")
            return
        self.ui.btnSave.setEnabled(True)
        self.notificationRequested.emit(f"Search completed. {count} compositions calculated.", "info")

    def _handle_clear(self) -> None:
        """Clear element selection and results, prompting for confirmation when results exist."""
        has_results = self.ui.resultsTreeWidget.topLevelItemCount() > 0
        has_selection = bool(self.selectedElements)
        if has_results or has_selection:
            box = QtWidgets.QMessageBox(self)
            box.setWindowFlags(box.windowFlags() | QtCore.Qt.WindowType.FramelessWindowHint)
            box.setWindowTitle("Clear")
            box.setText("This will clear all element selections and results. Continue?")
            box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            box.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
            box.setStyleSheet(_MSGBOX_STYLESHEET)
            if box.exec() != QtWidgets.QMessageBox.StandardButton.Yes:
                return
        self.ui.resultsTreeWidget.clear()
        self.selectedElements.clear()
        for btn in self._element_buttons:
            btn.setChecked(False)
        self.ui.btnSave.setEnabled(False)

    def _handle_save(self) -> None:
        """Export the results tree to a CSV file chosen via a save dialog."""
        if self.ui.resultsTreeWidget.topLevelItemCount() == 0:
            self.notificationRequested.emit("No results to save.", "warning")
            return
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self, "Save CSV", os.getenv("HOME"), "CSV(*.csv)")
        if ok and path:
            columns = range(self.ui.resultsTreeWidget.columnCount())
            try:
                with open(path, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(HEACalculator.get_headers())
                    for row in range(self.ui.resultsTreeWidget.topLevelItemCount()):
                        writer.writerow(self.ui.resultsTreeWidget.topLevelItem(row).text(c) for c in columns)
            except OSError as error:
                self.notificationRequested.emit(f"Could not save the results file. {error.args[0]}", "error")
                return
            self.notificationRequested.emit(f"Saved results to {os.path.basename(path)}.", "info")


class ParametersPage(QtWidgets.QWidget):
    """Main calculation page widget.

    Manages the periodic-table element selector, composition table, results
    tree, and save functionality. Emits notificationRequested(message, severity)
    to delegate notification display to the parent window.
    """

    notificationRequested = QtCore.pyqtSignal(str, str)

    _ERROR_PREFIXES = {
        "formation enthalpy database": (
            "Calculation failed because formation enthalpy data is missing for one or more selected element pairs."
        ),
        "mixing enthalpy database": (
            "Calculation failed because mixing enthalpy data is missing for one or more selected element pairs."
        ),
        "elements database": ("Calculation failed because one or more selected elements are not available in the database."),
        "extra letters were detected": (
            "Calculation failed because the selected composition could not be parsed as a valid formula."
        ),
    }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the parameters page UI, delegates, and button wiring."""
        super().__init__(*args, **kwargs)

        self.parametersPage = Ui_ParametersPage()
        self.parametersPage.setupUi(self)

        self.selectedElements = {}

        configure_results_tree_header(self.parametersPage.resultsTreeWidget)

        itemDelegate = ItemDelegate(self.parametersPage.tableWidget)
        self.parametersPage.tableWidget.setItemDelegate(itemDelegate)

        self.totalLabel = QtWidgets.QLabel(self)
        self.totalLabel.setGeometry(QtCore.QRect(570, 182, 410, 13))
        self.totalLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.totalLabel.setStyleSheet("color: #748CAB; font-size: 10px;")

        self._element_buttons = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("ebtn")]
        for btn in self._element_buttons:
            btn.clicked.connect(partial(self.handleElementClicked, btn.text()))
        self.parametersPage.tableWidget.cellChanged.connect(self.handleAmountChanged)
        self._update_action_buttons()
        self.parametersPage.ClearAllPushButton.pressed.connect(self.handleClearAllButton)
        self.parametersPage.CalculatePushButton.pressed.connect(self.handleCalculateButton)
        self.parametersPage.SavePushButton.clicked.connect(self.handleSaveButton)

    @staticmethod
    def _clean_error_message(error: Exception) -> str:
        """Return the first string argument of an exception, or its str() representation.

        Returns:
            User-facing error detail extracted from the exception.
        """
        if error.args and isinstance(error.args[0], str):
            return error.args[0]
        return str(error)

    @staticmethod
    def _format_formula_for_notification(formula: str) -> str:
        """HTML-escape a formula string and wrap numeric parts in <sub> tags.

        Returns:
            HTML-safe formula string with numeric parts rendered as subscripts.
        """
        escaped_formula = html.escape(formula)
        return re.sub(r"(\d+(?:\.\d+)?)", r"<sub>\1</sub>", escaped_formula)

    def _show_notification(self, message: str, severity: str) -> None:
        """Emit notificationRequested so the parent window can display the message."""
        self.notificationRequested.emit(message, severity)

    def _format_calculation_error(self, error: Exception) -> str:
        """Return a user-friendly error message for a failed HEA calculation.

        Returns:
            User-facing explanation of the calculation failure.
        """
        detail = self._clean_error_message(error)
        for keyword, prefix in self._ERROR_PREFIXES.items():
            if keyword in detail:
                return f"{prefix} {detail}"
        return f"Calculation failed. {detail}"

    def _format_save_error(self, error: Exception) -> str:
        """Return a user-friendly error message for a failed CSV save operation.

        Returns:
            User-facing explanation of the save failure.
        """
        return f"Could not save the results file. {self._clean_error_message(error)}"

    def _update_total_label(self) -> None:
        """Update the running total label with the current sum of element percentages."""
        if not self.selectedElements:
            self.totalLabel.setText("")
            return
        total = sum(self.selectedElements.values())
        near_100 = abs(total - 100.0) <= 0.01
        color = "#7FB685" if near_100 else "#C94040"
        self.totalLabel.setStyleSheet(f"color: {color}; font-size: 10px;")
        self.totalLabel.setText(f"Total: {total:.2f}%")

    def _update_action_buttons(self) -> None:
        """Enable or disable action buttons based on current selection and result state."""
        has_elements = bool(self.selectedElements)
        has_results = self.parametersPage.resultsTreeWidget.topLevelItemCount() > 0
        self.parametersPage.ClearAllPushButton.setEnabled(has_elements)
        self.parametersPage.CalculatePushButton.setEnabled(has_elements)
        self.parametersPage.SavePushButton.setEnabled(has_results)

    def calculate(self, formula: str) -> None:
        """Run HEACalculator for the given formula and append the result row to the tree.

        Shows a warning notification if the formula has already been calculated, or
        an error notification if the calculation raises a known exception.

        Args:
            formula: Alloy formula string (e.g. "FeCoCrNi").
        """
        if self.parametersPage.resultsTreeWidget.findItems(formula, QtCore.Qt.MatchFlag.MatchExactly):
            self._show_notification(
                f"{self._format_formula_for_notification(formula)} has already been calculated.",
                "warning",
            )
            return

        try:
            res = HEACalculator(formula)
            resList = res.get_list()
        except (KeyError, TypeError, ValueError) as error:
            self._show_notification(self._format_calculation_error(error), "error")
            return

        QtWidgets.QTreeWidgetItem(self.parametersPage.resultsTreeWidget, resList)
        self.parametersPage.SavePushButton.setEnabled(True)
        self._show_notification(
            f"{self._format_formula_for_notification(formula)} calculation completed.",
            "info",
        )

    def handleCalculateButton(self) -> None:
        """Validate that element percentages sum to 100 % then trigger calculation."""
        total = sum(self.selectedElements.values())
        if abs(total - 100.0) > 0.01:
            self._show_notification(
                f"Element percentages sum to {total:.2f}% (expected 100%). Adjust before calculating.",
                "warning",
            )
            return
        formula = "".join([f"{k}{v:g}" for k, v in dict(sorted(self.selectedElements.items())).items()])
        self.calculate(formula)

    def handleClearAllButton(self) -> None:
        """Clear the element table and results tree, prompting for confirmation when results exist."""
        if self.parametersPage.resultsTreeWidget.topLevelItemCount() > 0:
            box = QMessageBox(self)
            box.setWindowFlags(box.windowFlags() | QtCore.Qt.WindowType.FramelessWindowHint)
            box.setWindowTitle("Clear All")
            box.setText("This will also clear all calculated results. Continue?")
            box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            box.setDefaultButton(QMessageBox.StandardButton.No)
            box.setStyleSheet(
                """
                QMessageBox {
                    background-color: #0D1321;
                }
                QMessageBox QLabel {
                    color: #F0EBD8;
                    font-size: 13px;
                }
                QMessageBox QPushButton {
                    background-color: #1D2D44;
                    color: #F0EBD8;
                    border: none;
                    padding: 6px 20px;
                    min-width: 60px;
                }
                QMessageBox QPushButton:hover {
                    background-color: #3E5C76;
                }
                QMessageBox QPushButton:pressed {
                    background-color: #748CAB;
                }
                """
            )
            if box.exec() != QMessageBox.StandardButton.Yes:
                return
        self.parametersPage.tableWidget.setRowCount(0)
        self.parametersPage.resultsTreeWidget.clear()
        self.selectedElements.clear()
        for btn in self._element_buttons:
            btn.setChecked(False)
        self._update_action_buttons()
        self._update_total_label()

    def handleSaveButton(self) -> None:
        """Export the results tree to a CSV file chosen via a save dialog."""
        if self.parametersPage.resultsTreeWidget.topLevelItemCount() == 0:
            self._show_notification("There are no calculated results to save.", "warning")
            return

        path, ok = QtWidgets.QFileDialog.getSaveFileName(self, "Save CSV", os.getenv("HOME"), "CSV(*.csv)")
        if ok and path:
            columns = range(self.parametersPage.resultsTreeWidget.columnCount())
            try:
                with open(path, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(HEACalculator.get_headers())
                    for row in range(self.parametersPage.resultsTreeWidget.topLevelItemCount()):
                        writer.writerow(
                            self.parametersPage.resultsTreeWidget.topLevelItem(row).text(column) for column in columns
                        )
            except OSError as error:
                self._show_notification(self._format_save_error(error), "error")
                return

            self._show_notification(f"Saved results to {os.path.basename(path)}.", "info")

    def handleElementClicked(self, symbol: str, checked: bool) -> None:
        """Add or remove an element from the composition table when its button is toggled.

        Redistributes percentages equally across all currently selected elements.

        Args:
            symbol: Chemical symbol of the toggled element (e.g. "Fe").
            checked: True if the button was checked (element added), False if unchecked.
        """
        currentRowCount = self.parametersPage.tableWidget.rowCount()

        if checked and (symbol not in self.selectedElements):
            percentage = 100 / (len(self.selectedElements) + 1)
            self.selectedElements = {k: percentage for k, v in self.selectedElements.items()}
            self.selectedElements.update({symbol: float(percentage)})
            self.parametersPage.tableWidget.insertRow(currentRowCount)
            elmItem = QtWidgets.QTableWidgetItem(symbol)
            elmItem.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
            elmItem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.parametersPage.tableWidget.setItem(currentRowCount, 0, elmItem)
            amount = f"{percentage:.2f}"
            amountItem = QtWidgets.QTableWidgetItem(amount)
            amountItem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.parametersPage.tableWidget.setItem(currentRowCount, 1, amountItem)
            self.parametersPage.tableWidget.blockSignals(True)
            for row in range(self.parametersPage.tableWidget.rowCount()):
                self.parametersPage.tableWidget.item(row, 1).setText(amount)
            self.parametersPage.tableWidget.blockSignals(False)
            self._update_action_buttons()
            self._update_total_label()
        elif not checked and symbol in self.selectedElements:
            item = self.parametersPage.tableWidget.findItems(symbol, QtCore.Qt.MatchFlag.MatchExactly)
            for it in item:
                self.parametersPage.tableWidget.removeRow(it.row())
            del self.selectedElements[symbol]
            percentage = 100 / (len(self.selectedElements)) if len(self.selectedElements) != 0 else 100
            self.selectedElements = {k: float(percentage) for k, v in self.selectedElements.items()}
            amount = f"{percentage:.2f}"
            self.parametersPage.tableWidget.blockSignals(True)
            for row in range(self.parametersPage.tableWidget.rowCount()):
                self.parametersPage.tableWidget.item(row, 1).setText(amount)
            self.parametersPage.tableWidget.blockSignals(False)
            self._update_action_buttons()
            self._update_total_label()

    def handleAmountChanged(self, row: int, column: int) -> None:
        """Sync a manually edited percentage value back into selectedElements.

        Args:
            row: Table row index of the changed cell.
            column: Table column index; only column 1 (amount) is processed.
        """
        if column == 1:
            element = self.parametersPage.tableWidget.item(row, 0).text()
            amount = self.parametersPage.tableWidget.item(row, 1).text()
            if element in self.selectedElements and amount:
                if float(amount) == 0:
                    self.parametersPage.tableWidget.blockSignals(True)
                    self.parametersPage.tableWidget.item(row, 1).setText(f"{self.selectedElements[element]:.2f}")
                    self.parametersPage.tableWidget.blockSignals(False)
                    self._show_notification("Atomic percentage cannot be 0%.", "warning")
                else:
                    self.selectedElements.update({element: float(amount)})
                    self._update_total_label()


class HEACalculatorMainWindow(QtWidgets.QMainWindow):
    """Frameless main application window.

    Composes a NotificationBar and ParametersPage inside a stacked widget,
    and provides custom drag-to-move behavior since the OS title bar is hidden.
    """

    BTN_BACKGROUND_COLOR_HIGHLIGHTED = """QPushButton{background-color: #3E5C76}
                                          QPushButton:hover{background-color: #3E5C76}
                                          QPushButton:pressed{background-color: #748CAB;}"""

    BTN_BACKGROUND_COLOR_DEFAULT = """QPushButton{background-color: #1D2D44}
                                      QPushButton:hover{background-color: #3E5C76}
                                      QPushButton:pressed{background-color: #748CAB;}"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Create the main window, initialize child pages, and connect navigation controls."""
        super().__init__(*args, **kwargs)

        self.ui = Ui_HEACalculator()
        self.ui.setupUi(self)

        self.setWindowTitle("HEACalculator | MDL")

        self.oldPos = self.pos()

        self.parametersPage = ParametersPage()
        self.batchCalculationsPage = BatchCalculationsPage()
        self.notificationBar = NotificationBar()

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.verticalLayout.insertWidget(1, self.notificationBar)
        self.ui.stackedWidget.addWidget(self.parametersPage)
        self.ui.stackedWidget.addWidget(self.batchCalculationsPage)

        self.ui.btnParameters.setStyleSheet("QPushButton{background-color: #3E5C76}")

        self.ui.btnParameters.clicked.connect(self.btn_parameters_clicked)
        self.ui.btnBatchAmount.clicked.connect(self.btn_batch_amount_clicked)
        self.ui.btnMDL.clicked.connect(self.helpAbout)
        self.ui.btnClose.clicked.connect(self.close)
        self.parametersPage.notificationRequested.connect(self.show_notification)
        self.batchCalculationsPage.notificationRequested.connect(self.show_notification)

    def btn_parameters_clicked(self) -> None:
        """Switch the stacked widget to the parameters page and update button styles."""
        self.ui.stackedWidget.setCurrentWidget(self.parametersPage)
        self.ui.btnParameters.setStyleSheet(self.BTN_BACKGROUND_COLOR_HIGHLIGHTED)
        self.ui.btnBatchAmount.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnMDL.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)

    def btn_batch_amount_clicked(self) -> None:
        """Switch the stacked widget to the batch calculations page and update button styles."""
        self.ui.stackedWidget.setCurrentWidget(self.batchCalculationsPage)
        self.ui.btnParameters.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnBatchAmount.setStyleSheet(self.BTN_BACKGROUND_COLOR_HIGHLIGHTED)
        self.ui.btnMDL.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)

    def show_notification(self, message: str, severity: str) -> None:
        """Forward a notification request from a child widget to the notification bar."""
        self.notificationBar.show_message(message, severity)

    @staticmethod
    def helpAbout() -> None:
        """Display a modal About dialog with version and copyright information."""
        about_text = """<b>HEA Calculator v{}
    <p>Copyright &copy; 2022 MDL (METU).
    <p>This application enables the calculation and analysis of
     thermodynamic parameters in high-entropy alloys."""

        about_box = QMessageBox()
        about_box.setIconPixmap(QtGui.QPixmap(":/img/images/ic1.png"))
        about_box.setText(about_text.format(__version__))
        about_box.setWindowTitle("About | HEA Calculator | MDL")
        about_box.exec()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Record the cursor position to support frameless window dragging."""
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """Move the window by the delta since the last recorded mouse position."""
        new_pos = event.globalPosition().toPoint()
        delta = QtCore.QPoint(new_pos - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = new_pos


def run() -> None:
    """Create the QApplication, center the main window on screen, and start the event loop."""
    application = QtWidgets.QApplication(sys.argv)
    application.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/images/icon.ico")))
    window = HEACalculatorMainWindow()
    screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
    width = (screen.width() - window.width()) / 2
    height = (screen.height() - window.height()) / 2
    window.show()
    window.move(int(width), int(height))
    sys.exit(application.exec())


if __name__ == "__main__":
    run()
