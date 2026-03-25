"""CLI search subcommands for HEACalculator."""

import math
from itertools import combinations_with_replacement, permutations
from pathlib import Path

import numpy as np
import pandas as pd
import typer

from HEACalculator import HEACalculator
from HEACalculator.core.helpers import nested_formula_parser
from HEACalculator.exceptions import (
    ElementNotFoundError,
    MissingFormationEnthalpyError,
    MissingMixingEnthalpyError,
)

app = typer.Typer()


@app.command(name="csv")
def csv_search(csv_file: str = typer.Argument(...)) -> None:
    """Calculates HEA parameters from the composition column of the given CSV file."""
    csv_path = Path(csv_file)
    if not csv_path.exists():
        raise typer.BadParameter(f"File not found: {csv_file}")

    header = [
        "Formula",
        "Density (g/cm^3)",
        "Delta (%)",
        "Omega",
        "Gamma",
        "Lambda",
        "VEC",
        "Mixing Enthalpy (kJ/mol)",
        "Mixing Entropy (J/K.mol)",
        "Formation Enthalpy (meV/atom)",
        "Min. Formation Enthalpy (meV/atom)",
        "Melting Temperature (K)",
        "Crystal Structure",
        "Model 1",
        "Model 2",
        "Model 3",
        "Model 4",
        "Model 5",
        "Model 6",
        "Model 7",
        "Model 8",
    ]
    print(", ".join(header))

    df = pd.read_csv(csv_path)
    col_map = {c.lower(): c for c in df.columns}
    if "composition" not in col_map:
        raise typer.BadParameter(f"No 'composition' column found in {csv_file}. Available columns: {', '.join(df.columns)}")
    for alloy in df[col_map["composition"]]:
        if pd.isna(alloy):
            typer.echo("# Skipping empty row", err=True)
            continue
        try:
            print(", ".join(HEACalculator(alloy).get_list()))
        except Exception as e:
            typer.echo(f"# Skipping '{alloy}': {e}", err=True)


@app.command(no_args_is_help=True, name="single")
def single_search(alloy: str = typer.Argument(...)) -> None:
    """Calculates HEA parameters of the given alloy."""
    try:
        print(HEACalculator(alloy))
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
    elements: str = typer.Option(..., help="List elements to search"),
    start: float = typer.Option(0, min=0, max=100, help="Lowest composition for each element"),
    end: float = typer.Option(100, min=0, max=100, help="Highest composition for each element"),
    step: float = typer.Option(5, min=0, help="Composition screening step for each element"),
    csv: bool = typer.Option(False, "--csv", help="Export results to stdout as a CSV file"),
) -> None:
    """Screens given composition range of the given elements."""
    if start > end:
        raise typer.BadParameter("The End option should be higher than the Start option")

    if step == 0:
        raise typer.BadParameter("Step must be greater than 0.")

    if csv:
        header = [
            "Formula",
            "Density (g/cm^3)",
            "Delta (%)",
            "Omega",
            "Gamma",
            "Lambda",
            "VEC",
            "Mixing Enthalpy (kJ/mol)",
            "Mixing Entropy (J/K.mol)",
            "Formation Enthalpy (meV/atom)",
            "Min. Formation Enthalpy (meV/atom)",
            "Melting Temperature (K)",
            "Crystal Structure",
            "Model 1",
            "Model 2",
            "Model 3",
            "Model 4",
            "Model 5",
            "Model 6",
            "Model 7",
            "Model 8",
        ]
        print(", ".join(header))

    formula, composition_set = find_all_comps(elements, start, end, step)
    for composition in composition_set:
        new_alloy = "".join(
            f"{k}{v}"
            for k, v in {
                **formula,
                **dict(zip(formula.keys(), composition, strict=True)),
            }.items()
            if v != 0
        )
        try:
            if csv:
                print(", ".join(HEACalculator(new_alloy).get_list()))
            else:
                print(HEACalculator(new_alloy))
        except Exception as e:
            typer.echo(f"# Skipping '{new_alloy}': {e}", err=True)


def find_all_comps(alloy: str, start: float, end: float, step: float) -> tuple[dict[str, int | float], set[tuple[float, ...]]]:
    """Find all valid composition combinations for the given elements and range.

    Args:
        alloy (str): Alloy formula string defining the elements to screen.
        start (float): Lowest atomic percent for each element (inclusive).
        end (float): Highest atomic percent for each element (inclusive).
        step (float): Composition screening step size.

    Returns:
        tuple[dict, set]: The parsed formula dict and a set of valid composition tuples.
    """
    formula = nested_formula_parser(alloy)
    no_of_elements = len(formula)
    composition_set = set()
    results = [
        i
        for i in combinations_with_replacement(np.arange(start, end + step / 2, step), no_of_elements)
        if math.isclose(sum(i), 100.0, abs_tol=1e-9) and all(x < 100 for x in i)
    ]

    for result in results:
        for composition in permutations(result):
            composition_set.add(composition)

    return formula, composition_set
