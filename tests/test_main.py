"""Tests for the package entrypoint module."""

import runpy
import sys
from pathlib import Path
from types import ModuleType
from unittest import TestCase
from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from HEACalculator import __main__ as main_module

runner = CliRunner()


class TestRootApp(TestCase):
    """Tests for the top-level Typer application."""

    def test_help_lists_search_and_gui_commands(self):
        """The root CLI help includes the search group and gui command."""
        result = runner.invoke(main_module.app, ["--help"])
        assert result.exit_code == 0
        assert "search" in result.output
        assert "gui" in result.output

    def test_search_single_command_runs_from_root_app(self):
        """The root app dispatches to the search subcommands."""
        result = runner.invoke(main_module.app, ["search", "single", "FeCoCrNi"])
        assert result.exit_code == 0
        assert "FeCoCrNi" in result.output


class TestVersionOption(TestCase):
    """Tests for the ``--version``/``-V`` option."""

    def test_version_flag_exits_zero(self):
        """--version returns exit code 0."""
        result = runner.invoke(main_module.app, ["--version"])
        assert result.exit_code == 0

    def test_version_flag_prints_installed_version(self):
        """--version prints the installed package version from metadata."""
        from importlib.metadata import version as get_version  # noqa: PLC0415

        result = runner.invoke(main_module.app, ["--version"])
        assert get_version("HEACalculator") in result.output

    def test_short_version_flag_matches_long_flag(self):
        """-V is a shorthand alias for --version."""
        result = runner.invoke(main_module.app, ["-V"])
        assert result.exit_code == 0
        long_result = runner.invoke(main_module.app, ["--version"])
        assert result.output == long_result.output


class TestGuiCommand(TestCase):
    """Tests for the gui command."""

    def test_gui_command_calls_gui_runner(self):
        """The gui command imports and invokes HEACalculator.app.run."""
        fake_app_module = ModuleType("HEACalculator.app")
        fake_app_module.run = MagicMock()  # ty: ignore[unresolved-attribute]

        with patch.dict(sys.modules, {"HEACalculator.app": fake_app_module}):
            main_module.gui()

        fake_app_module.run.assert_called_once_with()


class TestModuleExecution(TestCase):
    """Tests for running the entrypoint file as a script."""

    def test_running_module_as_main_invokes_typer_app(self):
        """Executing __main__.py as __main__ calls the Typer application."""
        module_path = Path(__file__).resolve().parents[1] / "src" / "HEACalculator" / "__main__.py"

        with patch("typer.main.Typer.__call__", autospec=True) as mock_call:
            runpy.run_path(str(module_path), run_name="__main__")

        mock_call.assert_called_once()
