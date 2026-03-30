"""Validation of model predictions and printed parameters against the model papers."""

import pytest

from HEACalculator.core.composition import AlloyComposition
from HEACalculator.core.models import SolidSolutionPredictor
from HEACalculator.core.thermodynamics import GAS_CONSTANT, HEAThermodynamics


def _thermo_and_predictor(formula: str) -> tuple[HEAThermodynamics, SolidSolutionPredictor]:
    """Build thermodynamics and predictor objects for a validation formula."""
    composition = AlloyComposition(formula)
    thermodynamics = HEAThermodynamics(composition)
    return thermodynamics, SolidSolutionPredictor(composition, thermodynamics)


MODEL_1_CASES = [
    ("CoCrFeNi", "Solid Solution"),
    ("CoCrFeMnNi", "Solid Solution"),
    ("NbMoTaW", "Solid Solution"),
    ("FeCoNiCu", "Solid Solution"),
    ("CrMnFeCoNiCu", "Solid Solution"),
    ("TiZrHfNb", "Solid Solution"),
    ("NbMoTaWV", "Solid Solution"),
    ("CrFeNi", "Solid Solution"),
    ("VCrFeCoNi", "Solid Solution"),
    ("MoNbTaV", "Solid Solution"),
    ("AlNi", "Intermetallic"),
    ("AlFe", "Intermetallic"),
    ("AlCo", "Intermetallic"),
    ("CuZr", "Intermetallic"),
    ("NiTi", "Intermetallic"),
    ("AlTi", "Intermetallic"),
    ("CoZr", "Intermetallic"),
    ("NiZr", "Intermetallic"),
    ("FeZr", "Intermetallic"),
    ("NiHf", "Intermetallic"),
]

MODEL_1_PARAMS = [
    ("CoCrFeNi", 5.71, 1.06),
    ("CoCrFeNiCu", 7.36, 1.07),
    ("AlCoCrFeNi", 1.83, 5.25),
    ("CuNi", 2.22, 1.63),
    ("CoCrFeMnNi", 5.758, 1.122),
    ("NbMoTaW", 5.577, 2.456),
    ("NbMoTaWV", 8.502, 3.282),
    ("CrFeNi", 3.880, 1.296),
    ("VCrFeCoNi", 2.866, 2.791),
    ("FeCoNiCu", 3.838, 1.176),
    ("MoNbTaV", 9.806, 3.588),
    ("CrMnFeCoNiCu", 17.719, 1.180),
    ("TiZrHfNb", 10.724, 4.261),
    ("TiNbMoW", 5.891, 2.639),
    ("AlNi", 0.348, 7.116),
    ("AlFe", 0.718, 6.320),
    ("AlCo", 0.410, 6.716),
    ("CuZr", 0.436, 11.111),
    ("NiTi", 0.301, 8.487),
    ("FeCrCuNiZr", 1.701, 10.122),
]


class TestModel1YangZhang2012:
    """Validation tests for Model 1 against Yang and Zhang (2012)."""

    @pytest.mark.parametrize("formula,expected", MODEL_1_CASES, ids=[case[0] for case in MODEL_1_CASES])
    def test_prediction(self, formula, expected):
        """The model 1 classifier matches the published phase prediction."""
        _, predictor = _thermo_and_predictor(formula)
        assert predictor.model_1 == expected

    @pytest.mark.parametrize("formula,omega_paper,delta_paper", MODEL_1_PARAMS, ids=[case[0] for case in MODEL_1_PARAMS])
    def test_parameters(self, formula, omega_paper, delta_paper):
        """The calculated omega and delta values stay close to the paper data."""
        thermodynamics, _ = _thermo_and_predictor(formula)
        assert thermodynamics.omega == pytest.approx(omega_paper, rel=0.02)
        assert thermodynamics.atomic_size_difference == pytest.approx(delta_paper, abs=0.25)


