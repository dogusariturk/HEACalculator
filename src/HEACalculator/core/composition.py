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
        """Mapping of element symbol to raw atom count.

        Returns:
            Parsed element counts from the input formula.
        """
        return nested_formula_parser(self.formula)

    @cached_property
    def elements(self) -> dict[str, _Element]:
        """Cached element data keyed by element symbol.

        Returns:
            Element records for each symbol in the alloy.
        """
        return {elm: Element(elm) for elm in self.alloy}

    @cached_property
    def atomic_percentage(self) -> dict[str, float]:
        """Mapping of element symbol to atomic fraction (values sum to 1).

        Returns:
            Atomic fractions keyed by element symbol.
        """
        total = sum(self.alloy.values())
        return {elm: num / total for elm, num in self.alloy.items()}

    @cached_property
    def pair_list(self) -> list[tuple[str, str]]:
        """All unique binary element pairs.

        Returns:
            Unique unordered element pairs from the alloy.
        """
        return list(itertools.combinations(self.alloy, 2))

    @cached_property
    def pair_percentage(self) -> list[float]:
        """Probability of each pair (product of the two atomic fractions).

        Returns:
            Pair probabilities aligned with ``pair_list``.
        """
        return [self.atomic_percentage[a] * self.atomic_percentage[b] for a, b in self.pair_list]

    @cached_property
    def atomic_radius_list(self) -> list[float]:
        """Atomic radius for each element in the same order as ``alloy``.

        Returns:
            Atomic radii in pm aligned with the alloy element order.
        """
        return [self.elements[elm].atomic_radius for elm in self.alloy]

    @cached_property
    def average_atomic_radius(self) -> float:
        """Weighted average atomic radius using atomic fractions.

        Returns:
            Composition-weighted average atomic radius in pm.
        """
        return sum(pct * r for pct, r in zip(self.atomic_percentage.values(), self.atomic_radius_list, strict=True))

    @cached_property
    def atomic_radius_cn12_list(self) -> list[float]:
        """Goldschmidt CN12 corrected atomic radius for each element in the same order as alloy.

        Returns:
            CN12 radii in pm aligned with the alloy element order.
        """
        return [self.elements[elm].atomic_radius_cn12 for elm in self.alloy]

    @cached_property
    def average_atomic_radius_cn12(self) -> float:
        """Composition-weighted average CN12 corrected atomic radius.

        Returns:
            Composition-weighted average CN12 radius in pm.
        """
        return sum(pct * r for pct, r in zip(self.atomic_percentage.values(), self.atomic_radius_cn12_list, strict=True))

    @cached_property
    def allen_electronegativity_list(self) -> list[float]:
        """Allen electronegativity for each element in the same order as ``alloy``.

        Returns:
            Allen electronegativities in Pauling units aligned with the alloy element order.
        """
        return [self.elements[elm].allen_electronegativity for elm in self.alloy]

    @cached_property
    def average_allen_electronegativity(self) -> float:
        """Composition-weighted average Allen electronegativity.

        Returns:
            Composition-weighted average Allen electronegativity in Pauling units.
        """
        return sum(pct * x for pct, x in zip(self.atomic_percentage.values(), self.allen_electronegativity_list, strict=True))

    @cached_property
    def pauling_electronegativity_list(self) -> list[float]:
        """Pauling electronegativity for each element in the same order as ``alloy``.

        Returns:
            Pauling electronegativities aligned with the alloy element order.
        """
        return [self.elements[elm].pauling_electronegativity for elm in self.alloy]

    @cached_property
    def average_pauling_electronegativity(self) -> float:
        """Composition-weighted average Pauling electronegativity.

        Returns:
            Composition-weighted average Pauling electronegativity.
        """
        return sum(pct * x for pct, x in zip(self.atomic_percentage.values(), self.pauling_electronegativity_list, strict=True))
