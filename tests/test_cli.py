"""Tests for CLI search subcommands.

Uses ``typer.testing.CliRunner`` to invoke the ``single``, ``range``, and
``csv`` commands without spawning a subprocess, so no PyQt6 installation is
required.
"""

import json
import re
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from typer.testing import CliRunner

from HEACalculator import HEACalculator
from HEACalculator.cli import _worker_csv, _worker_json, _worker_str, app
from HEACalculator.exceptions import MissingFormationEnthalpyError, MissingMixingEnthalpyError

runner = CliRunner()


def _flat(text: str) -> str:
    """Flatten rich-rendered output into one line so wrapped messages can be matched.

    Typer renders ``typer.BadParameter`` messages inside a bordered box and hard-wraps
    them at the terminal width, which splits a message across lines mid-sentence.

    Args:
        text (str): Raw command output.

    Returns:
        The output with colour codes and box-drawing characters removed and all runs
            of whitespace collapsed to a single space.
    """
    _ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m")
    text = _ANSI_ESCAPE.sub("", text)
    for border in "\u2502\u256d\u2570\u256e\u256f\u2500":
        text = text.replace(border, " ")
    return " ".join(text.split())


@contextmanager
def _temp_csv(content: str) -> Iterator[str]:
    """Write content to a temporary CSV file and yield its path, removing it afterwards.

    Args:
        content (str): Full text to write to the file.

    Returns:
        The path of the temporary file, valid for the duration of the context.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(content)
        tmp_path = f.name
    try:
        yield tmp_path
    finally:
        Path(tmp_path).unlink()


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


class TestSingleSearchJson(TestCase):
    """Tests for the ``single`` subcommand ``--json`` flag."""

    def test_json_flag_exits_zero(self):
        """--json flag returns exit code 0 for a valid alloy."""
        result = runner.invoke(app, ["single", "FeCoCrNi", "--json"])
        assert result.exit_code == 0

    def test_json_output_is_valid_json(self):
        """--json output is a valid JSON object."""
        result = runner.invoke(app, ["single", "FeCoCrNi", "--json"])
        data = json.loads(result.output)
        assert isinstance(data, dict)

    def test_json_output_formula_key(self):
        """JSON output contains 'formula' key with the input alloy."""
        result = runner.invoke(app, ["single", "FeCoCrNi", "--json"])
        data = json.loads(result.output)
        assert data["formula"] == "FeCoCrNi"

    def test_json_output_density_is_float(self):
        """JSON output 'density' is a raw float, not a formatted string."""
        result = runner.invoke(app, ["single", "FeCoCrNi", "--json"])
        data = json.loads(result.output)
        assert isinstance(data["density"], float)

    def test_json_output_no_human_readable_labels(self):
        """--json output does not include human-readable property labels."""
        result = runner.invoke(app, ["single", "FeCoCrNi", "--json"])
        assert "Density" not in result.output
        assert "Mixing Enthalpy" not in result.output

    def test_json_output_nan_becomes_null(self):
        """NaN values (missing pair data) appear as JSON null in --json output."""
        result = runner.invoke(app, ["single", "Fe50Ga50", "--json"])
        data = json.loads(result.output)
        assert data["formation_enthalpy"] is None


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

    def test_csv_flag_header_matches_result_schema(self):
        """The --csv header row matches HEACalculator.get_headers() exactly."""
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
        assert result.output.splitlines()[0] == ", ".join(HEACalculator.get_headers())

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


class TestRangeSearchJson(TestCase):
    """Tests for the ``range`` subcommand ``--json`` flag."""

    def test_json_flag_exits_zero(self):
        """--json flag returns exit code 0 for a valid range."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "0", "--end", "100", "--step", "50", "--json"],
        )
        assert result.exit_code == 0

    def test_json_each_line_is_valid_json(self):
        """Each output line from --json is a valid JSON object."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "50", "--end", "50", "--step", "50", "--json"],
        )
        for line in result.stdout.strip().splitlines():
            obj = json.loads(line)
            assert "formula" in obj

    def test_json_output_has_no_csv_header(self):
        """--json output does not include the CSV header row."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "50", "--end", "50", "--step", "50", "--json"],
        )
        assert "Formula" not in result.output

    def test_json_and_csv_flags_are_mutually_exclusive(self):
        """Passing both --json and --csv causes a non-zero exit code."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "0", "--end", "100", "--step", "50", "--json", "--csv"],
        )
        assert result.exit_code != 0

    def test_json_output_density_is_float(self):
        """JSON objects from --json have a raw float 'density' field."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "50", "--end", "50", "--step", "50", "--json"],
        )
        obj = json.loads(result.stdout.strip())
        assert isinstance(obj["density"], float)


