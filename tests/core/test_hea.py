"""Tests for HEACalculator facade.

Verifies that the public API attributes and computed properties
of the ``HEACalculator`` thin facade match expected values for the
FeCoCrNi reference alloy.
"""

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
