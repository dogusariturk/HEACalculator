"""CLI search subcommands for HEACalculator."""

import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import pandas as pd
import typer

from HEACalculator import HEACalculator
from HEACalculator.exceptions import (
    ElementNotFoundError,
    MissingFormationEnthalpyError,
    MissingMixingEnthalpyError,
)
from HEACalculator.utils import find_all_comps

app = typer.Typer()


def _worker_str(formula: str) -> tuple[str | None, str | None]:
    """Compute the human-readable report for a single alloy formula.

    Intended as a ProcessPoolExecutor worker.

    Args:
        formula (str): Alloy formula string (e.g. ``Fe25Co25Cr25Ni25``).

    Returns:
        (output, None) on success, or (None, error_message) on failure.
    """
    try:
        return str(HEACalculator(formula)), None
    except Exception as e:
        return None, f"# Skipping '{formula}': {e}"


def _worker_json(formula: str) -> tuple[str | None, str | None]:
    """Compute a JSON result object for a single alloy formula.

    Intended as a ProcessPoolExecutor worker.

    Args:
        formula (str): Alloy formula string (e.g. ``Fe25Co25Cr25Ni25``).

    Returns:
        (output, None) on success, or (None, error_message) on failure.
    """
    try:
        return json.dumps(HEACalculator(formula).get_dict()), None
    except Exception as e:
        return None, f"# Skipping '{formula}': {e}"


def _worker_csv(formula: str) -> tuple[str | None, str | None]:
    """Compute a comma-separated result row for a single alloy formula.

    Intended as a ProcessPoolExecutor worker.

    Args:
        formula (str): Alloy formula string (e.g. ``Fe25Co25Cr25Ni25``).

    Returns:
        (output, None) on success, or (None, error_message) on failure.
    """
    try:
        return ", ".join(HEACalculator(formula).get_list()), None
    except Exception as e:
        return None, f"# Skipping '{formula}': {e}"


@app.command(name="csv")
def csv_search(
    csv_file: str = typer.Argument(...),
    json_output: bool = typer.Option(False, "--json", help="Output results as newline-delimited JSON"),
) -> None:
    """Calculates HEA parameters from the composition column of the given CSV file."""
    csv_path = Path(csv_file)
    if not csv_path.exists():
        raise typer.BadParameter(f"File not found: {csv_file}")

    if not json_output:
        print(", ".join(HEACalculator.get_headers()))

    df = pd.read_csv(csv_path)
    col_map = {c.lower(): c for c in df.columns}
    if "composition" not in col_map:
        raise typer.BadParameter(f"No 'composition' column found in {csv_file}. Available columns: {', '.join(df.columns)}")
    for alloy in df[col_map["composition"]]:
        if pd.isna(alloy):
            typer.echo("# Skipping empty row", err=True)
            continue
        try:
            calc = HEACalculator(alloy)
            if json_output:
                print(json.dumps(calc.get_dict()))
            else:
                print(", ".join(calc.get_list()))
        except Exception as e:
            typer.echo(f"# Skipping '{alloy}': {e}", err=True)


@app.command(no_args_is_help=True, name="single")
def single_search(
    alloy: str = typer.Argument(...),
    json_output: bool = typer.Option(False, "--json", help="Output results as JSON"),
) -> None:
    """Calculates HEA parameters of the given alloy."""
    try:
        calc = HEACalculator(alloy)
        if json_output:
            print(json.dumps(calc.get_dict()))
        else:
            print(calc)
    except ElementNotFoundError as e:
        raise typer.BadParameter(f"Unknown element in '{alloy}'. Check the symbol spelling. ({e})") from e
    except (MissingMixingEnthalpyError, MissingFormationEnthalpyError) as e:
        raise typer.BadParameter(
            f"Missing thermodynamic data for an element pair in '{alloy}'. "
            f"Not all element combinations are in the database. ({e})"
        ) from e
    except Exception as e:
        raise typer.BadParameter(f"Could not calculate '{alloy}': {e}") from e


@app.command(name="range")
def range_search(
    elements: str = typer.Option(..., help="List elements to screen for multi-component alloys"),
    start: float = typer.Option(0, min=0, max=100, help="Lowest composition for each element"),
    end: float = typer.Option(100, min=0, max=100, help="Highest composition for each element"),
    step: float = typer.Option(5, min=0, help="Composition screening step for each element"),
    csv: bool = typer.Option(False, "--csv", help="Export results to stdout as a CSV file"),
    json_output: bool = typer.Option(False, "--json", help="Output results as newline-delimited JSON"),
) -> None:
    """Screens given composition range of the given elements."""
    if csv and json_output:
        raise typer.BadParameter("--csv and --json are mutually exclusive")

    if start > end:
        raise typer.BadParameter("The End option should be higher than the Start option")

    if step == 0:
        raise typer.BadParameter("Step must be greater than 0.")

    if csv:
        print(", ".join(HEACalculator.get_headers()))

    formula, composition_set = find_all_comps(elements, start, end, step)
    alloys = [
        "".join(f"{k}{v}" for k, v in {**formula, **dict(zip(formula.keys(), composition, strict=True))}.items() if v != 0)
        for composition in composition_set
    ]

    if not alloys:
        return

    workers = min(os.cpu_count() or 1, len(alloys))
    chunksize = max(1, len(alloys) // (workers * 4))
    if csv:
        worker_fn = _worker_csv
    elif json_output:
        worker_fn = _worker_json
    else:
        worker_fn = _worker_str

    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = executor.map(worker_fn, alloys, chunksize=chunksize)
        with typer.progressbar(results, length=len(alloys), label="Screening compositions", file=sys.stderr) as progress:
            for output, err in progress:
                if err:
                    typer.echo(err, err=True)
                else:
                    print(output)