class TestRangeSearchProgress(TestCase):
    """Tests for the ``range`` subcommand's progress indicator."""

    def test_progress_label_written_to_stderr(self):
        """The progress indicator label is written to stderr, not stdout."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "0", "--end", "100", "--step", "50"],
        )
        assert "Screening compositions" in result.stderr

    def test_progress_label_does_not_pollute_stdout(self):
        """The progress indicator never appears in the plain stdout stream."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "0", "--end", "100", "--step", "50", "--csv"],
        )
        assert "Screening compositions" not in result.stdout
        assert result.stdout.splitlines()[0] == ", ".join(HEACalculator.get_headers())

    def test_no_progress_indicator_when_no_compositions_found(self):
        """No progress indicator is shown when the range produces no compositions."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "10", "--end", "20", "--step", "50"],
        )
        assert "Screening compositions" not in result.stderr


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

    def test_valid_csv_output_header_matches_result_schema(self):
        """The csv subcommand prints the shared result header row."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert result.output.splitlines()[0] == ", ".join(HEACalculator.get_headers())
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

    def test_csv_missing_column_prints_no_header(self):
        """A missing composition column writes nothing to stdout, not even the header."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("alloy_name\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code != 0
            assert result.stdout == ""
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

    def test_csv_blank_line_is_ignored_by_the_parser(self):
        """A blank line between rows is dropped by the CSV parser, not reported as an empty row."""
        with _temp_csv("composition\nFeCoCrNi\n\nFeNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
            assert "FeNi" in result.output
            assert "# Skipping empty row" not in result.stderr

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

    def test_csv_column_override_selects_named_column(self):
        """The --column option reads compositions from a non-default column name."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("alloy_name\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--column", "alloy_name"])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_column_override_is_case_insensitive(self):
        """The --column option matches the target column name case-insensitively."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("Alloy Name\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--column", "alloy name"])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_column_override_short_flag(self):
        """The -c short flag is accepted as an alias for --column."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("alloy_name\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "-c", "alloy_name"])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_column_override_missing_column_exits_nonzero(self):
        """Passing --column with a name absent from the CSV causes a non-zero exit code."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--column", "alloy_name"])
            assert result.exit_code != 0
            assert "alloy_name" in result.output
        finally:
            Path(tmp_path).unlink()

    def test_csv_column_override_ignores_default_composition_column(self):
        """When --column is given, a 'composition' column present in the file is not used."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition,alloy_name\nXxYyZz,FeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--column", "alloy_name"])
            assert result.exit_code == 0
            assert "FeCoCrNi" in result.output
        finally:
            Path(tmp_path).unlink()


