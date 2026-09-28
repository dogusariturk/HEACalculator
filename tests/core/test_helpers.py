"""Tests for nested_formula_parser.

Covers simple formulas, rational stoichiometry, nested parentheses,
groups written as a share of the alloy, square brackets, zero counts,
and input validation behavior.
"""

from unittest import TestCase

import pytest

from HEACalculator.core.helpers import nested_formula_parser


class TestSimpleFormulas(TestCase):
    """Parsing of formulas that contain no parentheses or charges."""

    def test_equimolar_four_elements(self):
        """An unweighted four-element formula yields counts of 1 for each element."""
        assert nested_formula_parser("FeCoCrNi") == {"Fe": 1, "Co": 1, "Cr": 1, "Ni": 1}

    def test_single_element(self):
        """A single-element symbol returns a single-entry dict with count 1."""
        assert nested_formula_parser("Fe") == {"Fe": 1}

    def test_binary_formula(self):
        """A two-element formula without counts returns 1 for each element."""
        assert nested_formula_parser("FeNi") == {"Fe": 1, "Ni": 1}

    def test_returns_dict(self):
        """The function always returns a dict regardless of input length."""
        assert isinstance(nested_formula_parser("FeCo"), dict)

    def test_explicit_integer_counts(self):
        """Explicit integer stoichiometric coefficients are stored as integers."""
        assert nested_formula_parser("Fe2Co3") == {"Fe": 2, "Co": 3}

    def test_explicit_percentage_counts(self):
        """At-percent-style integer counts are parsed correctly."""
        result = nested_formula_parser("Fe25Co25Cr25Ni25")
        assert result == {"Fe": 25, "Co": 25, "Cr": 25, "Ni": 25}

    def test_unequal_counts(self):
        """Unequal integer stoichiometries are parsed independently per element."""
        result = nested_formula_parser("Al70Ti20V10")
        assert result == {"Al": 70, "Ti": 20, "V": 10}

    def test_repeated_element_accumulates(self):
        """A repeated element symbol accumulates its counts rather than overwriting."""
        result = nested_formula_parser("FeCoFe")
        assert result == {"Fe": 2, "Co": 1}


class TestRationalCounts(TestCase):
    """Parsing of formulas that include floating-point stoichiometries."""

    def test_float_multiplier(self):
        """A decimal stoichiometric coefficient is preserved as a float."""
        result = nested_formula_parser("Fe1.5Co")
        assert result == {"Fe": 1.5, "Co": 1}

    def test_integer_multiplier_stored_as_int(self):
        """An integer stoichiometric coefficient is stored as int, not float."""
        result = nested_formula_parser("Fe2Co")
        assert result["Fe"] == 2
        assert isinstance(result["Fe"], int)


class TestNestedParentheses(TestCase):
    """Parsing of formulas that use round-bracket groups with multipliers."""

    def test_simple_parentheses_multiplier(self):
        """A parenthesized group with an integer multiplier scales each element."""
        result = nested_formula_parser("(FeCo)2Ni")
        assert result == {"Fe": 2, "Co": 2, "Ni": 1}

    def test_parentheses_no_multiplier(self):
        """A parenthesized group without a multiplier is equivalent to no parentheses."""
        result = nested_formula_parser("(FeCo)Ni")
        assert result == {"Fe": 1, "Co": 1, "Ni": 1}

    def test_nested_parentheses(self):
        """Doubly-nested parentheses apply multipliers from innermost outward."""
        result = nested_formula_parser("((Fe)2Co)3")
        assert result == {"Fe": 6, "Co": 3}

    def test_explicit_one_matches_no_multiplier(self):
        """A group written with a count of 1 parses the same as one written without a count."""
        assert nested_formula_parser("(FeCo)1Ni") == nested_formula_parser("(FeCo)Ni")

    def test_multiplier_before_other_elements(self):
        """(FeCo)2CrNi is Fe2Co2CrNi, since its counts add up to neither 100 nor 1."""
        assert nested_formula_parser("(FeCo)2CrNi") == {"Fe": 2, "Co": 2, "Cr": 1, "Ni": 1}


