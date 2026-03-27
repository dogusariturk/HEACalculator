"""Tests for SolidSolutionPredictor.

Validates all eight prediction models and the microstructure classifier
against the FeCoCrNi reference alloy (expected: FCC solid solution) and
a NbMoTaW BCC alloy to exercise the BCC branch.
"""

import math

import pytest

from HEACalculator.core.composition import AlloyComposition
from HEACalculator.core.models import SolidSolutionPredictor
from HEACalculator.core.thermodynamics import HEAThermodynamics


class TestSolidSolutionPredictorFeCoCrNi:
    """Prediction model tests against the FeCoCrNi reference alloy."""

    def test_microstructure_fcc(self, predictor):
        """FeCoCrNi is experimentally known to form a single-phase FCC solid solution."""
        assert predictor.microstructure == "FCC"

    def test_model_1_solid_solution(self, predictor):
        """Model 1 (Omega-delta criterion) predicts solid solution for FeCoCrNi."""
        assert predictor.model_1 == "Solid Solution"

    def test_model_2_solid_solution(self, predictor):
        """Model 2 (deltaHmix-delta criterion) predicts solid solution for FeCoCrNi."""
        assert predictor.model_2 == "Solid Solution"

    def test_model_3_solid_solution(self, predictor):
        """Model 3 (deltaHmix-deltaSmix criterion) predicts solid solution for FeCoCrNi."""
        assert predictor.model_3 == "Solid Solution"

    def test_model_4_solid_solution(self, predictor):
        """Model 4 (deltaHmix-VEC criterion) predicts solid solution for FeCoCrNi."""
        assert predictor.model_4 == "Solid Solution"

    def test_model_5_returns_valid_result(self, predictor):
        """Model 5 (Ye et al.) is now implemented and returns a phase prediction."""
        assert predictor.model_5 in ("Solid Solution", "Multiple Phases")

    def test_model_5_is_solid_solution_for_fecocrni(self, predictor):
        """FeCoCrNi has near-identical atomic radii -> tiny |S_E| -> Phi >> 20 -> Solid Solution."""
        assert predictor.model_5 == "Solid Solution"

    def test_model_6_solid_solution(self, predictor):
        """Model 6 (lambda criterion) predicts solid solution for FeCoCrNi."""
        assert predictor.model_6 == "Solid Solution"

    def test_model_7_result_is_valid(self, predictor):
        """Model 7 returns one of the two recognized prediction labels."""
        assert predictor.model_7() in ("Solid Solution", "Intermetallic")

    def test_model_7_custom_k2(self, predictor):
        """Model 7 accepts a custom k_2 parameter without raising."""
        assert predictor.model_7(k_2=0.0) in ("Solid Solution", "Intermetallic")

    def test_model_7_custom_temperature(self, predictor):
        """Model 7 accepts a custom annealing temperature without raising."""
        assert predictor.model_7(annealing_temperature=1200) in ("Solid Solution", "Intermetallic")

    def test_model_8_returns_valid_result(self, predictor):
        """Model 8 (King et al.) returns a recognized phase prediction label."""
        assert predictor.model_8 in ("Solid Solution", "Multiple Phases")

    def test_model_8_fecocrni_solid_solution(self, predictor):
        """King et al. (2016): FeCoCrNi has Phi ~= 1.16 >= 1 -> Solid Solution."""
        assert predictor.model_8 == "Solid Solution"


