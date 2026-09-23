"""Tests for the frameless HEACalculatorMainWindow shell."""

import sys

import pytest
from conftest import select_elements
from PyQt6 import QtCore, QtGui, QtWidgets

from HEACalculator.app import BatchCalculationsPage, HEACalculatorMainWindow, NotificationBar, ParametersPage
from HEACalculator.core.hea import __version__

HIGHLIGHTED = HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_HIGHLIGHTED
DEFAULT = HEACalculatorMainWindow.BTN_BACKGROUND_COLOR_DEFAULT


def _mouse_event(event_type: QtCore.QEvent.Type, global_pos: QtCore.QPointF) -> QtGui.QMouseEvent:
    """Build a real QMouseEvent at a given global position.

    Args:
        event_type: MouseButtonPress or MouseMove.
        global_pos: Global cursor position for the event.

    Returns:
        A mouse event suitable for handing to the window's handlers.
    """
    return QtGui.QMouseEvent(
        event_type,
        QtCore.QPointF(0.0, 0.0),
        global_pos,
        QtCore.Qt.MouseButton.LeftButton,
        QtCore.Qt.MouseButton.LeftButton,
        QtCore.Qt.KeyboardModifier.NoModifier,
    )


class TestWindowComposition:
    """Tests for the widget tree assembled in __init__."""

    def test_window_title(self, main_window):
        """The window identifies the application and its lab."""
        assert main_window.windowTitle() == "HEACalculator | MDL"

    def test_window_is_frameless(self, main_window):
        """The OS title bar is replaced by the custom top bar."""
        assert main_window.windowFlags() & QtCore.Qt.WindowType.FramelessWindowHint

    def test_window_background_is_translucent(self, main_window):
        """Rounded corners need a translucent backing surface."""
        assert main_window.testAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

    def test_both_pages_are_stacked(self, main_window):
        """The stack holds exactly the parameters and batch pages."""
        assert main_window.ui.stackedWidget.count() == 2

    def test_parameters_page_is_first(self, main_window):
        """The calculation page is the landing screen."""
        assert main_window.ui.stackedWidget.widget(0) is main_window.parametersPage
        assert isinstance(main_window.parametersPage, ParametersPage)

    def test_batch_page_is_second(self, main_window):
        """The screener sits behind the calculation page."""
        assert main_window.ui.stackedWidget.widget(1) is main_window.batchCalculationsPage
        assert isinstance(main_window.batchCalculationsPage, BatchCalculationsPage)

    def test_notification_bar_sits_above_the_content(self, main_window):
        """The banner is inserted between the top bar and the pages."""
        assert isinstance(main_window.notificationBar, NotificationBar)
        assert main_window.ui.verticalLayout.indexOf(main_window.notificationBar) == 1

    def test_notification_bar_starts_hidden(self, main_window):
        """No banner is shown until something asks for one."""
        assert not main_window.notificationBar.isVisible()


class TestNavigation:
    """Tests for switching between the two pages."""

    def test_batch_button_shows_the_batch_page(self, qtbot, main_window):
        """Clicking Range Search brings the screener forward."""
        qtbot.mouseClick(main_window.ui.btnBatchAmount, QtCore.Qt.MouseButton.LeftButton)

        assert main_window.ui.stackedWidget.currentWidget() is main_window.batchCalculationsPage

    def test_parameters_button_shows_the_parameters_page(self, qtbot, main_window):
        """Clicking HEA Parameters brings the calculation page back."""
        qtbot.mouseClick(main_window.ui.btnBatchAmount, QtCore.Qt.MouseButton.LeftButton)
        qtbot.mouseClick(main_window.ui.btnParameters, QtCore.Qt.MouseButton.LeftButton)

        assert main_window.ui.stackedWidget.currentWidget() is main_window.parametersPage

    @pytest.mark.parametrize(
        "clicked,highlighted,dimmed",
        [
            ("btnParameters", "btnParameters", ["btnBatchAmount", "btnMDL"]),
            ("btnBatchAmount", "btnBatchAmount", ["btnParameters", "btnMDL"]),
        ],
        ids=["parameters", "batch"],
    )
    def test_navigation_highlights_only_the_active_button(self, qtbot, main_window, clicked, highlighted, dimmed):
        """The active page's nav button is the only highlighted one."""
        qtbot.mouseClick(getattr(main_window.ui, clicked), QtCore.Qt.MouseButton.LeftButton)

        assert getattr(main_window.ui, highlighted).styleSheet() == HIGHLIGHTED
        assert all(getattr(main_window.ui, name).styleSheet() == DEFAULT for name in dimmed)

    def test_close_button_is_connected(self, qtbot, main_window):
        """The custom close button really closes the window."""
        main_window.show()

        qtbot.mouseClick(main_window.ui.btnClose, QtCore.Qt.MouseButton.LeftButton)

        assert not main_window.isVisible()


