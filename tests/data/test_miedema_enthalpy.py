"""Tests for the Miedema-model binary enthalpy helpers and source tables."""

import pytest

from HEACalculator.data.miedema_enthalpy import (
    MiedemaEnthalpy,
    MiedemaIntEnthalpy,
    _interfacial_table,
    _params,
    _structural_solution_enthalpy,
    model_niessen_structural,
)
from HEACalculator.exceptions import MissingMiedemaDataError

MIEDEMA_FACTORIES = [
    pytest.param(MiedemaEnthalpy, id="MiedemaEnthalpy"),
    pytest.param(MiedemaIntEnthalpy, id="MiedemaIntEnthalpy"),
]


class TestMiedemaEnthalpyLoaders:
    """Shared tests for the public Miedema pair enthalpy helpers."""

    @pytest.mark.parametrize("factory", MIEDEMA_FACTORIES)
    def test_fe_co_pair_returns_float(self, factory, fe_co_pair):
        """A supported binary pair returns a float."""
        assert isinstance(factory(fe_co_pair), float)

    @pytest.mark.parametrize("factory", MIEDEMA_FACTORIES)
    def test_pair_order_and_fraction_swaps_are_equivalent(self, factory, fe_co_pair):
        """Swapping the pair order with matching fractions leaves the result unchanged."""
        assert factory(fe_co_pair, 0.25, 0.75) == pytest.approx(
            factory(tuple(reversed(fe_co_pair)), 0.75, 0.25),
            abs=1e-12,
        )

    @pytest.mark.parametrize("factory", MIEDEMA_FACTORIES)
    def test_list_input_returns_same_as_tuple(self, factory, fe_co_pair):
        """List input produces the same result as an equivalent tuple."""
        assert factory(["Fe", "Co"]) == factory(fe_co_pair)

    @pytest.mark.parametrize("factory", MIEDEMA_FACTORIES)
    def test_missing_pair_raises_missing_miedema_data_error(self, factory):
        """Missing Miedema parameters raise MissingMiedemaDataError."""
        with pytest.raises(MissingMiedemaDataError):
            factory(("Fe", "Xx"))

    @pytest.mark.parametrize("factory", MIEDEMA_FACTORIES)
    def test_invalid_input_raises_type_error(self, factory):
        """A non-sequence pair input raises TypeError."""
        with pytest.raises(TypeError):
            factory(None)

    @pytest.mark.parametrize("factory", MIEDEMA_FACTORIES)
    def test_fractions_are_normalized_before_calculation(self, factory, fe_co_pair):
        """Equivalent fractions give the same result after normalization."""
        assert factory(fe_co_pair, 25, 75) == pytest.approx(factory(fe_co_pair, 0.25, 0.75), abs=1e-12)

    @pytest.mark.parametrize("factory", MIEDEMA_FACTORIES)
    def test_zero_total_fraction_raises_value_error(self, factory, fe_co_pair):
        """Pair fractions must sum to a positive value."""
        with pytest.raises(ValueError):
            factory(fe_co_pair, 0, 0)


class TestMiedemaEnthalpyRegression:
    """Regression checks for representative published pair outputs."""

    def test_al_ni_pair_matches_current_model_8_reference_output(self):
        """The equiatomic Al-Ni pair stays aligned with the current Model 8 data tables."""
        assert MiedemaEnthalpy(("Al", "Ni")) == pytest.approx(-25.91631068931243, abs=1e-10)
        assert MiedemaIntEnthalpy(("Al", "Ni")) == pytest.approx(-46.68348161780996, abs=1e-10)


