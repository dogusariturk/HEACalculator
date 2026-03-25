"""Tests for AlloyComposition.

Covers formula parsing, atomic-percentage normalization, pair-list
generation, and pair-percentage calculations for equimolar,
non-equimolar, and binary alloy inputs.
"""

import pytest

from HEACalculator.core.composition import AlloyComposition


class TestAlloyCompositionEquimolar:
    """Tests for formula parsing and derived composition data."""

    def test_formula_stored(self, composition):
        """Formula attribute stores the original input string."""
        assert composition.formula == "FeCoCrNi"

    def test_alloy_element_count(self, composition):
        """Parsed alloy contains exactly four elements including all of Fe, Co, Cr, Ni."""
        assert len(composition.alloy) == 4
        assert "Fe" in composition.alloy
        assert "Co" in composition.alloy
        assert "Cr" in composition.alloy
        assert "Ni" in composition.alloy

    def test_atomic_percentage_sums_to_one(self, composition):
        """Atomic percentages are normalized so that all fractions sum to 1.0."""
        assert sum(composition.atomic_percentage.values()) == pytest.approx(1.0, abs=1e-10)

    def test_equimolar_atomic_percentages(self, composition):
        """Each element has an equal 25 at% fraction in an equimolar four-element alloy."""
        for pct in composition.atomic_percentage.values():
            assert pct == pytest.approx(0.25, abs=1e-10)

    def test_pair_list_length(self, composition):
        """Four-element alloy produces C(4, 2) = 6 unique element pairs."""
        assert len(composition.pair_list) == 6

    def test_pair_list_are_tuples(self, composition):
        """Each entry in the pair list is a two-element tuple of element symbols."""
        for pair in composition.pair_list:
            assert isinstance(pair, tuple)
            assert len(pair) == 2

    def test_pair_percentages_length_matches_pair_list(self, composition):
        """The pair-percentage list has one entry per pair in the pair list."""
        assert len(composition.pair_percentage) == len(composition.pair_list)

    def test_pair_percentages_sum(self, composition):
        """For equimolar FeCoCrNi each pair percentage is 0.25**2 and six pairs sum to 0.375."""
        assert sum(composition.pair_percentage) == pytest.approx(0.375, abs=1e-10)

    def test_atomic_radius_list_length(self, composition):
        """The atomic-radius list contains one value per element."""
        assert len(composition.atomic_radius_list) == 4

    def test_average_atomic_radius_is_float(self, composition):
        """The weighted average atomic radius is stored as a float."""
        assert isinstance(composition.average_atomic_radius, float)

    def test_average_atomic_radius_positive(self, composition):
        """The weighted average atomic radius is a strictly positive value."""
        assert composition.average_atomic_radius > 0

    def test_allen_electronegativity_list_length(self, composition):
        """The Allen electronegativity list contains one value per element."""
        assert len(composition.allen_electronegativity_list) == 4

    def test_allen_electronegativity_list_all_positive(self, composition):
        """All Allen CE values for FeCoCrNi are finite and positive."""
        import math

        for x in composition.allen_electronegativity_list:
            assert math.isfinite(x) and x > 0

    def test_average_allen_electronegativity_fecocrni(self, composition):
        """Average Allen CE for equimolar FeCoCrNi equals (1.80+1.84+1.65+1.88)/4 = 1.7925."""
        assert composition.average_allen_electronegativity == pytest.approx(1.7925, abs=1e-4)


@pytest.fixture
def unequal_composition():
    """Return a non-equimolar three-element AlloyComposition (Fe50Co25Ni25)."""
    return AlloyComposition("Fe50Co25Ni25")


@pytest.fixture
def binary_composition():
    """Return a binary AlloyComposition (FeNi)."""
    return AlloyComposition("FeNi")


class TestAlloyCompositionUnequal:
    """Tests for a non-equimolar alloy formula."""

    def test_alloy_element_count(self, unequal_composition):
        """Non-equimolar three-element formula yields three alloy entries."""
        assert len(unequal_composition.alloy) == 3

    def test_atomic_percentage_sums_to_one(self, unequal_composition):
        """Atomic fractions are normalized to sum to 1.0 regardless of input counts."""
        assert sum(unequal_composition.atomic_percentage.values()) == pytest.approx(1.0, abs=1e-10)

    def test_fe_has_highest_fraction(self, unequal_composition):
        """The majority element (Fe at 50 at%) has a larger fraction than Co or Ni (25 at% each)."""
        assert unequal_composition.atomic_percentage["Fe"] > unequal_composition.atomic_percentage["Co"]
        assert unequal_composition.atomic_percentage["Fe"] > unequal_composition.atomic_percentage["Ni"]

    def test_pair_list_length(self, unequal_composition):
        """Three-element alloy produces C(3, 2) = 3 unique element pairs."""
        assert len(unequal_composition.pair_list) == 3


class TestAlloyCompositionBinary:
    """Tests for a two-element alloy."""

    def test_pair_list_length(self, binary_composition):
        """A binary alloy has exactly one pair."""
        assert len(binary_composition.pair_list) == 1

    def test_pair_percentage(self, binary_composition):
        """The single pair percentage equals 0.5 × 0.5 = 0.25 for an equimolar binary."""
        assert binary_composition.pair_percentage[0] == pytest.approx(0.25, abs=1e-10)