class TestNotificationRouting:
    """Tests for the page -> window -> banner notification path."""

    @pytest.mark.parametrize("page_attr", ["parametersPage", "batchCalculationsPage"], ids=["parameters", "batch"])
    def test_page_notifications_reach_the_banner(self, main_window, page_attr):
        """Each page's notificationRequested signal is connected to the window."""
        main_window.show()

        getattr(main_window, page_attr).notificationRequested.emit("Saved results.", "info")

        assert main_window.notificationBar.messageLabel.text() == "Saved results."
        assert main_window.notificationBar.isVisible()

    def test_severity_is_forwarded(self, main_window):
        """The banner is styled with the severity the page asked for."""
        main_window.parametersPage.notificationRequested.emit("Calculation failed.", "error")

        assert "#6E4651" in main_window.notificationBar.styleSheet()

    def test_show_notification_rejects_unknown_severity(self, main_window):
        """An invalid severity surfaces as an error rather than being swallowed."""
        with pytest.raises(ValueError):
            main_window.show_notification("Saved results.", "debug")


class TestEndToEnd:
    """Tests that exercise a full user journey through the assembled window."""

    def test_calculating_from_the_window_updates_tree_and_banner(self, qtbot, main_window):
        """Selecting elements and calculating shows a result row and a confirmation."""
        main_window.show()
        page = main_window.parametersPage
        select_elements(qtbot, page, "Fe", "Co", "Cr", "Ni")

        qtbot.mouseClick(page.parametersPage.CalculatePushButton, QtCore.Qt.MouseButton.LeftButton)

        assert page.parametersPage.resultsTreeWidget.topLevelItemCount() == 1
        assert main_window.notificationBar.isVisible()
        assert "calculation completed." in main_window.notificationBar.messageLabel.text()

    def test_failed_calculation_shows_an_error_banner(self, qtbot, main_window):
        """A validation failure is surfaced in the shared banner."""
        page = main_window.parametersPage
        select_elements(qtbot, page, "Fe", "Co")
        page.parametersPage.tableWidget.item(0, 1).setText("10")

        qtbot.mouseClick(page.parametersPage.CalculatePushButton, QtCore.Qt.MouseButton.LeftButton)

        assert "expected 100%" in main_window.notificationBar.messageLabel.text()

    def test_batch_validation_shows_a_banner(self, qtbot, main_window):
        """The batch page routes its warnings through the same banner."""
        qtbot.mouseClick(main_window.ui.btnBatchAmount, QtCore.Qt.MouseButton.LeftButton)

        qtbot.mouseClick(main_window.batchCalculationsPage.ui.btnSearch, QtCore.Qt.MouseButton.LeftButton)

        assert main_window.notificationBar.messageLabel.text().startswith("Select at least two elements")


