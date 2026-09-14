"""Model 8 against King et al., Acta Mater. 104 (2016) 172-179, and its Table S1."""

import pytest
from published_data import KING_2016_TABLE_S1 as TABLE

WORKED_EXAMPLES = [
    ("CoCrFeNi", -23.43, -20.16, 1.16),
    ("CoCrCuFeNi", -21.08, 38.28, 0.55),
    ("AlCoCrFeNi", -33.89, -94.66, 0.36),
]


def test_table_coverage():
    """The transcribed table is intact."""
    assert len(TABLE) == 182


@pytest.mark.parametrize(
    "formula,delta_g_ss_paper,delta_g_max_paper,f_parameter_paper",
    WORKED_EXAMPLES,
    ids=[case[0] for case in WORKED_EXAMPLES],
)
def test_parameters(thermo, formula, delta_g_ss_paper, delta_g_max_paper, f_parameter_paper):
    """The paper's three worked examples are reproduced."""
    calculated = thermo(formula)
    assert calculated.delta_g_ss == pytest.approx(delta_g_ss_paper, rel=0.03)
    assert calculated.delta_g_max == pytest.approx(delta_g_max_paper, rel=0.02)
    assert calculated.f_parameter == pytest.approx(f_parameter_paper, abs=0.025)


def test_classification_accuracy(predictor, assert_classification):
    """The criterion reproduces the sections King sorts the alloys into."""
    assert_classification(
        TABLE,
        predict=lambda row: predictor(row["formula"]).model_8,
        expected=lambda row: {"Solid Solution": True, "Intermetallic/multiphase": False}.get(row["section"]),
        overall=0.95,
        solid_solution=0.90,
        intermetallic=0.95,
        rows_scored=150,
    )
