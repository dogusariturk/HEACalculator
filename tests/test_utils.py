"""Tests for the utils module helper functions."""

from unittest import TestCase

import pytest

from HEACalculator.utils import find_all_comps


class TestFindAllComps(TestCase):
    """Tests for the ``find_all_comps`` helper function."""

    def test_returns_tuple(self):
        """Function returns a (dict, set) pair."""
        formula, comps = find_all_comps("FeNi", 0, 100, 50)
        assert isinstance(formula, dict)
        assert isinstance(comps, set)

    def test_formula_keys_match_elements(self):
        """The formula dict keys match the element symbols in the input string."""
        formula, _ = find_all_comps("FeNi", 0, 100, 50)
        assert set(formula.keys()) == {"Fe", "Ni"}

    def test_all_compositions_sum_to_100(self):
        """Every generated composition tuple sums to exactly 100 at%."""
        _, comps = find_all_comps("FeNi", 0, 100, 50)
        for comp in comps:
            assert sum(comp) == pytest.approx(100.0)

    def test_empty_when_no_valid_compositions(self):
        """An impossible range (step larger than range) returns an empty composition set."""
        _, comps = find_all_comps("FeNi", 0, 10, 3)
        assert len(comps) == 0

    def test_three_element_alloy(self):
        """A three-element range search produces compositions that sum to 100 at%."""
        formula, comps = find_all_comps("AlTiV", 0, 100, 50)
        assert set(formula.keys()) == {"Al", "Ti", "V"}
        for comp in comps:
            assert sum(comp) == pytest.approx(100.0)

    def test_fractional_step_includes_valid_compositions(self):
        """Fractional step sizes (e.g. 2.5) produce compositions that sum to exactly 100 at%."""
        _, comps = find_all_comps("FeNi", 0, 100, 2.5)
        for comp in comps:
            assert abs(sum(comp) - 100.0) < 1e-9

    def test_pure_element_compositions_included_when_in_range(self):
        """When start=0 and end=100, pure single-element tuples appear in the results."""
        _, comps = find_all_comps("FeNi", 0, 100, 50)
        assert (100.0, 0.0) in comps
        assert (0.0, 100.0) in comps

    def test_pure_element_compositions_excluded_when_not_in_range(self):
        """When start > 0, pure single-element tuples are absent from the results."""
        _, comps = find_all_comps("FeNi", 10, 90, 10)
        for comp in comps:
            assert all(x < 100 for x in comp)

    def test_ternary_includes_pure_element_compositions(self):
        """A ternary range with start=0 and end=100 includes pure single-element tuples."""
        _, comps = find_all_comps("AlTiV", 0, 100, 50)
        pure_element_comps = [c for c in comps if sum(1 for x in c if x > 0) == 1]
        assert len(pure_element_comps) == 3
