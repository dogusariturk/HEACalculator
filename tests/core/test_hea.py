"""Tests for HEACalculator facade.

Verifies that the public API attributes and computed properties
of the ``HEACalculator`` thin facade match expected values for the
FeCoCrNi reference alloy.
"""

import math

import pytest

from HEACalculator.core.hea import HEACalculator


class TestHEACalculator:
    """Smoke tests for the public attributes of HEACalculator."""

    def test_formula(self, calculator):
        """Formula attribute reflects the input string unchanged."""
        assert calculator.formula == "FeCoCrNi"

    def test_mixing_enthalpy(self, calculator):
        """Mixing enthalpy for FeCoCrNi is negative (exothermic)."""
        assert calculator.thermo.mixing_enthalpy == pytest.approx(-3.75)

    def test_density(self, calculator):
        """Density is within 0.01 g/cm^3 of the literature value."""
        assert calculator.thermo.density == pytest.approx(8.16, abs=1e-2)

    def test_valence_electron_concentration(self, calculator):
        """VEC for FeCoCrNi is 8.25 (average of Fe=8, Co=9, Cr=6, Ni=10)."""
        assert calculator.thermo.valence_electron_concentration == pytest.approx(8.25, abs=1e-2)

    def test_melting_temperature(self, calculator):
        """Melting temperature is the weighted average of constituent melting points."""
        assert calculator.thermo.melting_temperature == 1872

    def test_atomic_size_difference(self, calculator):
        """Atomic size difference for FeCoCrNi using Slater radii (Fe=126, Co=125, Cr=128, Ni=124 pm)."""
        assert calculator.thermo.atomic_size_difference == pytest.approx(1.18, abs=1e-2)

    def test_mixing_entropy(self, calculator):
        """Mixing entropy equals R*ln(4) for an equimolar 4-element alloy."""
        assert calculator.thermo.mixing_entropy == pytest.approx(11.53, abs=1e-2)

    def test_microstructure(self, calculator):
        """FeCoCrNi is experimentally known to form an FCC solid solution."""
        assert calculator.predictor.microstructure == "FCC"

    def test_omega_parameter(self, calculator):
        """Omega parameter for FeCoCrNi exceeds the solid-solution threshold of 1.1."""
        assert calculator.thermo.omega == pytest.approx(5.75, abs=1e-2)

    def test_str_density_format(self, calculator):
        """Density in __str__ uses g/cm^3 unit."""
        assert "g/cm^3" in str(calculator)

    def test_str_delta_has_percent_unit(self, calculator):
        """Delta in __str__ includes % unit."""
        lines = str(calculator).splitlines()
        delta_line = next(line for line in lines if line.strip().startswith("Delta") and "Chi" not in line)
        assert "%" in delta_line

    def test_str_delta_chi_allen_present(self, calculator):
        """Delta Chi (Allen) line appears in __str__ with % unit."""
        lines = str(calculator).splitlines()
        chi_line = next(line for line in lines if "Delta Chi" in line)
        assert "%" in chi_line

    def test_electronegativity_difference_in_get_list(self, calculator):
        """get_list() includes electronegativity_difference as a formatted float string."""
        lst = calculator.get_list()
        # index 4: formula(0), density(1), delta(2), delta_cn12(3), delta_chi(4)
        assert "." in lst[4]
        assert float(lst[4]) == pytest.approx(4.85, abs=0.01)

    def test_str_entropy_unit(self, calculator):
        """Mixing entropy unit in __str__ uses J/K.mol."""
        assert "J/K.mol" in str(calculator)

    def test_str_density_is_two_decimal_float(self, calculator):
        """Density in __str__ is formatted to two decimal places."""
        import re

        lines = str(calculator).splitlines()
        density_line = next(line for line in lines if "Density" in line)
        assert re.search(r"\d+\.\d{2}", density_line)

    def test_get_list_melting_temp_no_decimal(self, calculator):
        """Melting temperature in get_list() has no decimal point."""
        lst = calculator.get_list()
        # Layout: formula(0), 12 floats(1-12), melting(13), microstructure(14), 8 models(15-22)
        assert "." not in lst[13]

    def test_get_list_model_5_is_string_not_na(self, calculator):
        """Model 5 in get_list() returns a valid phase prediction string."""
        lst = calculator.get_list()
        assert lst[-4] in ("Solid Solution", "Multiple Phases")  # model_5 is 4th from end

    def test_get_list_model_8_returns_prediction(self, calculator):
        """Model 8 in get_list() returns a valid phase prediction."""
        lst = calculator.get_list()
        assert lst[-1] in ("Solid Solution", "Multiple Phases")  # model_8 is last

    def test_single_element_get_list_does_not_crash(self):
        """A single-element calculation should still produce a result row."""
        lst = HEACalculator("Fe").get_list()
        assert lst[0] == "Fe"
        assert len(lst) == 23

    def test_get_list_length_is_23(self, calculator):
        """get_list() always returns exactly 23 entries regardless of missing data."""
        assert len(HEACalculator("Fe50Ga50").get_list()) == 23

    def test_headers_align_with_get_list(self, calculator):
        """Shared result headers stay in lockstep with the tabular payload."""
        assert HEACalculator.get_headers() == [
            "Formula",
            "Density (g/cm^3)",
            "Delta (%)",
            "Delta (CN12) (%)",
            "Delta Chi (Allen) (%)",
            "Omega",
            "Gamma",
            "Lambda",
            "VEC",
            "Mixing Enthalpy (kJ/mol)",
            "Mixing Entropy (J/K.mol)",
            "Formation Enthalpy (meV/atom)",
            "Min. Formation Enthalpy (meV/atom)",
            "Melting Temperature (K)",
            "Crystal Structure",
            "Model 1",
            "Model 2",
            "Model 3",
            "Model 4",
            "Model 5",
            "Model 6",
            "Model 7",
            "Model 8",
        ]
        assert len(HEACalculator.get_headers()) == len(calculator.get_list())


