"""Smoke tests for the JSON-backed mixing enthalpy loader."""

import pytest

from HEACalculator.data import MixingEnthalpy


class TestMixingEnthalpyLoader:
    """Tests for the MixingEnthalpy factory function and JSON pair database."""

    def test_fe_co_pair_returns_float(self, fe_co_pair):
        """Mixing enthalpy for a valid pair is a float."""
        assert isinstance(MixingEnthalpy(fe_co_pair), float)

    def test_order_independent(self, fe_co_pair):
        """Mixing enthalpy is symmetric: H(Fe, Co) == H(Co, Fe)."""
        assert MixingEnthalpy(fe_co_pair) == MixingEnthalpy(tuple(reversed(fe_co_pair)))

    def test_missing_pair_raises_key_error(self):
        """An unrecognized element pair raises KeyError."""
        with pytest.raises(KeyError):
            MixingEnthalpy(("Xx", "Yy"))

    def test_invalid_input_raises_type_error(self):
        """A non-tuple input raises TypeError."""
        with pytest.raises(TypeError):
            MixingEnthalpy(None)  # ty: ignore[invalid-argument-type]
