"""Tests for the GUI entry point and the PyQt6 import guard."""

import os
import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

from HEACalculator.app import run

GUARD_SCRIPT = (
    "import sys;"
    "sys.modules['PyQt6']=None;"
    "sys.modules['PyQt6.QtCore']=None;"
    "sys.modules['PyQt6.QtGui']=None;"
    "sys.modules['PyQt6.QtWidgets']=None;"
    "import HEACalculator.app"
)


class TestRun:
    """Tests for run(), which owns the process lifetime.

    This is the one place real mocks are appropriate: the function creates the
    QApplication, enters the event loop and calls sys.exit.
    """

    @staticmethod
    def _patched_run() -> tuple[MagicMock, MagicMock]:
        """Execute run() with the application and window replaced by mocks.

        Returns:
            The mocked QApplication instance and the mocked main window.
        """
        application = MagicMock()
        application.exec.return_value = 0
        window = MagicMock()
        window.width.return_value = 800
        window.height.return_value = 600

        with (
            patch("HEACalculator.app.QtWidgets.QApplication", return_value=application) as application_cls,
            patch("HEACalculator.app.HEACalculatorMainWindow", return_value=window),
            patch("HEACalculator.app.QtGui.QPixmap"),
            patch("HEACalculator.app.QtGui.QIcon"),
            patch("sys.exit"),
        ):
            screen = application_cls.primaryScreen.return_value
            screen.availableGeometry.return_value.width.return_value = 1920
            screen.availableGeometry.return_value.height.return_value = 1080
            run()

        return application, window

    def test_run_shows_the_main_window(self):
        """The window becomes visible before the event loop starts."""
        _application, window = self._patched_run()

        window.show.assert_called_once()

    def test_run_starts_the_event_loop(self):
        """run() hands control to Qt."""
        application, _window = self._patched_run()

        application.exec.assert_called_once()

    def test_run_sets_the_window_icon(self):
        """The application advertises its icon to the desktop."""
        application, _window = self._patched_run()

        application.setWindowIcon.assert_called_once()

    def test_run_centers_the_window(self):
        """The window is positioned using the available screen geometry."""
        _application, window = self._patched_run()

        window.move.assert_called_once()
        x, y = window.move.call_args.args
        assert isinstance(x, int)
        assert isinstance(y, int)


class TestImportGuard:
    """Tests for the actionable error raised when PyQt6 is unavailable."""

    @staticmethod
    def _run_without_pyqt() -> subprocess.CompletedProcess:
        """Import app.py in a subprocess with PyQt6 blocked.

        A subprocess is required because the guard runs at module import time and
        PyQt6 is already imported in this interpreter.

        Returns:
            The finished subprocess, with stdout and stderr captured.
        """
        root_dir = Path(__file__).resolve().parents[2]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(root_dir / "src")

        return subprocess.run(
            [sys.executable, "-c", GUARD_SCRIPT],
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )

    def test_missing_pyqt6_fails_the_import(self):
        """Importing the GUI module without PyQt6 exits non-zero."""
        assert self._run_without_pyqt().returncode != 0

    def test_missing_pyqt6_explains_how_to_install_it(self):
        """The error names the extra to install rather than leaking an ImportError."""
        stderr = self._run_without_pyqt().stderr

        assert "PyQt6 is required for GUI mode." in stderr
        assert "HEACalculator[gui]" in stderr
