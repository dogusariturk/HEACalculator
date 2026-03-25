"""Utility helpers shared across CLI and GUI interfaces."""

import math
from collections.abc import Iterator

import numpy as np

from HEACalculator.core.helpers import nested_formula_parser


def _gen_compositions(n: int, values: tuple[float, ...], target: float) -> Iterator[tuple[float, ...]]:
    """Recursively yield every ordered n-tuple from values that sums to target.

    Values must be sorted ascending. Each valid composition is yielded exactly
    once -- no permutation step or deduplication required.
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
        tuple[dict, set]: The parsed formula dict and a set of valid composition tuples.
            Pure single-element compositions (one element at 100 at%, rest at 0 at%)
            are included when they fall naturally within the range.
    """
    formula = nested_formula_parser(alloy)
    n = len(formula)
    values = tuple(round(float(v), 10) for v in np.arange(start, end + step / 2, step))
    return formula, set(_gen_compositions(n, values, 100.0))