class TestCsvSearchJson(TestCase):
    """Tests for the ``csv`` subcommand ``--json`` flag."""

    def test_json_flag_exits_zero(self):
        """--json flag returns exit code 0 for a valid CSV file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--json"])
            assert result.exit_code == 0
        finally:
            Path(tmp_path).unlink()

    def test_json_each_line_is_valid_json(self):
        """Each output line from --json is a valid JSON object."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\nFeNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--json"])
            for line in result.output.strip().splitlines():
                obj = json.loads(line)
                assert "formula" in obj
        finally:
            Path(tmp_path).unlink()

    def test_json_output_has_no_csv_header(self):
        """--json output does not include the CSV header row."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--json"])
            assert "Formula" not in result.output
        finally:
            Path(tmp_path).unlink()

    def test_json_output_density_is_float(self):
        """JSON objects from --json have a raw float 'density' field."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--json"])
            obj = json.loads(result.output.strip())
            assert isinstance(obj["density"], float)
        finally:
            Path(tmp_path).unlink()

    def test_json_output_formula_matches_input(self):
        """Each JSON object's 'formula' matches the input composition."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("composition\nFeCoCrNi\n")
            tmp_path = f.name
        try:
            result = runner.invoke(app, ["csv", tmp_path, "--json"])
            obj = json.loads(result.output.strip())
            assert obj["formula"] == "FeCoCrNi"
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


class TestWorkerFunctions(TestCase):
    """Tests for the ``range`` subcommand's ProcessPoolExecutor workers.

    The workers run in child processes during a real ``range`` invocation, so they are
    exercised directly here to pin their return contract and error formatting.
    """

    def test_worker_str_success_returns_report_and_no_error(self):
        """_worker_str returns the human-readable report and no error for a valid formula."""
        output, err = _worker_str("FeCoCrNi")
        assert output is not None
        assert err is None
        assert "FeCoCrNi" in output
        assert "Density" in output

    def test_worker_str_failure_returns_error_and_no_output(self):
        """_worker_str returns a skip message and no output for an unknown element."""
        output, err = _worker_str("Xx")
        assert output is None
        assert err is not None
        assert err.startswith("# Skipping 'Xx':")

    def test_worker_json_success_returns_valid_json(self):
        """_worker_json returns a JSON object carrying the input formula."""
        output, err = _worker_json("FeCoCrNi")
        assert output is not None
        assert err is None
        assert json.loads(output)["formula"] == "FeCoCrNi"

    def test_worker_json_failure_returns_error_and_no_output(self):
        """_worker_json returns a skip message and no output for an unknown element."""
        output, err = _worker_json("Xx")
        assert output is None
        assert err is not None
        assert err.startswith("# Skipping 'Xx':")

    def test_worker_csv_success_returns_row_matching_header_width(self):
        """_worker_csv returns a row with exactly as many fields as there are headers."""
        output, err = _worker_csv("FeCoCrNi")
        assert output is not None
        assert err is None
        assert len(output.split(", ")) == len(HEACalculator.get_headers())

    def test_worker_csv_failure_returns_error_and_no_output(self):
        """_worker_csv returns a skip message and no output for an unknown element."""
        output, err = _worker_csv("Xx")
        assert output is None
        assert err is not None
        assert err.startswith("# Skipping 'Xx':")

    def test_worker_error_messages_are_comment_prefixed(self):
        """Every worker prefixes its error with '#' so it is ignorable in piped output."""
        for worker in (_worker_str, _worker_json, _worker_csv):
            _, err = worker("Xx")
            assert err is not None
            assert err.startswith("#")


class TestSingleSearchErrorMessages(TestCase):
    """Tests for the error messages the ``single`` subcommand produces."""

    def test_unknown_element_message_mentions_spelling(self):
        """An unknown element symbol produces a message pointing at the spelling."""
        result = runner.invoke(app, ["single", "Xx"])
        assert result.exit_code != 0
        assert "Unknown element in 'Xx'." in _flat(result.output)
        assert "Check the symbol spelling." in _flat(result.output)

    def test_empty_formula_reports_generic_failure(self):
        """An empty formula is reported through the generic failure message."""
        result = runner.invoke(app, ["single", ""])
        assert result.exit_code != 0
        assert "Could not calculate ''" in _flat(result.output)

    def test_all_zero_composition_reports_generic_failure(self):
        """A formula whose amounts all sum to zero is reported, not raised as a traceback."""
        result = runner.invoke(app, ["single", "Fe0Ni0"])
        assert result.exit_code != 0
        assert result.exception is None or isinstance(result.exception, SystemExit)
        assert "Could not calculate 'Fe0Ni0'" in _flat(result.output)

    def test_numeric_only_formula_reports_generic_failure(self):
        """A formula containing no element symbols is reported through the generic message."""
        result = runner.invoke(app, ["single", "123"])
        assert result.exit_code != 0
        assert "Could not calculate '123'" in _flat(result.output)

    def test_lowercase_symbols_report_generic_failure(self):
        """Lowercase element symbols are reported rather than silently misparsed."""
        result = runner.invoke(app, ["single", "fe co"])
        assert result.exit_code != 0
        assert "Could not calculate 'fe co'" in _flat(result.output)

    def test_missing_mixing_enthalpy_reports_thermodynamic_data_gap(self):
        """A MissingMixingEnthalpyError is reported as a thermodynamic data gap.

        The core swallows this exception into NaN, so it is injected here to pin the
        message the handler is meant to produce.
        """
        with patch("HEACalculator.cli.HEACalculator", side_effect=MissingMixingEnthalpyError("no pair data")):
            result = runner.invoke(app, ["single", "FeNi"])
        assert result.exit_code != 0
        assert "Missing thermodynamic data for an element pair in 'FeNi'." in _flat(result.output)

    def test_missing_formation_enthalpy_reports_thermodynamic_data_gap(self):
        """A MissingFormationEnthalpyError is reported as a thermodynamic data gap."""
        with patch("HEACalculator.cli.HEACalculator", side_effect=MissingFormationEnthalpyError("no pair data")):
            result = runner.invoke(app, ["single", "FeNi"])
        assert result.exit_code != 0
        assert "Missing thermodynamic data for an element pair in 'FeNi'." in _flat(result.output)

    def test_json_flag_does_not_suppress_error_reporting(self):
        """An invalid alloy still fails loudly when --json is requested."""
        result = runner.invoke(app, ["single", "Xx", "--json"])
        assert result.exit_code != 0
        assert "Unknown element in 'Xx'." in _flat(result.output)


class TestCsvSearchEmptyRows(TestCase):
    """Tests for how the ``csv`` subcommand handles empty composition cells."""

    def test_empty_cell_is_reported_on_stderr(self):
        """An empty composition cell is reported as a skipped row on stderr."""
        with _temp_csv('composition\nFeCoCrNi\n""\nFeNi\n') as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "# Skipping empty row" in result.stderr

    def test_empty_cell_does_not_stop_remaining_rows(self):
        """Rows after an empty composition cell are still calculated."""
        with _temp_csv('composition\nFeCoCrNi\n""\nFeNi\n') as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert "FeCoCrNi" in result.stdout
            assert "FeNi" in result.stdout

    def test_empty_cell_message_does_not_pollute_stdout(self):
        """The skipped-row notice is not written to the data stream."""
        with _temp_csv('composition\nFeCoCrNi\n""\nFeNi\n') as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert "# Skipping empty row" not in result.stdout

    def test_empty_cell_in_multi_column_file_is_skipped(self):
        """An empty cell in a file with other columns is skipped, not parsed."""
        with _temp_csv("composition,note\nFeCoCrNi,a\n,b\nFeNi,c\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "# Skipping empty row" in result.stderr

    def test_empty_cell_keeps_json_stream_parseable(self):
        """With --json, a skipped empty row leaves one JSON object per stdout line."""
        with _temp_csv('composition\nFeCoCrNi\n""\nFeNi\n') as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path, "--json"])
            lines = result.stdout.strip().splitlines()
            assert len(lines) == 2
            assert [json.loads(line)["formula"] for line in lines] == ["FeCoCrNi", "FeNi"]

    def test_na_literal_is_treated_as_an_empty_row(self):
        """A literal 'NA' cell is read as missing and skipped rather than parsed as a formula."""
        with _temp_csv("composition\nFeCoCrNi\nNA\nFeNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "# Skipping empty row" in result.stderr


class TestCsvSearchBadRows(TestCase):
    """Tests for how the ``csv`` subcommand reports individual unusable rows."""

    def test_bad_row_message_names_the_offending_value(self):
        """The skip message for an invalid row includes the value that failed."""
        with _temp_csv("composition\nFeCoCrNi\nXxYyZz\nFeNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert "# Skipping 'XxYyZz':" in result.stderr

    def test_bad_row_message_does_not_pollute_stdout(self):
        """Per-row skip messages stay out of the data stream."""
        with _temp_csv("composition\nFeCoCrNi\nXxYyZz\nFeNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert "# Skipping" not in result.stdout

    def test_bad_row_keeps_json_stream_parseable(self):
        """With --json, an invalid row leaves one JSON object per stdout line."""
        with _temp_csv("composition\nFeCoCrNi\nXxYyZz\nFeNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path, "--json"])
            lines = result.stdout.strip().splitlines()
            assert len(lines) == 2
            assert [json.loads(line)["formula"] for line in lines] == ["FeCoCrNi", "FeNi"]

    def test_all_rows_invalid_still_exits_zero(self):
        """A file in which every row fails still exits 0 with only the header on stdout."""
        with _temp_csv("composition\nXxYyZz\nQqWwEe\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert result.stdout.strip() == ", ".join(HEACalculator.get_headers())

    def test_numeric_composition_cell_is_skipped(self):
        """A numeric composition cell is skipped rather than crashing the run."""
        with _temp_csv("composition\n123\nFeCoCrNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code == 0
            assert "# Skipping '123':" in result.stderr
            assert "FeCoCrNi" in result.stdout


class TestCsvSearchUnreadableFiles(TestCase):
    """Tests for files the ``csv`` subcommand cannot parse at all."""

    def test_empty_file_exits_nonzero(self):
        """A zero-byte CSV file causes a non-zero exit code."""
        with _temp_csv("") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code != 0

    def test_ragged_rows_exit_nonzero(self):
        """A CSV whose rows have inconsistent field counts causes a non-zero exit code."""
        with _temp_csv("composition\nFeCoCrNi\na,b,c\nFeNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            assert result.exit_code != 0

    def test_directory_path_exits_nonzero(self):
        """Passing a directory instead of a file causes a non-zero exit code."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            result = runner.invoke(app, ["csv", tmp_dir])
            assert result.exit_code != 0

    def test_missing_file_message_names_the_path(self):
        """The not-found message repeats the path that was given."""
        result = runner.invoke(app, ["csv", "/nonexistent/file.csv"])
        assert result.exit_code != 0
        assert "File not found: /nonexistent/file.csv" in _flat(result.output)

    def test_missing_file_is_checked_before_the_header_is_printed(self):
        """A missing file produces no header row, so failures are never mistaken for data."""
        result = runner.invoke(app, ["csv", "/nonexistent/file.csv"])
        assert "Formula, Density" not in result.stdout