MODEL_2_CASES = [
    ("CoCrFeNi", "Solid Solution"),
    ("CoCrFeMnNi", "Solid Solution"),
    ("NbMoTaW", "Solid Solution"),
    ("TiNbMoW", "Solid Solution"),
    ("CrFeNi", "Solid Solution"),
    ("TiZrHfNb", "Solid Solution"),
    ("NbMoTaWV", "Solid Solution"),
    ("CrMnFeCoNiCu", "Solid Solution"),
    ("VCrFeCoNi", "Solid Solution"),
    ("MoNbTaV", "Solid Solution"),
    ("AlNi", "Intermetallic"),
    ("AlCo", "Intermetallic"),
    ("CuZr", "Intermetallic"),
    ("NiZr", "Intermetallic"),
    ("CoZr", "Intermetallic"),
    ("FeZr", "Intermetallic"),
    ("NiTi", "Intermetallic"),
    ("AlTi", "Intermetallic"),
    ("AlCoCrFeNi", "Intermetallic"),
    ("CuNiZr", "Intermetallic"),
]

MODEL_2_PARAMS = [
    ("NbMoTaW", -6.50, 2.31),
    ("NbMoTaWV", -4.64, 3.15),
    ("CoCrFeNi", -3.75, 1.06),
    ("CoCrFeMnNi", -4.16, 1.122),
    ("TiNbMoW", -5.50, 2.639),
    ("CrFeNi", -4.44, 1.296),
    ("VCrFeCoNi", -8.96, 2.791),
    ("FeCoNiCu", 5.00, 1.176),
    ("MoNbTaV", -3.25, 3.588),
    ("CrMnFeCoNiCu", 1.44, 1.180),
    ("TiZrHfNb", 2.50, 4.261),
    ("AlNi", -22.00, 7.116),
    ("AlFe", -11.00, 6.320),
    ("AlCo", -19.00, 6.716),
    ("CuZr", -23.00, 11.111),
    ("NiTi", -35.00, 8.487),
    ("CoZr", -41.00, 12.281),
    ("NiZr", -49.00, 12.676),
    ("FeZr", -25.00, 11.888),
    ("FeCrCuNiZr", -14.40, 10.122),
]


class TestModel2Guo2013:
    """Validation tests for Model 2 against Guo et al. (2013)."""

    @pytest.mark.parametrize("formula,expected", MODEL_2_CASES, ids=[case[0] for case in MODEL_2_CASES])
    def test_prediction(self, formula, expected):
        """The model 2 classifier matches the published phase prediction."""
        _, predictor = _thermo_and_predictor(formula)
        assert predictor.model_2 == expected

    @pytest.mark.parametrize(
        "formula,mixing_enthalpy_paper,delta_paper", MODEL_2_PARAMS, ids=[case[0] for case in MODEL_2_PARAMS]
    )
    def test_parameters(self, formula, mixing_enthalpy_paper, delta_paper):
        """The calculated mixing enthalpy and delta values stay close to the paper data."""
        thermodynamics, _ = _thermo_and_predictor(formula)
        assert thermodynamics.mixing_enthalpy == pytest.approx(mixing_enthalpy_paper, rel=0.02)
        assert thermodynamics.atomic_size_difference == pytest.approx(delta_paper, abs=0.25)


MODEL_3_CASES = [
    ("CoCrFeNi", "Solid Solution"),
    ("CoCrFeMnNi", "Solid Solution"),
    ("NbMoTaW", "Solid Solution"),
    ("FeCoNiCu", "Solid Solution"),
    ("CrFeNi", "Solid Solution"),
    ("VCrFeCoNi", "Solid Solution"),
    ("MoNbTaV", "Solid Solution"),
    ("NbMoTaWV", "Solid Solution"),
    ("CrMnFeCoNiCu", "Solid Solution"),
    ("TiNbMoW", "Solid Solution"),
    ("FeCrCuNiZr", "Intermetallic"),
    ("CuZr", "Intermetallic"),
    ("NiZr", "Intermetallic"),
    ("CoZr", "Intermetallic"),
    ("FeZr", "Intermetallic"),
    ("CrZr", "Intermetallic"),
    ("NiHf", "Intermetallic"),
    ("TiZrAlNi", "Intermetallic"),
    ("AlCoCrFeNiZr", "Intermetallic"),
    ("NbZrAlNi", "Intermetallic"),
]


