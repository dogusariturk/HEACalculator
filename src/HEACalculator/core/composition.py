"""Alloy composition parsing and data preparation."""

from __future__ import annotations

import itertools
from functools import cached_property
from typing import TYPE_CHECKING

from HEACalculator.core.helpers import nested_formula_parser
from HEACalculator.data import Element

if TYPE_CHECKING:
    from HEACalculator.data.elements import _Element

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"


class AlloyComposition:
    """Parses a chemical formula and exposes composition data needed for calculations.

    Args:
        formula (str): Alloy formula string (e.g. ``"FeCoCrNi"`` or ``"Fe25Co25Cr25Ni25"``).

    Attributes:
        formula (str): The original formula string.
    """

    def __init__(self, formula: str) -> None:
        """Initialize with *formula*; all derived properties are computed lazily on first access.

        Raises:
            KeyError: If any element symbol in the formula is not in the element database.
        """
        self.formula = formula

    @cached_property
    def alloy(self) -> dict[str, float]:
        """Mapping of element symbol to raw atom count."""
        return nested_formula_parser(self.formula)

    @cached_property
    def elements(self) -> dict[str, _Element]:
        """Cached element data keyed by element symbol."""
        return {elm: Element(elm) for elm in self.alloy}

    @cached_property
    def atomic_percentage(self) -> dict[str, float]:
        """Mapping of element symbol to atomic fraction (values sum to 1)."""
        total = sum(self.alloy.values())
        return {elm: num / total for elm, num in self.alloy.items()}

    @cached_property
    def pair_list(self) -> list[tuple[str, str]]:
        """All unique binary element pairs."""
        return list(itertools.combinations(self.alloy, 2))

    @cached_property
    def pair_percentage(self) -> list[float]:
        """Probability of each pair (product of the two atomic fractions)."""
        return [self.atomic_percentage[a] * self.atomic_percentage[b] for a, b in self.pair_list]

    @cached_property
    def atomic_radius_list(self) -> list[float]:
        """Atomic radius for each element in the same order as ``alloy``."""
        return [self.elements[elm].atomic_radius for elm in self.alloy]

    @cached_property
    def average_atomic_radius(self) -> float:
        """Weighted average atomic radius using atomic fractions."""
        return sum(pct * r for pct, r in zip(self.atomic_percentage.values(), self.atomic_radius_list, strict=True))

    @cached_property
    def atomic_radius_cn12_list(self) -> list[float]:
        """Goldschmidt CN12 corrected atomic radius for each element in the same order as alloy."""
        return [self.elements[elm].atomic_radius_cn12 for elm in self.alloy]

    @cached_property
    def average_atomic_radius_cn12(self) -> float:
        """Composition-weighted average CN12 corrected atomic radius."""
        return sum(pct * r for pct, r in zip(self.atomic_percentage.values(), self.atomic_radius_cn12_list, strict=True))

    @cached_property
    def allen_electronegativity_list(self) -> list[float]:
        """Allen electronegativity for each element in the same order as ``alloy``."""
        return [self.elements[elm].allen_electronegativity for elm in self.alloy]

    @cached_property
    def average_allen_electronegativity(self) -> float:
        """Composition-weighted average Allen electronegativity."""
        return sum(pct * x for pct, x in zip(self.atomic_percentage.values(), self.allen_electronegativity_list, strict=True))