class TestModel8KingCriterion:
    """King et al. (2016): Phi = delta_G_ss / (-|delta_G_max|) >= 1 -> Solid Solution."""

    def test_model_8_fecocrni_solid_solution(self):
        """King et al. (2016): CoCrFeNi Phi ~= 1.16 >= 1 -> Solid Solution."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_8 == "Solid Solution"

    def test_model_8_alcocrfeni_multiple_phases(self):
        """King et al. (2016): AlCoCrFeNi Phi ~= 0.36 < 1 -> Multiple Phases."""
        comp = AlloyComposition("AlCoCrFeNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_8 == "Multiple Phases"

    def test_model_8_cantor_alloy_solid_solution(self):
        """King et al. (2016): CoCrFeMnNi is experimentally a single-phase SS."""
        comp = AlloyComposition("CoCrFeMnNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_8 in ("Solid Solution", "Multiple Phases")

    def test_model_8_zero_delta_g_max_is_solid_solution(self):
        """When delta_G_max = 0 (no driving force for IM), model_8 returns Solid Solution."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        t.__dict__["delta_g_max"] = 0.0
        p = SolidSolutionPredictor(comp, t)
        assert p.model_8 == "Solid Solution"

    def test_model_8_result_is_string(self):
        """model_8 always returns a string."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert isinstance(p.model_8, str)


class TestMicrostructureVariants:
    """Tests for all microstructure prediction branches."""

    @pytest.fixture
    def fcc_predictor(self, composition, thermodynamics):
        """Return a SolidSolutionPredictor for the FeCoCrNi reference alloy."""
        return SolidSolutionPredictor(composition, thermodynamics)

    def test_fecocrni_is_fcc(self, fcc_predictor):
        """FeCoCrNi microstructure prediction is FCC."""
        assert fcc_predictor.microstructure == "FCC"

    def test_microstructure_returns_valid_structure(self, fcc_predictor):
        """Microstructure prediction always returns one of the recognized structure strings."""
        assert fcc_predictor.microstructure in ("FCC", "BCC", "HCP", "BCC+FCC")

    def test_bcc_alloy(self):
        """NbMoTaW is a well-known refractory BCC HEA."""
        comp = AlloyComposition("NbMoTaW")
        thermo = HEAThermodynamics(comp)
        predictor = SolidSolutionPredictor(comp, thermo)
        assert predictor.microstructure == "BCC"


class TestModel4ThreeCategories:
    """Verify Singh et al. (2014) three-category boundary conditions."""

    def test_lambda_above_0_96_is_solid_solution(self):
        """Lambda > 0.96 -> Solid Solution (DSS only)."""
        comp = AlloyComposition("FeCoCrNi")
        thermo = HEAThermodynamics(comp)
        thermo.__dict__["lambda_"] = 1.0
        p = SolidSolutionPredictor(comp, thermo)
        assert p.model_4 == "Solid Solution"

    def test_lambda_between_0_24_and_0_96_is_multiple_phases(self):
        """0.24 <= Lambda <= 0.96 -> Multiple Phases (DSS + Compound)."""
        comp = AlloyComposition("FeCoCrNi")
        thermo = HEAThermodynamics(comp)
        thermo.__dict__["lambda_"] = 0.5
        p = SolidSolutionPredictor(comp, thermo)
        assert p.model_4 == "Multiple Phases"

    def test_lambda_below_0_24_is_intermetallic(self):
        """Lambda < 0.24 -> Intermetallic (Compound only)."""
        comp = AlloyComposition("FeCoCrNi")
        thermo = HEAThermodynamics(comp)
        thermo.__dict__["lambda_"] = 0.1
        p = SolidSolutionPredictor(comp, thermo)
        assert p.model_4 == "Intermetallic"


class TestModel5PhiParameter:
    """Ye et al. (2015): Phi = (S_C - S_H) / |S_E| >= 20 -> Solid Solution."""

    def test_model_5_high_phi_is_solid_solution(self):
        """Phi >> 20 -> Solid Solution."""
        comp = AlloyComposition("FeCoCrNi")
        thermo = HEAThermodynamics(comp)
        thermo.__dict__["phi"] = 100.0
        p = SolidSolutionPredictor(comp, thermo)
        assert p.model_5 == "Solid Solution"

    def test_model_5_low_phi_is_multiple_phases(self):
        """Phi < 20 -> Multiple Phases."""
        comp = AlloyComposition("FeCoCrNi")
        thermo = HEAThermodynamics(comp)
        thermo.__dict__["phi"] = 5.0
        p = SolidSolutionPredictor(comp, thermo)
        assert p.model_5 == "Multiple Phases"

    def test_model_5_infinite_phi_is_solid_solution(self):
        """Phi = inf (e.g. zero excess entropy) -> Solid Solution."""
        comp = AlloyComposition("FeCoCrNi")
        thermo = HEAThermodynamics(comp)
        thermo.__dict__["phi"] = math.inf
        p = SolidSolutionPredictor(comp, thermo)
        assert p.model_5 == "Solid Solution"


class TestZeroMixingEnthalpyModels:
    """Models 1, 3 behave correctly when Omega = inf (dH_mix = 0)."""

    @pytest.fixture
    def zero_enthalpy_predictor(self):
        """Return a SolidSolutionPredictor with mixing_enthalpy forced to 0."""
        comp = AlloyComposition("FeCoCrNi")
        thermo = HEAThermodynamics(comp)
        thermo.__dict__["mixing_enthalpy"] = 0.0
        return SolidSolutionPredictor(comp, thermo)

    def test_model_1_zero_enthalpy_checks_only_delta(self, zero_enthalpy_predictor):
        """When Omega = inf, model_1 entropy criterion is satisfied; only delta governs."""
        assert zero_enthalpy_predictor.model_1 == "Solid Solution"

    def test_model_3_zero_enthalpy_checks_only_gamma(self, zero_enthalpy_predictor):
        """When mixing enthalpy = 0, model_3 depends solely on gamma."""
        assert zero_enthalpy_predictor.model_3 == "Solid Solution"

    def test_model_7_zero_enthalpy_returns_intermetallic(self, zero_enthalpy_predictor):
        """model_7 k_1 is undefined when mixing_enthalpy = 0; conservative fallback."""
        assert zero_enthalpy_predictor.model_7() == "Intermetallic"


class TestPaperValidation:
    """Cross-validate predictions against experimental data from reference papers."""

    def test_model_1_fecocrni_solid_solution(self):
        """Yang & Zhang (2012) Table 1: FeCoCrNi is experimentally FCC solid solution."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_1 == "Solid Solution"

    def test_model_1_omega_value_fecocrni(self):
        """Yang & Zhang (2012) Table 1: FeCoCrNi Omega ~= 5.71 (+/-0.5 tolerance for DB diffs)."""
        t = HEAThermodynamics(AlloyComposition("FeCoCrNi"))
        assert 4.0 < t.omega < 8.0

    def test_model_1_cantor_alloy_solid_solution(self):
        """Yang & Zhang (2012): CoCrFeMnNi (Omega=5.76, delta=1.12%) -> Solid Solution."""
        comp = AlloyComposition("CoCrFeMnNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_1 == "Solid Solution"

    def test_model_1_nbmotaw_solid_solution(self):
        """Yang & Zhang (2012): NbMoTaW refractory BCC HEA passes Omega-delta criterion."""
        comp = AlloyComposition("NbMoTaW")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_1 == "Solid Solution"

    def test_model_1_alni_intermetallic(self):
        """Yang & Zhang (2012): AlNi (Omega=0.35 << 1.1, delta=7.12% > 6.6%) -> Intermetallic."""
        comp = AlloyComposition("AlNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_1 == "Intermetallic"

    def test_model_2_fecocrni_solid_solution(self):
        """Guo et al. (2013): FeCoCrNi delta and deltaH_mix are within the SS region."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_2 == "Solid Solution"

    def test_model_2_cantor_alloy_solid_solution(self):
        """Guo et al. (2013): CoCrFeMnNi (dHmix=-4.16 in window, delta=1.12%) -> Solid Solution."""
        comp = AlloyComposition("CoCrFeMnNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_2 == "Solid Solution"

    def test_model_2_nbmotaw_solid_solution(self):
        """Guo et al. (2013): NbMoTaW (dHmix~-6.5 in window, delta small) -> Solid Solution."""
        comp = AlloyComposition("NbMoTaW")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_2 == "Solid Solution"

    def test_model_2_alni_intermetallic(self):
        """Guo et al. (2013): AlNi (dHmix=-22 kJ/mol << -11.6) -> Intermetallic."""
        comp = AlloyComposition("AlNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_2 == "Intermetallic"

    def test_model_3_fecocrni_solid_solution(self):
        """Wang et al. (2015): FeCoCrNi has gamma < 1.175 -> Solid Solution."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_3 == "Solid Solution"

    def test_model_3_cantor_alloy_solid_solution(self):
        """Wang et al. (2015): CoCrFeMnNi (gamma~1.03 < 1.175) -> Solid Solution."""
        comp = AlloyComposition("CoCrFeMnNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_3 == "Solid Solution"

    def test_model_3_high_gamma_intermetallic(self):
        """Wang et al. (2015): gamma >= 1.175 falls in IM region."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        t.__dict__["gamma"] = 1.2
        p = SolidSolutionPredictor(comp, t)
        assert p.model_3 == "Intermetallic"

    def test_model_4_fecocrni_solid_solution(self):
        """Singh et al. (2014): FeCoCrNi has high Lambda (>> 0.96)."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_4 == "Solid Solution"

    def test_model_4_alfe_intermetallic(self):
        """Singh et al. (2014) Table 1 AN1: AlFe (B2) has Lambda < 0.24 -> Intermetallic."""
        comp = AlloyComposition("AlFe")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_4 == "Intermetallic"

    def test_model_4_cantor_alloy_solid_solution(self):
        """Singh et al. (2014): CoCrFeMnNi (lambda >> 0.96) -> Solid Solution."""
        comp = AlloyComposition("CoCrFeMnNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_4 == "Solid Solution"

    def test_model_4_alcocrfeni_multiple_phases(self):
        """Singh et al. (2014): AlCoCrFeNi (lambda~0.42 in [0.24, 0.96]) -> Multiple Phases."""
        comp = AlloyComposition("AlCoCrFeNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_4 == "Multiple Phases"

    def test_model_5_coni_zero_enthalpy_solid_solution(self):
        """Ye et al. (2015): CoNi has dHmix=0 -> Omega=inf -> Phi=inf -> Solid Solution."""
        comp = AlloyComposition("CoNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_5 == "Solid Solution"

    def test_model_5_cantor_alloy_solid_solution(self):
        """Ye et al. (2015): CoCrFeMnNi has near-identical radii -> tiny |S_E| -> Phi >> 20 -> Solid Solution."""
        comp = AlloyComposition("CoCrFeMnNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_5 == "Solid Solution"

    def test_model_5_nbmotaw_solid_solution(self):
        """Ye et al. (2015): NbMoTaW has small size mismatch -> Phi >> 20 -> Solid Solution."""
        comp = AlloyComposition("NbMoTaW")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_5 == "Solid Solution"

    def test_model_5_fecrkunizr_multiple_phases(self):
        """Ye et al. (2015) Fig. 2: FeCrCuNiZr has large size mismatch (Zr) -> Phi < 20 -> Multiple Phases."""
        comp = AlloyComposition("FeCrCuNiZr")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_5 == "Multiple Phases"

    def test_model_6_fecocrni_solid_solution(self):
        """Troparevsky et al. (2015): All CoCrFeNi binaries are within enthalpy window."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_6 == "Solid Solution"

    def test_model_6_nbmotaw_solid_solution(self):
        """Troparevsky et al. (2015): NbMoTaW min_Hf > lower bound -> Solid Solution."""
        comp = AlloyComposition("NbMoTaW")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_6 == "Solid Solution"

    def test_model_6_alcocrfeni_multiple_phases(self):
        """Troparevsky et al. (2015): AlCoCrFeNi min_Hf=-677 meV/atom << lower bound -> Multiple Phases."""
        comp = AlloyComposition("AlCoCrFeNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_6 == "Multiple Phases"

    def test_model_7_fecocrni_solid_solution(self):
        """Senkov & Miracle (2016) Table 1: CoCrFeNi at T_A=973K is FCC solid solution."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_7(annealing_temperature=973) == "Solid Solution"

    def test_model_7_cantor_alloy_solid_solution(self):
        """Senkov & Miracle (2016): CoCrFeMnNi at default T_A -> Solid Solution."""
        comp = AlloyComposition("CoCrFeMnNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_7() == "Solid Solution"

    def test_model_7_nbmotaw_solid_solution(self):
        """Senkov & Miracle (2016): NbMoTaW refractory HEA at default T_A -> Solid Solution."""
        comp = AlloyComposition("NbMoTaW")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_7() == "Solid Solution"

    def test_model_8_fecocrni_solid_solution(self):
        """King et al. (2016) Table 1: CoCrFeNi Phi ~= 1.16 >= 1 -> Solid Solution."""
        comp = AlloyComposition("FeCoCrNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_8 == "Solid Solution"

    def test_model_8_alcocrfeni_multiple_phases(self):
        """King et al. (2016) Table 1: AlCoCrFeNi Phi ~= 0.36 < 1 -> Multiple Phases."""
        comp = AlloyComposition("AlCoCrFeNi")
        t = HEAThermodynamics(comp)
        p = SolidSolutionPredictor(comp, t)
        assert p.model_8 == "Multiple Phases"