class TestGroupShares(TestCase):
    """When the counts at a bracket level add up to 100 or 1, a group's count is its share of the alloy."""

    def test_group_share_in_percent(self):
        """(CoCrFeNi)90Al10 is 90 at.% equiatomic CoCrFeNi and 10 at.% Al."""
        result = nested_formula_parser("(CoCrFeNi)90Al10")
        assert result == {"Co": 22.5, "Cr": 22.5, "Fe": 22.5, "Ni": 22.5, "Al": 10}

    def test_group_share_in_fractions(self):
        """Counts that add up to 1 are read as atomic fractions, the same way as percentages."""
        result = nested_formula_parser("(CoCrFeNi)0.9Al0.1")
        assert result == pytest.approx({"Co": 0.225, "Cr": 0.225, "Fe": 0.225, "Ni": 0.225, "Al": 0.1})

    def test_group_written_after_element(self):
        """Al20(TiCoCrFeNiCuVMn)80, as Yang and Zhang write it, is 20 at.% Al."""
        result = nested_formula_parser("Al20(TiCoCrFeNiCuVMn)80")
        assert result == pytest.approx({"Al": 20} | dict.fromkeys(("Ti", "Co", "Cr", "Fe", "Ni", "Cu", "V", "Mn"), 10))

    def test_decimal_counts_adding_up_to_100(self):
        """Al11.1(TiCoCrFeNiCuVMn)88.9 adds up to 100 within floating-point rounding."""
        result = nested_formula_parser("Al11.1(TiCoCrFeNiCuVMn)88.9")
        assert result["Al"] == pytest.approx(11.1)
        assert result["Ti"] == pytest.approx(88.9 / 8)

    def test_group_counts_set_the_split(self):
        """The counts inside a group split its share: (Fe3Co)80Ni20 is 60 Fe, 20 Co and 20 Ni."""
        assert nested_formula_parser("(Fe3Co)80Ni20") == {"Fe": 60, "Co": 20, "Ni": 20}

    def test_only_the_group_ratio_matters(self):
        """Scaling the counts inside a group leaves its share unchanged."""
        assert nested_formula_parser("(Fe2Co2)90Al10") == nested_formula_parser("(FeCo)90Al10")

    def test_share_of_a_two_element_group(self):
        """(FeCo)50Ni50 is 50 at.% equiatomic FeCo, not Fe50Co50Ni50."""
        assert nested_formula_parser("(FeCo)50Ni50") == {"Fe": 25, "Co": 25, "Ni": 50}

    def test_nested_glass_notation(self):
        """[(Fe0.5Co0.5)75B20Si5]96Nb4 applies the rule at each bracket level."""
        result = nested_formula_parser("[(Fe0.5Co0.5)75B20Si5]96Nb4")
        assert result == pytest.approx({"Fe": 36, "Co": 36, "B": 19.2, "Si": 4.8, "Nb": 4})

    def test_group_counts_already_adding_up_to_one(self):
        """(Fe0.5Co0.5)72B20Si4Nb4 gives the same alloy under either reading."""
        result = nested_formula_parser("(Fe0.5Co0.5)72B20Si4Nb4")
        assert result == pytest.approx({"Fe": 36, "Co": 36, "B": 20, "Si": 4, "Nb": 4})

    def test_other_totals_still_multiply(self):
        """(CoCrFeNi)9Al1 adds up to 10, so its group count multiplies: Co9Cr9Fe9Ni9Al1."""
        assert nested_formula_parser("(CoCrFeNi)9Al1") == {"Co": 9, "Cr": 9, "Fe": 9, "Ni": 9, "Al": 1}

    def test_group_share_with_no_nonzero_count_raises(self):
        """A group given a share but holding no nonzero count cannot be split and raises."""
        with pytest.raises(ValueError, match="may not be a formula"):
            nested_formula_parser("(Fe0Co0)50Ni50")


class TestSquareBracketsAndZeroCounts(TestCase):
    """Square brackets group like round brackets; zero-count elements are dropped."""

    def test_square_brackets_group(self):
        """A multiplier after ']' scales the whole bracketed group."""
        assert nested_formula_parser("[Fe]Co") == {"Fe": 1, "Co": 1}
        assert nested_formula_parser("[FeCo]2Ni") == {"Fe": 2, "Co": 2, "Ni": 1}

    def test_zero_count_element_dropped(self):
        """An element written with a zero count is left out."""
        assert nested_formula_parser("Fe0Co50Ni50") == {"Co": 50, "Ni": 50}


@pytest.mark.parametrize("formula", ["Ni(FeCo", "Fe)Co", "2Fe", "Fe1e3", "Fe-Co", "Ti-6Al-4V", "FeCo+", "FeCo-", "Fe0Co0", ""])
def test_malformed_formula_raises(formula):
    """Malformed formulas raise ValueError instead of returning a wrong composition."""
    with pytest.raises(ValueError, match="may not be a formula"):
        nested_formula_parser(formula)


class TestValidation(TestCase):
    """Input validation and the check flag behavior."""

    def test_invalid_formula_raises_value_error(self):
        """An all-lowercase token that cannot match any element raises ValueError."""
        with pytest.raises(ValueError, match="may not be a formula"):
            nested_formula_parser("not_a_formula")

    def test_invalid_formula_check_false_no_raise(self):
        """With check=False, unrecognized letter suffixes are silently ignored."""
        result = nested_formula_parser("Fexyz", check=False)
        assert isinstance(result, dict)
        assert "Fe" in result

    def test_check_defaults_to_true(self):
        """The check parameter defaults to True in the function signature."""
        import inspect

        sig = inspect.signature(nested_formula_parser)
        assert sig.parameters["check"].default is True


class TestDeepNestingAndLargeMultipliers(TestCase):
    """Parsing of deeply nested formulas and large multipliers."""

    def test_deeply_nested_parentheses(self):
        """Three-level nesting applies multipliers from innermost outward."""
        result = nested_formula_parser("((Fe2Co)3Ni)2")
        assert result == {"Fe": 12, "Co": 6, "Ni": 2}

    def test_large_integer_multiplier(self):
        """A very large integer multiplier is stored correctly."""
        result = nested_formula_parser("Fe1000")
        assert result == {"Fe": 1000}

    def test_whitespace_in_formula_is_ignored(self):
        """Leading and trailing whitespace in a formula is silently ignored by the tokenizer."""
        result = nested_formula_parser(" Fe ")
        assert result == {"Fe": 1}

    def test_single_repeated_element(self):
        """A formula with only one element repeated accumulates to a single entry."""
        result = nested_formula_parser("FeFe")
        assert result == {"Fe": 2}
