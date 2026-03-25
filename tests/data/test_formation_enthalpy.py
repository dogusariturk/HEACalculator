"""Smoke tests for the JSON-backed formation enthalpy loader."""

import pytest

from HEACalculator.data import FormationEnthalpy
from HEACalculator.exceptions import MissingFormationEnthalpyError


class TestFormationEnthalpyLoader:
    """Tests for the FormationEnthalpy factory function and JSON pair database."""

    def test_fe_co_pair_returns_float(self, fe_co_pair):
        """Formation enthalpy for a valid pair is a float."""
        assert isinstance(FormationEnthalpy(fe_co_pair), float)

    def test_order_independent(self, fe_co_pair):
        """Formation enthalpy is symmetric: H_f(Fe, Co) == H_f(Co, Fe)."""
        assert FormationEnthalpy(fe_co_pair) == FormationEnthalpy(tuple(reversed(fe_co_pair)))

    def test_missing_pair_raises_error(self):
        """An unrecognized element pair raises MissingFormationEnthalpyError."""
        with pytest.raises(MissingFormationEnthalpyError):
            FormationEnthalpy(("Xx", "Yy"))

    def test_invalid_input_raises_type_error(self):
        """A non-tuple input raises TypeError."""
        with pytest.raises(TypeError):
            FormationEnthalpy(None)
