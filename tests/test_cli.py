"""Tests for CLI search subcommands.

Uses ``typer.testing.CliRunner`` to invoke the ``single``, ``range``, and
``csv`` commands without spawning a subprocess, so no PyQt6 installation is
required.
"""

import tempfile
from pathlib import Path
from unittest import TestCase

from typer.testing import CliRunner

from HEACalculator.cli import app

runner = CliRunner()


class TestSingleSearch(TestCase):
    """Tests for the ``single`` subcommand."""

    def test_valid_alloy_exits_zero(self):
        """A recognized alloy formula returns exit code 0."""
        result = runner.invoke(app, ["single", "FeCoCrNi"])
        assert result.exit_code == 0

    def test_valid_alloy_output_contains_formula(self):
        """The formula string appears verbatim in the command output."""
        result = runner.invoke(app, ["single", "FeCoCrNi"])
        assert "FeCoCrNi" in result.output

    def test_valid_alloy_output_contains_density(self):
        """The density property label appears in the command output."""
        result = runner.invoke(app, ["single", "FeCoCrNi"])
        assert "Density" in result.output

    def test_valid_alloy_output_contains_microstructure(self):
        """The microstructure prediction label appears in the command output."""
        result = runner.invoke(app, ["single", "FeCoCrNi"])
        assert "Microstructure" in result.output

    def test_invalid_alloy_exits_nonzero(self):
        """An unrecognized element symbol causes the command to exit with a non-zero code."""
        result = runner.invoke(app, ["single", "Xx"])
        assert result.exit_code != 0

    def test_binary_alloy(self):
        """A valid two-element formula runs without error and echoes the formula."""
        result = runner.invoke(app, ["single", "FeNi"])
        assert result.exit_code == 0
        assert "FeNi" in result.output


class TestRangeSearch(TestCase):
    """Tests for the ``range`` subcommand."""

    def test_valid_range_exits_zero(self):
        """A well-formed range invocation with valid bounds returns exit code 0."""
        result = runner.invoke(
            app,
            [
                "range",
                "--elements",
                "FeNi",
                "--start",
                "0",
                "--end",
                "100",
                "--step",
                "50",
            ],
        )
        assert result.exit_code == 0

    def test_start_greater_than_end_exits_nonzero(self):
        """Passing start > end causes the command to exit with a non-zero code."""
        result = runner.invoke(
            app,
            [
                "range",
                "--elements",
                "FeNi",
                "--start",
                "80",
                "--end",
                "20",
                "--step",
                "10",
            ],
        )
        assert result.exit_code != 0

    def test_range_zero_step_gives_bad_parameter(self):
        """Passing --step 0 causes the command to exit with a non-zero code."""
        result = runner.invoke(
            app,
            [
                "range",
                "--elements",
                "FeNi",
                "--start",
                "0",
                "--end",
                "100",
                "--step",
                "0",
            ],
        )
        assert result.exit_code != 0

    def test_csv_flag_prints_header(self):
        """The --csv flag causes the output to include a 'Formula' column header."""
        result = runner.invoke(
            app,
            [
                "range",
                "--elements",
                "FeNi",
                "--start",
                "0",
                "--end",
                "100",
                "--step",
                "50",
                "--csv",
            ],
        )
        assert result.exit_code == 0
        assert "Formula" in result.output

    def test_range_excludes_pure_single_component_results(self):
        """Range search should not print pure-element endpoints when screening alloys."""
        result = runner.invoke(
            app,
            [
                "range",
                "--elements",
                "FeNi",
                "--start",
                "0",
                "--end",
                "100",
                "--step",
                "50",
                "--csv",
            ],
        )
        assert result.exit_code == 0
        assert "Fe100.0" not in result.output
        assert "Ni100.0" not in result.output
        assert "Fe50.0Ni50.0" in result.output


class TestCsvSearch(TestCase):
    """Tests for the ``csv`` subcommand."""

    def test_valid_csv_exits_zero(self):
        """A CSV file containing valid compositions runs without error."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\nFeNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
        finally:
            Path(tmp_path).unlink()

    def test_valid_csv_output_contains_header(self):
        """The output for a valid CSV file includes a 'Formula' column header."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert "Formula" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_valid_csv_output_contains_alloy(self):
        """The output for a valid CSV file echoes the input alloy formula."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert "FeCoCrNi" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_file_not_found(self):
        """A nonexistent CSV path causes the command to exit with a non-zero code."""
        result = runner.invoke(app, ["csv", "/nonexistent/file.csv"])
        assert result.exit_code != 0

    def test_csv_missing_composition_column_exits_nonzero(self):
        """A CSV file without a 'composition' column causes the command to exit with non-zero code."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("alloy_name\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code != 0
            assert "alloy_name" in result.output or "composition" in result.output.lower()
        finally:
            Path(tmp_path).unlink()

    def test_csv_case_insensitive_composition_column(self):
        """A CSV with 'Composition' (capitalized) column is accepted."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("Composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_bad_row_is_skipped_not_crash(self):
        """A CSV with one invalid element in the middle does not crash; remaining rows appear in stdout."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\nXxYyZz\nFeNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
            assert "FeNi" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_nan_row_is_skipped(self):
        """A CSV with an empty composition cell does not crash; other rows still appear."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n\nFeNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
            assert "FeNi" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_headers_only_exits_zero(self):
        """A CSV file with headers but no data rows exits with code 0."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
        finally:
            Path(tmp_path).unlink()

    def test_csv_headers_only_output_contains_header(self):
        """A CSV file with headers but no data rows still prints the output header row."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert "Formula" in result.output
        finally:
            Path(tmp_path).unlink()


class TestRangeSearchEdgeCases(TestCase):
    """Edge case tests for the ``range`` subcommand."""

    def test_start_equals_end_exits_zero(self):
        """When start == end, the command exits successfully."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "50", "--end", "50", "--step", "5"],
        )
        assert result.exit_code == 0

    def test_step_larger_than_range_exits_zero(self):
        """When the step is larger than the range no compositions are found but the command exits 0."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "10", "--end", "20", "--step", "50"],
        )
        assert result.exit_code == 0
