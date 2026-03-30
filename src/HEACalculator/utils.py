"""Utility helpers shared across CLI and GUI interfaces."""

import math
from collections.abc import Iterator

import numpy as np

from HEACalculator.core.helpers import nested_formula_parser


def _has_multiple_components(composition: tuple[float, ...]) -> bool:
    """Return True when at least two composition entries are meaningfully non-zero.

    Args:
        composition (tuple[float, ...]): Atomic fractions or percentages for all
            elements in the alloy.

    Returns:
        True if two or more entries exceed the zero threshold (abs_tol=1e-9),
            False otherwise.
    """
    return sum(1 for value in composition if not math.isclose(value, 0.0, abs_tol=1e-9)) >= 2


def _gen_compositions(n: int, values: tuple[float, ...], target: float) -> Iterator[tuple[float, ...]]:
    """Recursively yield every ordered n-tuple from values that sums to target.

    Args:
        n (int): Number of components remaining to fill in the tuple.
        values (tuple[float, ...]): Sorted candidate values for each position.
        target (float): Required sum for the remaining n positions.

    Returns:
        Ordered n-tuples drawn from values whose
            elements sum to target within abs_tol=1e-9.
    """
    if n == 1:
        for v in values:
            if math.isclose(v, target, abs_tol=1e-9):
                yield (v,)
        return
    for v in values:
        if v > target + 1e-9:
            break
        yield from ((v,) + rest for rest in _gen_compositions(n - 1, values, target - v))


def find_all_comps(alloy: str, start: float, end: float, step: float) -> tuple[dict[str, int | float], set[tuple[float, ...]]]:
    """Find all valid composition combinations for the given elements and range.

    Args:
        alloy (str): Alloy formula string defining the elements to screen.
        start (float): Lowest atomic percent for each element (inclusive).
        end (float): Highest atomic percent for each element (inclusive).
        step (float): Composition screening step size.

    Returns:
        The parsed formula dict and a set of valid composition tuples.
            Pure single-element compositions are always excluded, even when
            the range includes both 0 and 100.
    """
    formula = nested_formula_parser(alloy)
    n = len(formula)
    values = tuple(round(float(v), 10) for v in np.arange(start, end + step / 2, step))
    return formula, {composition for composition in _gen_compositions(n, values, 100.0) if _has_multiple_components(composition)}