class TestModel3Wang2015:
    """Validation tests for Model 3 against Wang et al. (2015)."""

    @pytest.mark.parametrize("formula,expected", MODEL_3_CASES, ids=[case[0] for case in MODEL_3_CASES])
    def test_prediction(self, formula, expected):
        """The model 3 classifier matches the published phase prediction."""
        _, predictor = _thermo_and_predictor(formula)
        assert predictor.model_3 == expected


MODEL_4_CASES = [
    ("CoCrFeNi", "Solid Solution"),
    ("CoCrFeMnNi", "Solid Solution"),
    ("NbMoTaW", "Solid Solution"),
    ("FeCoNiCu", "Solid Solution"),
    ("CrFeNi", "Solid Solution"),
    ("NbMoTaWV", "Solid Solution"),
    ("VCrFeCoNi", "Solid Solution"),
    ("CrMnFeCoNiCu", "Solid Solution"),
    ("AlCoCrFeNi", "Multiple Phases"),
    ("AlCrFeNi", "Multiple Phases"),
    ("AlCoCrFe", "Multiple Phases"),
    ("TiCrFeCoNi", "Multiple Phases"),
    ("MoNbTaV", "Multiple Phases"),
    ("AlFe", "Intermetallic"),
    ("AlNi", "Intermetallic"),
    ("AlCo", "Intermetallic"),
    ("CuZr", "Intermetallic"),
    ("NiZr", "Intermetallic"),
    ("CoZr", "Intermetallic"),
    ("FeZr", "Intermetallic"),
]

MODEL_4_PARAMS = [
    ("CoCrFeMnNi", 1.251, 3.27),
    ("CrCuMnNi", 1.077, 3.27),
    ("CuCoFeNiV", 2.755, 2.20),
    ("AlFe", 0.113, 7.15),
]


class TestModel4Singh2014:
    """Validation tests for Model 4 against Singh et al. (2014)."""

    @pytest.mark.parametrize("formula,expected", MODEL_4_CASES, ids=[case[0] for case in MODEL_4_CASES])
    def test_prediction(self, formula, expected):
        """The model 4 classifier matches the published phase prediction."""
        _, predictor = _thermo_and_predictor(formula)
        assert predictor.model_4 == expected

    @pytest.mark.parametrize("formula,lambda_paper,delta_cn12_paper", MODEL_4_PARAMS, ids=[case[0] for case in MODEL_4_PARAMS])
    def test_parameters(self, formula, lambda_paper, delta_cn12_paper):
        """The calculated lambda and CN12 delta values stay close to the paper data."""
        thermodynamics, _ = _thermo_and_predictor(formula)
        assert thermodynamics.lambda_ == pytest.approx(lambda_paper, rel=0.02)
        assert thermodynamics.atomic_size_difference_cn12 == pytest.approx(delta_cn12_paper, abs=0.0055)


MODEL_5_CASES = [
    ("CoCrCu0.5FeNi", "Solid Solution"),
    ("NbMoTaW", "Solid Solution"),
    ("NbMoTaWV", "Solid Solution"),
    ("Al0.3CoCrFeNi", "Solid Solution"),
    ("Al0.5CrCuFeNi2", "Solid Solution"),
    ("AlCo3CrCu0.5FeNi", "Multiple Phases"),
    ("CoCrFeNiAlNb0.25", "Multiple Phases"),
]

MODEL_5_PARAMS = [
    ("CoCrCu0.5FeNi", 1.5811, 631.245),
    ("NbMoTaW", 1.3863, 60.085),
    ("NbMoTaWV", 1.6094, 40.860),
    ("Al0.3CoCrFeNi", 1.5426, 19.450),
    ("Al0.5CrCuFeNi2", 1.5157, 20.280),
    ("FeNi2CrCuAl0.6", 1.5299, 17.200),
    ("AlCo3CrCu0.5FeNi", 1.6217, 12.170),
]