class TestHelpAbout:
    """Tests for the About dialog."""

    def test_about_dialog_reports_the_version(self, monkeypatch):
        """The About box shows the installed package version."""
        captured: list[QtWidgets.QMessageBox] = []

        def _capture(box: QtWidgets.QMessageBox) -> int:
            captured.append(box)
            return 0

        monkeypatch.setattr(QtWidgets.QMessageBox, "exec", _capture, raising=True)
        HEACalculatorMainWindow.helpAbout()

        assert __version__ in captured[0].text()

    def test_about_dialog_shows_the_copyright(self, monkeypatch):
        """The About box carries the project's copyright notice."""
        captured: list[QtWidgets.QMessageBox] = []
        monkeypatch.setattr(QtWidgets.QMessageBox, "exec", lambda box: captured.append(box) or 0)

        HEACalculatorMainWindow.helpAbout()

        assert "Copyright" in captured[0].text()

    @pytest.mark.skipif(sys.platform == "darwin", reason="macOS ignores QMessageBox window titles by design")
    def test_about_dialog_title(self, monkeypatch):
        """The About box is titled for the application and its lab."""
        captured: list[QtWidgets.QMessageBox] = []
        monkeypatch.setattr(QtWidgets.QMessageBox, "exec", lambda box: captured.append(box) or 0)

        HEACalculatorMainWindow.helpAbout()

        assert captured[0].windowTitle() == "About | HEA Calculator | MDL"

    def test_mdl_button_opens_the_about_dialog(self, qtbot, main_window, monkeypatch):
        """The MDL nav button is wired to helpAbout."""
        calls: list[int] = []
        monkeypatch.setattr(QtWidgets.QMessageBox, "exec", lambda box: calls.append(1) or 0)

        qtbot.mouseClick(main_window.ui.btnMDL, QtCore.Qt.MouseButton.LeftButton)

        assert calls == [1]


class TestFramelessDragging:
    """Tests for the custom drag-to-move behavior."""

    def test_press_records_the_cursor_position(self, main_window):
        """A press seeds the drag origin from the global cursor position."""
        main_window.mousePressEvent(_mouse_event(QtCore.QEvent.Type.MouseButtonPress, QtCore.QPointF(300.0, 400.0)))

        assert main_window.oldPos == QtCore.QPoint(300, 400)

    def test_move_translates_the_window_by_the_delta(self, main_window):
        """Dragging shifts the window by the cursor delta."""
        main_window.move(100, 100)
        main_window.mousePressEvent(_mouse_event(QtCore.QEvent.Type.MouseButtonPress, QtCore.QPointF(300.0, 400.0)))

        main_window.mouseMoveEvent(_mouse_event(QtCore.QEvent.Type.MouseMove, QtCore.QPointF(310.0, 420.0)))

        assert main_window.pos() == QtCore.QPoint(110, 120)

    def test_move_updates_the_drag_origin(self, main_window):
        """Successive moves are relative to the previous position, not the press."""
        main_window.mousePressEvent(_mouse_event(QtCore.QEvent.Type.MouseButtonPress, QtCore.QPointF(300.0, 400.0)))

        main_window.mouseMoveEvent(_mouse_event(QtCore.QEvent.Type.MouseMove, QtCore.QPointF(310.0, 420.0)))

        assert main_window.oldPos == QtCore.QPoint(310, 420)

    def test_consecutive_moves_accumulate(self, main_window):
        """A multi-step drag moves the window by the total delta."""
        main_window.move(0, 0)
        main_window.mousePressEvent(_mouse_event(QtCore.QEvent.Type.MouseButtonPress, QtCore.QPointF(0.0, 0.0)))

        main_window.mouseMoveEvent(_mouse_event(QtCore.QEvent.Type.MouseMove, QtCore.QPointF(10.0, 10.0)))
        main_window.mouseMoveEvent(_mouse_event(QtCore.QEvent.Type.MouseMove, QtCore.QPointF(25.0, 30.0)))

        assert main_window.pos() == QtCore.QPoint(25, 30)


class TestStyleConstants:
    """Tests for the navigation button color constants."""

    def test_highlighted_uses_the_accent_color(self):
        """The active nav button uses the accent background."""
        assert "#3E5C76" in HIGHLIGHTED

    def test_default_uses_the_panel_color(self):
        """Inactive nav buttons blend into the side panel."""
        assert "#1D2D44" in DEFAULT

    def test_the_two_styles_differ(self):
        """The active button must be visually distinguishable."""
        assert HIGHLIGHTED != DEFAULT