class TestMiedemaSourceTables:
    """Coverage for the source-backed Miedema parameter, interfacial, and structural tables."""

    def test_model_miedema_params_include_de_boer_values_for_model_8_elements(self):
        """The parameter table includes the expected de Boer values for supported elements."""
        assert _params["Al"]["phi_star"] == 4.20
        assert _params["Al"]["n_ws"] == 2.70
        assert _params["Al"]["V_molar"] == 10.00
        assert _params["Al"]["bulk_modulus"] == 72.18
        assert _params["Al"]["shear_modulus"] == 26.59

        assert _params["Co"]["phi_star"] == 5.10
        assert _params["Co"]["n_ws"] == 5.36
        assert _params["Co"]["V_molar"] == 6.70
        assert _params["Co"]["bulk_modulus"] == 191.5
        assert _params["Co"]["shear_modulus"] == 76.42

        assert _params["Cr"]["phi_star"] == 4.65
        assert _params["Cr"]["n_ws"] == 5.18
        assert _params["Cr"]["V_molar"] == 7.23
        assert _params["Cr"]["bulk_modulus"] == 190.3
        assert _params["Cr"]["shear_modulus"] == 116.7

        assert _params["Fe"]["phi_star"] == 4.93
        assert _params["Fe"]["n_ws"] == 5.55
        assert _params["Fe"]["V_molar"] == 7.09
        assert _params["Fe"]["bulk_modulus"] == 168.3
        assert _params["Fe"]["shear_modulus"] == 81.52

        assert _params["Ni"]["phi_star"] == 5.20
        assert _params["Ni"]["n_ws"] == 5.36
        assert _params["Ni"]["V_molar"] == 6.60
        assert _params["Ni"]["bulk_modulus"] == 186.4
        assert _params["Ni"]["shear_modulus"] == 75.05

    def test_model_miedema_params_keep_transition_classification_and_r_over_p(self):
        """Transition-metal flags and optional ``r_over_p`` values are preserved."""
        assert _params["Al"]["is_transition_metal"] is False
        assert _params["Cu"]["is_transition_metal"] is True
        assert _params["Al"]["r_over_p"] == 1.9
        assert _params["Cu"]["r_over_p"] == 0.3

    def test_model_miedema_interfacial_includes_bakker_directional_values(self):
        """Known Bakker directional values are loaded into the interfacial table."""
        assert _interfacial_table["Cr"]["Ni"] == -27
        assert _interfacial_table["Ni"]["Cr"] == -27
        assert _interfacial_table["Fe"]["Cu"] == 53
        assert _interfacial_table["Cu"]["Fe"] == 50
        assert _interfacial_table["Al"]["Ni"] == -139
        assert _interfacial_table["Ni"]["Al"] == -118
        assert _interfacial_table["Al"]["Co"] == -124
        assert _interfacial_table["Co"]["Al"] == -105

    def test_model_miedema_interfacial_leaves_bakker_gaps_absent_for_fallbacks(self):
        """Pairs without Bakker overrides are left absent so the code can fall back."""
        assert "Cu" not in _interfacial_table["Al"]
        assert "Al" not in _interfacial_table["Cu"]

    def test_model_niessen_structural_table_i_values_are_loaded(self):
        """The structural energy table loads the expected tabulated z-points and energies."""
        data = model_niessen_structural()

        assert data["z_points"] == [3.0, 4.0, 5.0, 5.5, 6.0, 7.0, 8.0, 8.5, 9.0, 10.0]
        assert data["energies_kj_per_mol"]["hcp"] == [-2.4, -2.5, 10.0, 15.0, 13.0, -5.0, -10.5, -11.0, -8.0, -1.0]
        assert data["energies_kj_per_mol"]["fcc"] == [-2.0, -1.5, 9.0, 14.0, 11.0, -3.0, -9.5, -11.0, -9.0, -2.0]
        assert data["energies_kj_per_mol"]["bcc"] == [2.2, 2.0, -9.5, -14.5, -12.0, 4.0, 10.0, 11.0, 8.5, 1.5]

    def test_model_niessen_structural_reference_structures_are_loaded(self):
        """The reference-structure lookup loads the expected integer valence mappings."""
        data = model_niessen_structural()

        assert data["reference_structures"] == {
            "3": "hcp",
            "4": "hcp",
            "5": "bcc",
            "6": "bcc",
            "7": "hcp",
            "8": "hcp",
            "9": "fcc",
            "10": "fcc",
        }

    def test_structural_solution_enthalpy_matches_niessen_eq_9_examples(self):
        """The structural solution enthalpy matches the published Niessen Eq. 9 examples."""
        assert _structural_solution_enthalpy("Co", "Cr") == -41.5
        assert _structural_solution_enthalpy("Cr", "Co") == 22.0
        assert _structural_solution_enthalpy("Ni", "Fe") == 4.5

    def test_structural_solution_enthalpy_returns_zero_outside_tabulated_range(self):
        """Out-of-range or unsupported directions return a zero structural enthalpy."""
        assert _structural_solution_enthalpy("Cu", "Ni") == 0.0
        assert _structural_solution_enthalpy("Ni", "Cu") == 0.0