class TestFmtHelper:
    """Unit tests for the _fmt formatting helper."""

    def test_nan_with_width_spec_is_right_aligned(self):
        """NaN formatted with '>10.2f' gives right-aligned 'N/A' in a width-10 field."""
        result = HEACalculator._fmt(float("nan"), ">10.2f")
        assert result == f"{'N/A':>10}"
        assert len(result) == 10

    def test_nan_with_precision_only_spec_is_bare_na(self):
        """NaN formatted with '.2f' (no width) returns the bare string 'N/A'."""
        assert HEACalculator._fmt(float("nan"), ".2f") == "N/A"

    def test_nan_default_spec_is_right_aligned(self):
        """NaN with the default spec ('>10.2f') is right-aligned to width 10."""
        result = HEACalculator._fmt(float("nan"))
        assert result == f"{'N/A':>10}"

    def test_normal_float_uses_spec(self):
        """A finite float is formatted with the given spec unchanged."""
        assert HEACalculator._fmt(7.84, ".2f") == "7.84"
        assert HEACalculator._fmt(7.84, ">10.2f") == f"{7.84:>10.2f}"

    def test_int_passes_through(self):
        """An integer value is not treated as NaN."""
        assert HEACalculator._fmt(1872, ">10") == f"{1872:>10}"

    def test_inf_passes_through(self):
        """math.inf is not NaN and is formatted normally."""
        assert HEACalculator._fmt(math.inf, ".2f") == "inf"


class TestNaNIntegration:
    """Integration tests: alloys with genuinely missing database entries."""

    def test_fega_formation_enthalpy_na_in_get_list(self):
        """FeGa has no Troparevsky formation enthalpy data; get_list shows 'N/A'."""
        lst = HEACalculator("Fe50Ga50").get_list()
        assert lst[11] == "N/A"

    def test_fega_min_formation_enthalpy_na_in_get_list(self):
        """FeGa min formation enthalpy column is 'N/A'."""
        lst = HEACalculator("Fe50Ga50").get_list()
        assert lst[12] == "N/A"

    def test_fega_model_6_na_in_get_list(self):
        """Model 6 for FeGa is 'N/A' because it depends on formation enthalpy."""
        lst = HEACalculator("Fe50Ga50").get_list()
        assert lst[20] == "N/A"

    def test_fega_model_7_na_in_get_list(self):
        """Model 7 for FeGa is 'N/A' because it depends on formation enthalpy."""
        lst = HEACalculator("Fe50Ga50").get_list()
        assert lst[21] == "N/A"

    def test_fega_other_properties_are_not_na(self):
        """Properties that do not require formation enthalpy data remain finite for FeGa."""
        lst = HEACalculator("Fe50Ga50").get_list()
        for idx in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            assert lst[idx] != "N/A", f"index {idx} unexpectedly shows N/A"

    def test_femnga_ternary_get_list_length(self):
        """FeMnGa ternary with missing formation enthalpy still yields a 23-element list."""
        assert len(HEACalculator("Fe33.3Mn33.3Ga33.4").get_list()) == 23

    def test_fega_str_shows_na_for_formation_enthalpy(self):
        """__str__ for FeGa shows 'N/A' in the Formation Enthalpy line."""
        output = str(HEACalculator("Fe50Ga50"))
        fe_line = next(
            line for line in output.splitlines() if "Formation Enthalpy" in line and "Min" not in line and "Max" not in line
        )
        assert "N/A" in fe_line

    def test_fega_str_shows_na_for_model_6(self):
        """__str__ for FeGa shows 'N/A' in the Model 6 line."""
        output = str(HEACalculator("Fe50Ga50"))
        m6_line = next(line for line in output.splitlines() if line.strip().startswith("Model 6"))
        assert "N/A" in m6_line

    def test_missing_mixing_enthalpy_propagates_na_to_model_1(self):
        """When mixing_enthalpy is NaN (mocked), Model 1 shows 'N/A'."""
        from unittest.mock import patch

        from HEACalculator.exceptions import MissingMixingEnthalpyError

        with patch(
            "HEACalculator.core.thermodynamics.MixingEnthalpy",
            side_effect=MissingMixingEnthalpyError("no data"),
        ):
            lst = HEACalculator("FeCoCrNi").get_list()
        assert lst[15] == "N/A"

    def test_missing_mixing_enthalpy_propagates_na_to_model_2(self):
        """When mixing_enthalpy is NaN (mocked), Model 2 shows 'N/A'."""
        from unittest.mock import patch

        from HEACalculator.exceptions import MissingMixingEnthalpyError

        with patch(
            "HEACalculator.core.thermodynamics.MixingEnthalpy",
            side_effect=MissingMixingEnthalpyError("no data"),
        ):
            lst = HEACalculator("FeCoCrNi").get_list()
        assert lst[16] == "N/A"
