"""Model 6 against Troparevsky et al., Phys. Rev. X 5 (2015) 011041."""

import pytest

CASES = [
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

PARAMS = [
    ("CrMnFeCoNi", -115.0),
    ("NbMoTaW", -193.0),
    ("AlCrFeCoNiCu", -677.0),
]


@pytest.mark.parametrize("formula,expected", CASES, ids=[case[0] for case in CASES])
def test_prediction(predictor, formula, expected):
    """The model 6 classifier matches the published phase prediction."""
    assert predictor(formula).model_6 == expected


@pytest.mark.parametrize("formula,min_formation_enthalpy_paper", PARAMS, ids=[case[0] for case in PARAMS])
def test_parameters(thermo, formula, min_formation_enthalpy_paper):
    """The calculated minimum formation enthalpy matches the value quoted in the text."""
    assert thermo(formula).min_formation_enthalpy == pytest.approx(min_formation_enthalpy_paper, abs=0.1)