class TestRangeSearchWorkerFailures(TestCase):
    """Tests for the ``range`` subcommand when individual compositions cannot be calculated."""

    def test_unknown_element_is_reported_per_composition(self):
        """A composition containing an unknown element is skipped with a message on stderr."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeXx", "--start", "0", "--end", "100", "--step", "50"],
        )
        assert result.exit_code == 0
        assert "# Skipping" in result.stderr

    def test_unknown_element_produces_no_stdout_rows(self):
        """No data reaches stdout when every screened composition fails."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeXx", "--start", "0", "--end", "100", "--step", "50"],
        )
        assert result.stdout.strip() == ""

    def test_unknown_element_still_prints_csv_header(self):
        """With --csv the header row is printed even when every composition fails."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeXx", "--start", "0", "--end", "100", "--step", "50", "--csv"],
        )
        assert result.exit_code == 0
        assert result.stdout.strip() == ", ".join(HEACalculator.get_headers())

    def test_unknown_element_keeps_json_stream_empty(self):
        """With --json a fully failing screen emits no JSON lines at all."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeXx", "--start", "0", "--end", "100", "--step", "50", "--json"],
        )
        assert result.exit_code == 0
        assert result.stdout.strip() == ""


class TestRangeSearchInvalidElements(TestCase):
    """Tests for the ``range`` subcommand's handling of unusable --elements values."""

    def test_single_element_yields_no_compositions(self):
        """Screening one element produces no rows, since pure elements are excluded."""
        result = runner.invoke(
            app,
            ["range", "--elements", "Fe", "--start", "0", "--end", "100", "--step", "50"],
        )
        assert result.exit_code == 0
        assert result.stdout.strip() == ""

    def test_empty_elements_exits_nonzero(self):
        """An empty --elements value fails rather than screening nothing successfully."""
        result = runner.invoke(
            app,
            ["range", "--elements", "", "--start", "0", "--end", "100", "--step", "50"],
        )
        assert result.exit_code != 0

    def test_numeric_only_elements_exits_nonzero(self):
        """An --elements value with no element symbols fails."""
        result = runner.invoke(
            app,
            ["range", "--elements", "123", "--start", "0", "--end", "100", "--step", "50"],
        )
        assert result.exit_code != 0

    def test_elements_option_is_required(self):
        """Omitting --elements is a usage error."""
        result = runner.invoke(app, ["range", "--start", "0", "--end", "100", "--step", "50"])
        assert result.exit_code != 0