class TestModel5Ye2015:
    """Validation tests for Model 5 against Ye et al. (2015)."""

    @pytest.mark.parametrize("formula,expected", MODEL_5_CASES, ids=[case[0] for case in MODEL_5_CASES])
    def test_prediction(self, formula, expected):
        """The model 5 classifier matches the published phase prediction."""
        _, predictor = _thermo_and_predictor(formula)
        assert predictor.model_5 == expected

    @pytest.mark.parametrize("formula,sc_over_kb_paper,phi_paper", MODEL_5_PARAMS, ids=[case[0] for case in MODEL_5_PARAMS])
    def test_parameters(self, formula, sc_over_kb_paper, phi_paper):
        """The calculated entropy and phi values stay close to the paper data."""
        thermodynamics, _ = _thermo_and_predictor(formula)
        assert thermodynamics.mixing_entropy / GAS_CONSTANT == pytest.approx(sc_over_kb_paper, abs=6e-5)
        assert thermodynamics.phi == pytest.approx(phi_paper, rel=0.12)


MODEL_6_CASES = [
    ("CrMnFeCoNi", "Solid Solution"),
    ("CrPdFeCoNi", "Solid Solution"),
    ("CrMnPdFeCoNi", "Multiple Phases"),
    ("CrMnFeTiNi", "Multiple Phases"),
    ("MoMnFeCoNi", "Multiple Phases"),
    ("VMnFeCoNi", "Multiple Phases"),
    ("CrMnVCoNi", "Multiple Phases"),
    ("CrMnFeCoCu", "Multiple Phases"),
    ("NbMoTaW", "Solid Solution"),
    ("VNbMoTaW", "Solid Solution"),
    ("AlCrFeCoNiCu", "Multiple Phases"),
]

MODEL_6_PARAMS = [
    ("CrMnFeCoNi", -115.0),
    ("NbMoTaW", -193.0),
    ("AlCrFeCoNiCu", -677.0),
]


class TestModel6Troparevsky2015:
    """Validation tests for Model 6 against Troparevsky et al. (2015)."""

    @pytest.mark.parametrize("formula,expected", MODEL_6_CASES, ids=[case[0] for case in MODEL_6_CASES])
    def test_prediction(self, formula, expected):
        """The model 6 classifier matches the published phase prediction."""
        _, predictor = _thermo_and_predictor(formula)
        assert predictor.model_6 == expected

    @pytest.mark.parametrize("formula,min_formation_enthalpy_paper", MODEL_6_PARAMS, ids=[case[0] for case in MODEL_6_PARAMS])
    def test_parameters(self, formula, min_formation_enthalpy_paper):
        """The calculated minimum formation enthalpy stays close to the paper data."""
        thermodynamics, _ = _thermo_and_predictor(formula)
        assert thermodynamics.min_formation_enthalpy == pytest.approx(min_formation_enthalpy_paper, abs=0.1)


MODEL_7_CASES = [
    ("CoCrFeNi", 573, "Solid Solution"),
    ("CoCrFeMnNi", 1273, "Solid Solution"),
    ("CoCr2FeNi", 1273, "Solid Solution"),
    ("Cu0.5CoCrFeNi", 1273, "Solid Solution"),
    ("HfNbTaTiZr", 1473, "Solid Solution"),
    ("MoNbTaW", 1673, "Solid Solution"),
    ("Al0.5CrFeNiTiV", 973, "Intermetallic"),
    ("CoFeMnMoNi", 973, "Intermetallic"),
]

