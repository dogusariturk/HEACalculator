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
        chi_line = next(line for line in lines if "Delta Chi (Allen)" in line)
        assert "%" in chi_line

    def test_str_delta_chi_pauling_present(self, calculator):
        """Delta Chi (Pauling) line appears in __str__ with % unit."""
        lines = str(calculator).splitlines()
        chi_line = next(line for line in lines if "Delta Chi (Pauling)" in line)
        assert "%" in chi_line

    def test_allen_electronegativity_difference_in_get_list(self, calculator):
        """get_list() includes allen_electronegativity_difference as a formatted float string."""
        lst = calculator.get_list()
        # index 4: formula(0), density(1), delta(2), delta_cn12(3), delta_chi_allen(4)
        assert "." in lst[4]
        assert float(lst[4]) == pytest.approx(4.85, abs=0.01)

    def test_pauling_electronegativity_difference_in_get_list(self, calculator):
        """get_list() includes pauling_electronegativity_difference as a formatted float string."""
        lst = calculator.get_list()
        # index 5: formula(0), density(1), delta(2), delta_cn12(3), delta_chi_allen(4), delta_chi_pauling(5)
        assert "." in lst[5]
        assert float(lst[5]) == pytest.approx(5.31, abs=0.01)

    def test_str_entropy_unit(self, calculator):
        """Mixing entropy unit in __str__ uses J/K.mol."""
        assert "J/K.mol" in str(calculator)

    def test_str_density_is_two_decimal_float(self, calculator):
        """Density in __str__ is formatted to two decimal places."""
        import re

        lines = str(calculator).splitlines()
        density_line = next(line for line in lines if "Density" in line)
        assert re.search(r"\d+\.\d{2}", density_line)

    def test_ea_ratio(self, calculator):
        """e/a for FeCoCrNi is 1.75 (Fe=2, Co=2, Cr=1, Ni=2 outer s-electrons)."""
        assert calculator.thermo.ea_ratio == pytest.approx(1.75)

    def test_get_list_melting_temp_no_decimal(self, calculator):
        """Melting temperature in get_list() has no decimal point."""
        lst = calculator.get_list()
        # Layout: formula(0), 14 floats(1-14), melting(15), microstructure(16), 8 models(17-24)
        assert "." not in lst[15]

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
        assert len(lst) == 25

    def test_get_list_length_is_25(self, calculator):
        """get_list() always returns exactly 25 entries regardless of missing data."""
        assert len(HEACalculator("Fe50Ga50").get_list()) == 25

    def test_headers_align_with_get_list(self, calculator):
        """Shared result headers stay in lockstep with the tabular payload."""
        assert HEACalculator.get_headers() == [
            "Formula",
            "Density (g/cm^3)",
            "Delta (%)",
            "Delta (CN12) (%)",
            "Delta Chi (Allen) (%)",
            "Delta Chi (Pauling) (%)",
            "Omega",
            "Gamma",
            "Lambda",
            "VEC",
            "e/a",
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
        assert lst[13] == "N/A"

    def test_fega_min_formation_enthalpy_na_in_get_list(self):
        """FeGa min formation enthalpy column is 'N/A'."""
        lst = HEACalculator("Fe50Ga50").get_list()
        assert lst[14] == "N/A"

    def test_fega_model_6_na_in_get_list(self):
        """Model 6 for FeGa is 'N/A' because it depends on formation enthalpy."""
        lst = HEACalculator("Fe50Ga50").get_list()
        assert lst[22] == "N/A"

    def test_fega_model_7_na_in_get_list(self):
        """Model 7 for FeGa is 'N/A' because it depends on formation enthalpy."""
        lst = HEACalculator("Fe50Ga50").get_list()
        assert lst[23] == "N/A"

    def test_fega_other_properties_are_not_na(self):
        """Properties that do not require formation enthalpy data remain finite for FeGa."""
        lst = HEACalculator("Fe50Ga50").get_list()
        for idx in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            assert lst[idx] != "N/A", f"index {idx} unexpectedly shows N/A"

    def test_femnga_ternary_get_list_length(self):
        """FeMnGa ternary with missing formation enthalpy still yields a 25-element list."""
        assert len(HEACalculator("Fe33.3Mn33.3Ga33.4").get_list()) == 25

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
        assert lst[17] == "N/A"

    def test_missing_mixing_enthalpy_propagates_na_to_model_2(self):
        """When mixing_enthalpy is NaN (mocked), Model 2 shows 'N/A'."""
        from unittest.mock import patch

        from HEACalculator.exceptions import MissingMixingEnthalpyError

        with patch(
            "HEACalculator.core.thermodynamics.MixingEnthalpy",
            side_effect=MissingMixingEnthalpyError("no data"),
        ):
            lst = HEACalculator("FeCoCrNi").get_list()
        assert lst[18] == "N/A"


class TestHEACalculatorStrAdditional:
    """Additional __str__ coverage for lines not verified by TestHEACalculator."""

    def test_str_header_contains_formula(self, calculator):
        """The first line of __str__ is a banner containing the formula."""
        assert "FeCoCrNi" in str(calculator).splitlines()[0]

    def test_str_max_formation_enthalpy_present(self, calculator):
        """Max. Formation Enthalpy appears in __str__."""
        lines = str(calculator).splitlines()
        assert any("Max. Formation Enthalpy" in line for line in lines)

    def test_str_melting_temperature_unit(self, calculator):
        """The Melting Temperature line ends with the K unit."""
        lines = str(calculator).splitlines()
        melting_line = next(line for line in lines if "Melting Temperature" in line)
        assert "K" in melting_line

    def test_str_critical_temperature_present(self, calculator):
        """Critical Temperature appears in __str__."""
        lines = str(calculator).splitlines()
        assert any("Critical Temperature" in line for line in lines)

    def test_str_phi_bcc_present(self, calculator):
        """Phi (BCC) line appears in __str__."""
        lines = str(calculator).splitlines()
        assert any("Phi (BCC)" in line for line in lines)

    def test_str_phi_fcc_present(self, calculator):
        """Phi (FCC) line appears in __str__."""
        lines = str(calculator).splitlines()
        assert any("Phi (FCC)" in line for line in lines)

    def test_str_delta_g_ss_present(self, calculator):
        """Delta G_ss line appears in __str__."""
        lines = str(calculator).splitlines()
        assert any("Delta G_ss" in line for line in lines)

    def test_str_delta_g_max_present(self, calculator):
        """Delta G_max line appears in __str__."""
        lines = str(calculator).splitlines()
        assert any("Delta G_max" in line for line in lines)

    def test_str_f_parameter_present(self, calculator):
        """F Parameter line appears in __str__."""
        lines = str(calculator).splitlines()
        assert any("F Parameter" in line for line in lines)

    def test_str_predictions_section_header(self, calculator):
        """A Predictions banner divides thermodynamics from model results."""
        assert "Predictions" in str(calculator)

    def test_str_model_1_line_contains_omega(self, calculator):
        """The Model 1 line in __str__ includes the Omega parameter."""
        lines = str(calculator).splitlines()
        model1_line = next(line for line in lines if line.strip().startswith("Model 1"))
        assert "Omega" in model1_line

    def test_str_model_6_line_contains_hf_min(self, calculator):
        """The Model 6 line in __str__ includes Hf_min."""
        lines = str(calculator).splitlines()
        model6_line = next(line for line in lines if line.strip().startswith("Model 6"))
        assert "Hf_min" in model6_line

    def test_str_model_7_line_contains_k1(self, calculator):
        """The Model 7 line in __str__ includes the k1 parameter."""
        lines = str(calculator).splitlines()
        model7_line = next(line for line in lines if line.strip().startswith("Model 7"))
        assert "k1" in model7_line


class TestGetListAdditionalValues:
    """Additional get_list() index value tests not covered by TestHEACalculator."""

    def test_get_list_density_value(self, calculator):
        """Density at index 1 matches the expected FeCoCrNi value."""
        lst = calculator.get_list()
        assert float(lst[1]) == pytest.approx(8.16, abs=1e-2)

    def test_get_list_omega_value(self, calculator):
        """Omega at index 6 matches the expected FeCoCrNi value."""
        lst = calculator.get_list()
        assert float(lst[6]) == pytest.approx(5.75, abs=1e-2)

    def test_get_list_vec_value(self, calculator):
        """VEC at index 9 is 8.25 for equimolar FeCoCrNi."""
        lst = calculator.get_list()
        assert float(lst[9]) == pytest.approx(8.25, abs=1e-2)

    def test_get_list_ea_value(self, calculator):
        """e/a at index 10 is 1.75 for equimolar FeCoCrNi."""
        lst = calculator.get_list()
        assert float(lst[10]) == pytest.approx(1.75, abs=1e-2)

    def test_get_list_mixing_enthalpy_value(self, calculator):
        """Mixing enthalpy at index 11 is -3.75 kJ/mol for FeCoCrNi."""
        lst = calculator.get_list()
        assert float(lst[11]) == pytest.approx(-3.75, abs=1e-2)

    def test_get_list_mixing_entropy_value(self, calculator):
        """Mixing entropy at index 12 is R*ln(4) for equimolar FeCoCrNi."""
        lst = calculator.get_list()
        assert float(lst[12]) == pytest.approx(11.53, abs=1e-2)

    def test_get_list_microstructure_is_valid_crystal_structure(self, calculator):
        """Crystal structure at index 16 is one of the recognized phase strings."""
        lst = calculator.get_list()
        assert lst[16] in ("FCC", "BCC", "HCP", "BCC+FCC", "N/A")

    def test_get_list_model_1_is_valid_prediction(self, calculator):
        """Model 1 at index 17 is a recognized prediction string."""
        lst = calculator.get_list()
        assert lst[17] in ("Solid Solution", "Multiple Phases", "N/A")

    def test_get_list_model_3_is_valid_prediction(self, calculator):
        """Model 3 at index 19 is a recognized prediction string."""
        lst = calculator.get_list()
        assert lst[19] in ("Solid Solution", "Multiple Phases", "N/A")

    def test_get_list_all_float_entries_parseable(self, calculator):
        """All numeric (non-formula, non-melting-temp, non-model) entries parse as float or 'N/A'."""
        lst = calculator.get_list()
        for idx in range(1, 15):
            assert lst[idx] == "N/A" or float(lst[idx]) is not None


class TestResultHeadersConstant:
    """Tests for the RESULT_HEADERS module-level constant."""

    def test_result_headers_count(self):
        """RESULT_HEADERS contains exactly 25 entries."""
        from HEACalculator.core.hea import RESULT_HEADERS

        assert len(RESULT_HEADERS) == 25

    def test_result_headers_first_is_formula(self):
        """First header is 'Formula'."""
        from HEACalculator.core.hea import RESULT_HEADERS

        assert RESULT_HEADERS[0] == "Formula"

    def test_result_headers_last_is_model_8(self):
        """Last header is 'Model 8'."""
        from HEACalculator.core.hea import RESULT_HEADERS

        assert RESULT_HEADERS[-1] == "Model 8"

    def test_get_headers_returns_list_copy(self):
        """get_headers() returns a fresh list, not the underlying tuple."""
        from HEACalculator.core.hea import RESULT_HEADERS

        result = HEACalculator.get_headers()
        assert isinstance(result, list)
        assert tuple(result) == RESULT_HEADERS
