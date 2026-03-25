"""Tests for HEAThermodynamics.

Verifies all thermodynamic property calculations against known values
for the FeCoCrNi reference alloy, including edge cases and invariants.
"""

import math

import pytest

from HEACalculator.core.composition import AlloyComposition
from HEACalculator.core.thermodynamics import HEAThermodynamics


class TestHEAThermodynamics:
    """Unit tests for all thermodynamic property calculations."""

    def test_mixing_enthalpy(self, thermodynamics):
        """Mixing enthalpy for FeCoCrNi is -3.75 kJ/mol."""
        assert thermodynamics.mixing_enthalpy == pytest.approx(-3.75, abs=1e-4)

    def test_formation_enthalpy(self, thermodynamics):
        """Formation enthalpy for FeCoCrNi is -52.75 meV/atom."""
        assert thermodynamics.formation_enthalpy == pytest.approx(-52.75, abs=1e-4)

    def test_min_formation_enthalpy(self, thermodynamics):
        """Minimum formation enthalpy is no greater than the average formation enthalpy."""
        result = thermodynamics.min_formation_enthalpy
        assert result == pytest.approx(-97.0, abs=1e-4)
        assert result <= thermodynamics.formation_enthalpy

    def test_density(self, thermodynamics):
        """Density for FeCoCrNi is approximately 8.16 g/cm^3."""
        assert thermodynamics.density == pytest.approx(8.16, abs=1e-1)

    def test_valence_electron_concentration(self, thermodynamics):
        """VEC equals the weighted average of 8, 9, 6, 10 = 8.25 for FeCoCrNi."""
        assert thermodynamics.valence_electron_concentration == pytest.approx(8.25, abs=1e-4)

    def test_melting_temperature(self, thermodynamics):
        """Melting temperature equals the weighted average of constituent melting points."""
        assert thermodynamics.melting_temperature == 1858

    def test_melting_temperature_is_int(self, thermodynamics):
        """Melting temperature is returned as an integer (rounded Kelvin value)."""
        assert isinstance(thermodynamics.melting_temperature, int)

    def test_atomic_size_difference_positive(self, thermodynamics):
        """Atomic size difference is a positive float for any multi-element alloy."""
        result = thermodynamics.atomic_size_difference
        assert isinstance(result, float)
        assert result > 0

    def test_mixing_entropy(self, thermodynamics):
        """Mixing entropy for equimolar FeCoCrNi is approximately 11.53 J/mol/K."""
        assert thermodynamics.mixing_entropy == pytest.approx(11.53, abs=1e-1)

    def test_mixing_entropy_equimolar_maximum(self, thermodynamics):
        """Equimolar mixing entropy equals R*ln(N) where N is the number of components."""
        assert thermodynamics.mixing_entropy == pytest.approx(8.314462618 * math.log(4), abs=1e-4)

    def test_gamma_parameter(self, thermodynamics):
        """Gamma parameter is positive and matches the expected value for FeCoCrNi."""
        result = thermodynamics.gamma
        assert result == pytest.approx(1.035, abs=1e-2)
        assert result > 0

    def test_omega_parameter_default(self, thermodynamics):
        """Omega at the alloy's weighted melting temperature exceeds the SS threshold."""
        assert thermodynamics.omega == pytest.approx(5.71, abs=1e-1)

    def test_omega_scales_linearly_with_temperature(self, thermodynamics):
        """Omega is directly proportional to temperature, so doubling T doubles omega."""
        assert thermodynamics.omega_at(2000) / thermodynamics.omega_at(1000) == pytest.approx(2.0, abs=1e-5)

    def test_lambda_parameter(self, thermodynamics):
        """Lambda parameter is positive and matches the expected value for FeCoCrNi."""
        result = thermodynamics.lambda_
        assert result == pytest.approx(8.33, abs=1e-1)
        assert result > 0

    def test_properties_are_cached(self, thermodynamics):
        """Repeated property access returns identical values (cached, no recomputation)."""
        assert thermodynamics.mixing_enthalpy == thermodynamics.mixing_enthalpy
        assert thermodynamics.density == thermodynamics.density
        assert thermodynamics.melting_temperature == thermodynamics.melting_temperature


