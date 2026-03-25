"""Tests for nested_formula_parser.

Covers simple formulas, rational stoichiometry, nested parentheses,
bracket/charge stripping, and input validation behavior.
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


class TestChargeAndBracketStripping(TestCase):
    """Stripping of square brackets and ionic charge symbols before parsing."""

    def test_square_brackets_stripped(self):
        """Square brackets are removed before element counting."""
        result = nested_formula_parser("[Fe]Co")
        assert result == {"Fe": 1, "Co": 1}

    def test_positive_charge_stripped(self):
        """A trailing '+' charge symbol is stripped before parsing."""
        result = nested_formula_parser("FeCo+")
        assert result == {"Fe": 1, "Co": 1}

    def test_negative_charge_stripped(self):
        """A trailing '-' charge symbol is stripped before parsing."""
        result = nested_formula_parser("FeCo-")
        assert result == {"Fe": 1, "Co": 1}


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