MODEL_7_PARAMS = [
    ("CoCrFeNi", 573, 1.35, 1.70),
    ("CoCrFeMnNi", 1273, 1.64, 2.63),
    ("CoCr2FeNi", 1273, 0.85, 2.27),
    ("Cu0.5CoCrFeNi", 1273, -3.73, 14.03),
    ("HfNbTaTiZr", 1473, 0.89, 3.97),
    ("MoNbTaW", 1673, 1.94, 2.16),
    ("Al0.5CrFeNiTiV", 973, 1.79, 1.24),
    ("CoFeMnMoNi", 973, 4.17, 2.31),
]


class TestModel7SenkovMiracle2016:
    """Validation tests for Model 7 against Senkov and Miracle (2016)."""

    @pytest.mark.parametrize(
        "formula,annealing_temperature,expected",
        MODEL_7_CASES,
        ids=[case[0] for case in MODEL_7_CASES],
    )
    def test_prediction(self, formula, annealing_temperature, expected):
        """The model 7 classifier matches the published phase prediction."""
        thermodynamics, predictor = _thermo_and_predictor(formula)
        assert predictor.model_7(annealing_temperature=annealing_temperature) == expected

    @pytest.mark.parametrize(
        "formula,annealing_temperature,k1_paper,k1_critical_paper",
        MODEL_7_PARAMS,
        ids=[case[0] for case in MODEL_7_PARAMS],
    )
    def test_parameters(self, formula, annealing_temperature, k1_paper, k1_critical_paper):
        """The calculated model 7 parameters stay close to the paper data."""
        thermodynamics, predictor = _thermo_and_predictor(formula)
        assert predictor.model_7_k1() == pytest.approx(k1_paper, rel=0.055)
        assert predictor.model_7_k1_critical(annealing_temperature=annealing_temperature) == pytest.approx(
            k1_critical_paper,
            rel=0.055,
        )


MODEL_8_CASES = [
    ("NbHfTiZr", "Solid Solution"),
    ("NbTiVZr", "Solid Solution"),
    ("CoCrFeMnNi", "Solid Solution"),
    ("CoFeNi", "Solid Solution"),
    ("MoNbTaW", "Solid Solution"),
    ("CoCrFeNi", "Solid Solution"),
    ("MoNbTiZr", "Solid Solution"),
    ("MoNbTiVZr", "Solid Solution"),
    ("Mo0.3CoCrFeNi", "Solid Solution"),
    ("CoCrFeMo0.22Ni", "Solid Solution"),
    ("MoNbTaVW", "Solid Solution"),
    ("NbTaTiHfZr", "Solid Solution"),
    ("CoCrCuFeNi", "Multiple Phases"),
    ("AlCoCrFeNi", "Multiple Phases"),
]

MODEL_8_PARAMS = [
    ("CoCrFeNi", -23.43, -20.16, 1.16),
    ("CoCrCuFeNi", -21.08, 38.28, 0.55),
    ("AlCoCrFeNi", -33.89, -94.66, 0.36),
]


class TestModel8King2016:
    """Validation tests for Model 8 against King et al. (2016)."""

    @pytest.mark.parametrize("formula,expected", MODEL_8_CASES, ids=[case[0] for case in MODEL_8_CASES])
    def test_prediction(self, formula, expected):
        """The model 8 classifier matches the published phase prediction."""
        _, predictor = _thermo_and_predictor(formula)
        assert predictor.model_8 == expected

    @pytest.mark.parametrize(
        "formula,delta_g_ss_paper,delta_g_max_paper,f_parameter_paper",
        MODEL_8_PARAMS,
        ids=[case[0] for case in MODEL_8_PARAMS],
    )
    def test_parameters(self, formula, delta_g_ss_paper, delta_g_max_paper, f_parameter_paper):
        """The calculated Gibbs-energy terms stay close to the paper data."""
        thermodynamics, _ = _thermo_and_predictor(formula)
        assert thermodynamics.delta_g_ss == pytest.approx(delta_g_ss_paper, rel=0.02)
        assert thermodynamics.delta_g_max == pytest.approx(delta_g_max_paper, rel=0.02)
        assert thermodynamics.f_parameter == pytest.approx(f_parameter_paper, abs=0.025)
