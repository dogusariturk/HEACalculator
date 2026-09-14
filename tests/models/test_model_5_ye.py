"""Model 5 against Ye et al., Scr. Mater. 104 (2015) 53-55, Supplementary Table S1."""

import pytest
from published_data import YE_2015_TABLE_S1 as TABLE

from HEACalculator.core.thermodynamics import GAS_CONSTANT


def published_phi(row):
    """Return the mean of a row's two packing fractions, which is what the implementation reports.

    Args:
        row: One row of Ye's Table S1.

    Returns:
        Average of the published BCC and FCC phi values.
    """
    return (row["phi_bcc"] + row["phi_fcc"]) / 2


def test_table_coverage():
    """The transcribed table is intact."""
    assert len(TABLE) == 43


@pytest.mark.parametrize(
    "formula,entropy_paper,phi_paper",
    [("CoCrCu0.5FeNi", 1.5811, 631.245), ("WNbMoTa", 1.3863, 60.085), ("AlCo3CrCu0.5FeNi", 1.6217, 12.170)],
)
def test_named_alloys(thermo, formula, entropy_paper, phi_paper):
    """Phi is the mean of the paper's two packing fractions, as the implementation computes it."""
    calculated = thermo(formula)
    assert calculated.mixing_entropy / GAS_CONSTANT == pytest.approx(entropy_paper, abs=6e-5)
    assert calculated.phi == pytest.approx(phi_paper, rel=0.06)


def test_configurational_entropy_reproduces_table(thermo, assert_median_error):
    """Configurational entropy matches every published value."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).mixing_entropy / GAS_CONSTANT,
        lambda row: row["entropy"],
        below=0.001,
        rows_compared=43,
        worst=0.06,
    )


def test_phi_reproduces_table(thermo, assert_median_error):
    """Phi tracks the mean of the published BCC and FCC packing values."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).phi,
        published_phi,
        below=4.0,
        rows_compared=40,
        relative=True,
    )


def test_classification_accuracy(predictor, assert_classification):
    """The criterion reproduces the detected phases."""
    assert_classification(
        TABLE,
        predict=lambda row: predictor(row["formula"]).model_5,
        expected=lambda row: {"FCC": True, "BCC": True, "Multi-phase": False}.get(row["phase"]),
        overall=0.90,
        solid_solution=0.80,
        intermetallic=0.90,
        rows_scored=40,
    )