class TestRangeSearchOptionBounds(TestCase):
    """Tests for the numeric bounds typer enforces on ``range`` options."""

    def test_negative_start_exits_nonzero(self):
        """A start below 0 is rejected by the option's minimum."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "-5", "--end", "100", "--step", "50"],
        )
        assert result.exit_code != 0

    def test_end_above_one_hundred_exits_nonzero(self):
        """An end above 100 is rejected by the option's maximum."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "0", "--end", "150", "--step", "50"],
        )
        assert result.exit_code != 0

    def test_negative_step_exits_nonzero(self):
        """A negative step is rejected by the option's minimum."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "0", "--end", "100", "--step", "-5"],
        )
        assert result.exit_code != 0

    def test_non_numeric_start_exits_nonzero(self):
        """A non-numeric start is a usage error."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "low", "--end", "100", "--step", "50"],
        )
        assert result.exit_code != 0

    def test_fractional_step_is_accepted(self):
        """A fractional step is accepted and screens the expected composition."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "49.5", "--end", "50.5", "--step", "0.5", "--csv"],
        )
        assert result.exit_code == 0
        assert "Fe50.0Ni50.0" in result.stdout


class TestOutputSchemaContract(TestCase):
    """Tests that the three output formats agree on the shared result schema."""

    def test_csv_row_field_count_matches_header(self):
        """Each --csv data row has exactly as many fields as the header."""
        result = runner.invoke(
            app,
            ["range", "--elements", "FeNi", "--start", "0", "--end", "100", "--step", "25", "--csv"],
        )
        expected = len(HEACalculator.get_headers())
        for line in result.stdout.strip().splitlines():
            assert len(line.split(", ")) == expected

    def test_csv_values_never_contain_a_comma(self):
        """No formatted value embeds a comma, which would silently shift CSV columns."""
        with _temp_csv("composition\nFeCoCrNi\nFe50Ga50\nWMoTaNb\nAlCoCrFeNi\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            expected = len(HEACalculator.get_headers())
            for line in result.stdout.strip().splitlines():
                assert len(line.split(", ")) == expected

    def test_missing_values_render_as_na_in_csv_output(self):
        """Values the models cannot compute appear as 'N/A' in the row output."""
        with _temp_csv("composition\nFe50Ga50\n") as tmp_path:
            result = runner.invoke(app, ["csv", tmp_path])
            headers = HEACalculator.get_headers()
            row = result.stdout.strip().splitlines()[1].split(", ")
            assert row[headers.index("Formation Enthalpy (meV/atom)")] == "N/A"

    def test_json_keys_match_across_subcommands(self):
        """The csv and single subcommands emit the same JSON keys for the same alloy."""
        single = runner.invoke(app, ["single", "FeCoCrNi", "--json"])
        with _temp_csv("composition\nFeCoCrNi\n") as tmp_path:
            from_csv = runner.invoke(app, ["csv", tmp_path, "--json"])
        assert json.loads(single.stdout) == json.loads(from_csv.stdout)

    def test_json_key_count_matches_header_count(self):
        """The JSON object carries one key per CSV header column."""
        result = runner.invoke(app, ["single", "FeCoCrNi", "--json"])
        assert len(json.loads(result.stdout)) == len(HEACalculator.get_headers())


class TestHelpOutput(TestCase):
    """Tests that every subcommand exposes usage help."""

    def test_app_help_lists_all_subcommands(self):
        """The top-level help lists the three search subcommands."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        for name in ("csv", "single", "range"):
            assert name in _flat(result.stdout)

    def test_single_help_exits_zero(self):
        """The single subcommand's help renders successfully."""
        assert runner.invoke(app, ["single", "--help"]).exit_code == 0

    def test_range_help_exits_zero(self):
        """The range subcommand's help renders successfully."""
        assert runner.invoke(app, ["range", "--help"]).exit_code == 0

    def test_csv_help_exits_zero(self):
        """The csv subcommand's help renders successfully."""
        assert runner.invoke(app, ["csv", "--help"]).exit_code == 0

    def test_single_without_arguments_shows_help(self):
        """The single subcommand shows its help when invoked with no arguments."""
        result = runner.invoke(app, ["single"])
        assert "--json" in _flat(result.stdout)