class TestNewProperties:
    """Tests for phi, delta_g_ss, and delta_g_max properties."""

    def test_phi_fecocrni(self, thermodynamics):
        """Phi = Omega - 1 for FeCoCrNi (Omega ~= 5.71 -> Phi ~= 4.71)."""
        assert thermodynamics.phi == pytest.approx(thermodynamics.omega - 1, abs=1e-10)

    def test_phi_positive_for_fecocrni(self, thermodynamics):
        """Phi is positive when Omega > 1."""
        assert thermodynamics.phi > 0

    def test_phi_infinite_when_mixing_enthalpy_zero(self):
        """Phi = inf when mixing_enthalpy == 0 (Omega = inf)."""
        t = HEAThermodynamics(AlloyComposition("FeCoCrNi"))
        t.__dict__["mixing_enthalpy"] = 0.0
        assert math.isinf(t.phi)

    def test_delta_g_ss_fecocrni(self, thermodynamics):
        """delta_G_ss = deltaH_mix - T_m * deltaS_mix / 1000 for FeCoCrNi."""
        expected = thermodynamics.mixing_enthalpy - thermodynamics.melting_temperature * thermodynamics.mixing_entropy / 1000
        assert thermodynamics.delta_g_ss == pytest.approx(expected, abs=1e-10)

    def test_delta_g_ss_is_negative_for_fecocrni(self, thermodynamics):
        """delta_G_ss is negative for FeCoCrNi (entropy term dominates)."""
        assert thermodynamics.delta_g_ss < 0

    def test_delta_g_max_fecocrni_is_negative(self, thermodynamics):
        """delta_G_max for FeCoCrNi is negative (most stabilizing binary is Cr-Ni)."""
        assert thermodynamics.delta_g_max < 0

    def test_delta_g_max_fecocrni_approx(self, thermodynamics):
        """delta_G_max for FeCoCrNi equals 2x the largest-magnitude pairwise mixing enthalpy."""
        assert thermodynamics.delta_g_max == pytest.approx(-14.0, abs=0.5)

    def test_delta_g_max_is_largest_magnitude(self, thermodynamics):
        """delta_G_max has the largest absolute value among all binary pair energies."""
        from HEACalculator.data.mixing_enthalpy import MixingEnthalpy

        pair_enthalpies = [MixingEnthalpy(pair) for pair in thermodynamics._c.pair_list]
        expected_max_abs = max(pair_enthalpies, key=abs)
        assert thermodynamics.delta_g_max == pytest.approx(2 * expected_max_abs, abs=1e-10)


class TestElectronegativityDifference:
    """Tests for the Allen electronegativity difference (delta_chi_Allen) property."""

    def test_electronegativity_difference_is_positive(self, thermodynamics):
        """delta_chi_Allen is strictly positive for a multi-element alloy with distinct CE values."""
        assert thermodynamics.electronegativity_difference > 0

    def test_electronegativity_difference_fecocrni(self, thermodynamics):
        """delta_chi_Allen for FeCoCrNi is approximately 4.85% (Allen CE: Fe=1.80, Co=1.84, Cr=1.65, Ni=1.88)."""
        assert thermodynamics.electronegativity_difference == pytest.approx(4.85, abs=0.01)

    def test_electronegativity_difference_is_float(self, thermodynamics):
        """delta_chi_Allen is returned as a float."""
        assert isinstance(thermodynamics.electronegativity_difference, float)

    def test_electronegativity_difference_uses_allen_scale(self, thermodynamics):
        """Verify that the result is consistent with manual calculation using Allen CE values."""
        import math

        chi = thermodynamics._c.allen_electronegativity_list
        pct = list(thermodynamics._c.atomic_percentage.values())
        chi_avg = sum(c * x for c, x in zip(pct, chi, strict=True))
        expected = math.sqrt(sum(c * (1 - x / chi_avg) ** 2 for c, x in zip(pct, chi, strict=True))) * 100
        assert thermodynamics.electronegativity_difference == pytest.approx(expected, abs=1e-10)


class TestEdgeCases:
    """Edge case tests for degenerate thermodynamic inputs."""

    def test_omega_at_zero_mixing_enthalpy_returns_inf(self):
        """omega_at() returns math.inf when mixing_enthalpy == 0 (entropy dominates)."""
        t = HEAThermodynamics(AlloyComposition("FeCoCrNi"))
        t.__dict__["mixing_enthalpy"] = 0.0
        assert math.isinf(t.omega_at(1000.0))

    def test_omega_zero_mixing_enthalpy_returns_inf(self):
        """Omega property returns math.inf when mixing_enthalpy == 0."""
        t = HEAThermodynamics(AlloyComposition("FeCoCrNi"))
        t.__dict__["mixing_enthalpy"] = 0.0
        assert math.isinf(t.omega)

    def test_lambda_zero_atomic_size_difference_returns_inf(self):
        """lambda_ returns math.inf when atomic_size_difference == 0 (no size mismatch)."""
        t = HEAThermodynamics(AlloyComposition("FeCoCrNi"))
        t.__dict__["atomic_size_difference"] = 0.0
        assert math.isinf(t.lambda_)
