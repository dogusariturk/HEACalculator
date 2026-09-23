"""Tests for the dismissible NotificationBar banner."""

import pytest
from PyQt6 import QtCore

from HEACalculator.app import NotificationBar

SEVERITIES = [
    ("error", "#6E4651"),
    ("warning", "#6C5B3B"),
    ("info", "#3E5C76"),
]


class TestNotificationBarConstruction:
    """Tests for the widgets NotificationBar builds in __init__."""

    def test_bar_starts_hidden(self, notification_bar):
        """A freshly constructed bar is not visible."""
        assert not notification_bar.isVisible()

    def test_dismiss_timer_is_single_shot(self, notification_bar):
        """The auto-dismiss timer fires once per message."""
        assert notification_bar.dismissTimer.isSingleShot()

    def test_dismiss_timer_starts_inactive(self, notification_bar):
        """No auto-dismiss is pending before a message is shown."""
        assert not notification_bar.dismissTimer.isActive()

    def test_close_button_is_labelled_x(self, notification_bar):
        """The dismiss affordance is a small 'x' button."""
        assert notification_bar.closeButton.text() == "x"

    def test_close_button_does_not_take_focus(self, notification_bar):
        """Dismissing the banner must not steal keyboard focus from the page."""
        assert notification_bar.closeButton.focusPolicy() == QtCore.Qt.FocusPolicy.NoFocus

    def test_message_label_wraps_long_text(self, notification_bar):
        """Long error messages wrap instead of clipping."""
        assert notification_bar.messageLabel.wordWrap()


class TestShowMessage:
    """Tests for NotificationBar.show_message."""

    @pytest.mark.parametrize("severity,background", SEVERITIES, ids=[severity for severity, _ in SEVERITIES])
    def test_severity_applies_its_background_color(self, notification_bar, severity, background):
        """Each severity paints the banner with its own background color."""
        notification_bar.show_message("Calculation failed.", severity)

        assert background in notification_bar.styleSheet()

    @pytest.mark.parametrize("severity,background", SEVERITIES, ids=[severity for severity, _ in SEVERITIES])
    def test_severity_applies_shared_foreground_color(self, notification_bar, severity, background):
        """Every severity uses the same light foreground color."""
        notification_bar.show_message("Calculation failed.", severity)

        assert NotificationBar.STYLES[severity]["foreground"] in notification_bar.styleSheet()

    def test_message_text_is_displayed(self, notification_bar):
        """The supplied message lands in the visible label."""
        notification_bar.show_message("Saved results to out.csv.", "info")

        assert notification_bar.messageLabel.text() == "Saved results to out.csv."

    def test_bar_becomes_visible(self, notification_bar):
        """Showing a message reveals the banner."""
        notification_bar.show_message("Saved results to out.csv.", "info")

        assert notification_bar.isVisible()

    def test_auto_dismiss_timer_is_started(self, notification_bar):
        """Showing a message schedules the auto-dismiss for the full interval.

        Qt coarse timers may round remainingTime() above the nominal interval, so
        the interval itself is the stable thing to assert on.
        """
        notification_bar.show_message("Saved results to out.csv.", "info")

        assert notification_bar.dismissTimer.isActive()
        assert notification_bar.dismissTimer.interval() == NotificationBar.AUTO_DISMISS_MS

    def test_unknown_severity_raises_value_error(self, notification_bar):
        """An unrecognized severity is a programming error, not a silent fallback."""
        with pytest.raises(ValueError, match="Unsupported notification severity: debug"):
            notification_bar.show_message("Saved results.", "debug")

    def test_unknown_severity_leaves_bar_hidden(self, notification_bar):
        """A rejected severity must not half-show the banner."""
        with pytest.raises(ValueError):
            notification_bar.show_message("Saved results.", "debug")

        assert not notification_bar.isVisible()

    def test_second_message_replaces_the_first(self, notification_bar):
        """Showing a new message overwrites the old text and styling."""
        notification_bar.show_message("Calculation failed.", "error")
        notification_bar.show_message("Saved results.", "info")

        assert notification_bar.messageLabel.text() == "Saved results."
        assert "#3E5C76" in notification_bar.styleSheet()
        assert "#6E4651" not in notification_bar.styleSheet()

    def test_second_message_restarts_the_countdown(self, qtbot, notification_bar):
        """A new message resets the dismissal countdown rather than letting it run out."""
        notification_bar.AUTO_DISMISS_MS = 300
        notification_bar.show_message("Calculation failed.", "error")
        qtbot.wait(200)

        notification_bar.show_message("Saved results.", "info")
        qtbot.wait(200)

        # 400 ms have elapsed since the first message; only a restart keeps it visible.
        assert notification_bar.isVisible()
        qtbot.waitUntil(lambda: not notification_bar.isVisible(), timeout=2000)


class TestHideMessage:
    """Tests for dismissing the banner."""

    def test_hide_message_hides_the_bar(self, notification_bar):
        """Calling hide_message conceals a visible banner."""
        notification_bar.show_message("Saved results.", "info")
        notification_bar.hide_message()

        assert not notification_bar.isVisible()

    def test_hide_message_stops_the_timer(self, notification_bar):
        """Dismissing cancels the pending auto-dismiss."""
        notification_bar.show_message("Saved results.", "info")
        notification_bar.hide_message()

        assert not notification_bar.dismissTimer.isActive()

    def test_close_button_click_dismisses_the_bar(self, qtbot, notification_bar):
        """The closeButton.clicked -> hide_message connection is wired up."""
        notification_bar.show_message("Saved results.", "info")

        qtbot.mouseClick(notification_bar.closeButton, QtCore.Qt.MouseButton.LeftButton)

        assert not notification_bar.isVisible()
        assert not notification_bar.dismissTimer.isActive()

    def test_timer_timeout_dismisses_the_bar(self, qtbot, notification_bar):
        """The dismissTimer.timeout -> hide_message connection auto-hides the banner."""
        notification_bar.show_message("Saved results.", "info")
        notification_bar.dismissTimer.stop()
        notification_bar.dismissTimer.start(20)

        qtbot.waitUntil(lambda: not notification_bar.isVisible(), timeout=2000)
