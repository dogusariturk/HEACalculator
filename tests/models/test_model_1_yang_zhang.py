"""Model 1 against Yang and Zhang, Mater. Chem. Phys. 132 (2012) 233-238, Table 1."""

import pytest
from published_data import YANG_ZHANG_2012_TABLE_1 as TABLE

NOT_SOLID_SOLUTION = ("compound", "laves", "sigma", "boride", "ordered", "aucu", "mo5 si3", "cu2 y")


def is_solid_solution(structure):
    """Return whether a structure reported in this table is a solid solution only.

    Args:
        structure: Structure as printed.

    Returns:
        True when the structure names no compound or ordered phase.
    """
    return not any(word in structure.lower() for word in NOT_SOLID_SOLUTION)


def test_table_coverage():
    """The transcribed table is intact."""
    assert len(TABLE) == 129


@pytest.mark.parametrize(
    "formula,delta_paper,omega_paper",
    [("CoCrFeNi", 1.06, 5.71), ("CoCrFeNiCu", 1.07, 7.36), ("CoCrFeNiAl", 5.25, 1.83), ("CuNi", 1.63, 2.22)],
)
def test_named_alloys(thermo, formula, delta_paper, omega_paper):
    """Four alloys the paper reports are reproduced."""
    calculated = thermo(formula)
    assert calculated.atomic_size_difference_cn12 == pytest.approx(delta_paper, abs=0.25)
    assert calculated.omega == pytest.approx(omega_paper, rel=0.02)


def test_delta_reproduces_table(thermo, assert_median_error):
    """Delta tracks the published column."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).atomic_size_difference_cn12,
        lambda row: row["delta"],
        below=0.30,
        rows_compared=125,
    )


def test_delta_uses_cn12_radii(thermo, median_error):
    """Yang and Zhang's radii are the CN12 set, so that column must back this delta."""
    published = lambda row: row["delta"]  # noqa: E731
    cn12 = median_error(TABLE, lambda row: thermo(row["formula"]).atomic_size_difference_cn12, published)
    plain = median_error(TABLE, lambda row: thermo(row["formula"]).atomic_size_difference, published)
    assert cn12 < plain


def test_criterion_reads_the_cn12_delta(predictor_with_deltas):
    """The criterion reads the CN12 delta, not the plain one."""
    assert predictor_with_deltas("CoCrFeMnNi", plain=1.0, cn12=9.0).model_1 == "Intermetallic"
    assert predictor_with_deltas("CoCrFeMnNi", plain=9.0, cn12=1.0).model_1 == "Solid Solution"


def test_omega_reproduces_table(thermo, assert_median_error):
    """Omega tracks the published column."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).omega,
        lambda row: row["omega"],
        below=1.0,
        relative=True,
        floor=0.01,
    )


def test_mixing_enthalpy_reproduces_table(thermo, assert_median_error):
    """Mixing enthalpy tracks the published column."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).mixing_enthalpy,
        lambda row: row["enthalpy"],
        below=0.02,
    )


def test_classification_accuracy(predictor, assert_classification):
    """The criterion reproduces the reported structures."""
    assert_classification(
        TABLE,
        predict=lambda row: predictor(row["formula"]).model_1,
        expected=lambda row: is_solid_solution(row["structure"]),
        overall=0.75,
        solid_solution=0.90,
        intermetallic=0.35,
    )
