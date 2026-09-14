"""Model 7 against Senkov and Miracle, J. Alloys Compd. 658 (2016) 603-607, Table 1."""

import pytest
from published_data import SENKOV_2016_TABLE_1 as TABLE

NOT_SOLID_SOLUTION = ("B2", "IM", "IMs", "sigma")


def is_solid_solution(phases):
    """Return whether a phase string in this table names a solid solution only.

    Args:
        phases: Phases as printed.

    Returns:
        True when no ordered, intermetallic or sigma phase is named.
    """
    return not any(code in NOT_SOLID_SOLUTION for code in phases.replace("+", " ").replace("/", " ").split())


def test_table_coverage():
    """The transcribed table is intact."""
    assert len(TABLE) == 45


@pytest.mark.parametrize(
    "formula,annealing_temperature,k1_paper,k1_critical_paper",
    [("CoCrFeNi", 573, 1.35, 1.70), ("CoCrFeMnNi", 1273, 1.64, 2.63), ("MoNbTaW", 1673, 1.94, 2.16)],
)
def test_named_alloys(predictor, formula, annealing_temperature, k1_paper, k1_critical_paper):
    """Three alloys from the table are reproduced."""
    calculated = predictor(formula)
    assert calculated.model_7_k1() == pytest.approx(k1_paper, rel=0.055)
    assert calculated.model_7_k1_critical(annealing_temperature=annealing_temperature) == pytest.approx(
        k1_critical_paper, rel=0.055
    )


def test_k1_reproduces_table(predictor, assert_median_error):
    """k1 tracks the published column."""
    assert_median_error(
        TABLE,
        lambda row: predictor(row["formula"]).model_7_k1(),
        lambda row: row["k1"],
        below=2.5,
        rows_compared=45,
        relative=True,
        floor=0.5,
    )


def test_critical_k1_reproduces_table(predictor, assert_median_error):
    """The critical k1 tracks the published column."""
    assert_median_error(
        TABLE,
        lambda row: predictor(row["formula"]).model_7_k1_critical(annealing_temperature=row["annealing_temperature"]),
        lambda row: row["k1_critical"],
        below=1.5,
        relative=True,
    )


def test_classification_accuracy(predictor, assert_classification):
    """The criterion reproduces the reported phases."""
    assert_classification(
        TABLE,
        predict=lambda row: predictor(row["formula"]).model_7(annealing_temperature=row["annealing_temperature"]),
        expected=lambda row: is_solid_solution(row["phases"]),
        overall=0.80,
        solid_solution=0.85,
        intermetallic=0.75,
    )
