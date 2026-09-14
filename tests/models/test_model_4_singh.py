"""Model 4 against Singh et al., Intermetallics 53 (2014) 112-119, Table 1."""

import pytest
from published_data import SINGH_2014_TABLE_1 as TABLE

NOT_SOLID_SOLUTION = ("B2", "C", "L", "L12", "sigma", "tet")


def is_solid_solution(phases):
    """Return whether a phase string in this table names a solid solution only.

    Args:
        phases: Phase codes as printed.

    Returns:
        True when every code is a disordered solid solution.
    """
    return not any(code in NOT_SOLID_SOLUTION for code in phases.replace("+", " ").split())


def test_table_coverage():
    """The transcribed table is intact."""
    assert len(TABLE) == 61


@pytest.mark.parametrize(
    "formula,lambda_paper,delta_paper",
    [("MnCoCrFeNi", 1.251, 3.27), ("CrCuMnNi", 1.077, 3.27), ("CuCoFeNiV", 2.755, 2.20), ("AlFe", 0.113, 7.15)],
)
def test_named_alloys(thermo, formula, lambda_paper, delta_paper):
    """Four alloys from the table are reproduced."""
    calculated = thermo(formula)
    assert calculated.lambda_ == pytest.approx(lambda_paper, rel=0.02)
    assert calculated.atomic_size_difference == pytest.approx(delta_paper, abs=0.0055)


def test_delta_reproduces_table(thermo, assert_median_error):
    """Delta reproduces the published column to within rounding."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).atomic_size_difference,
        lambda row: row["delta"],
        below=0.02,
        rows_compared=61,
        worst=0.45,
    )


def test_delta_uses_atomic_radius(thermo, median_error):
    """Singh's deltas come from ``atomic_radius``."""
    published = lambda row: row["delta"]  # noqa: E731
    plain = median_error(TABLE, lambda row: thermo(row["formula"]).atomic_size_difference, published)
    cn12 = median_error(TABLE, lambda row: thermo(row["formula"]).atomic_size_difference_cn12, published)
    assert plain * 20 < cn12


def test_lambda_reproduces_table(thermo, assert_median_error):
    """Lambda tracks the published column."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).lambda_,
        lambda row: row["lambda"],
        below=0.5,
        relative=True,
    )


def test_classification_accuracy(predictor, assert_classification):
    """The criterion reproduces the reported phases."""
    assert_classification(
        TABLE,
        predict=lambda row: predictor(row["formula"]).model_4,
        expected=lambda row: is_solid_solution(row["phases"]),
        overall=0.95,
        solid_solution=0.90,
        intermetallic=0.95,
    )
