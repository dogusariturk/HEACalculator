"""Model 2 against Guo et al., Intermetallics 41 (2013) 96-103, Table 1."""

from published_data import GUO_2013_TABLE_1 as TABLE

CRYSTALLINE = tuple(row for row in TABLE if row["phase"] in ("SS", "IM"))


def test_table_coverage():
    """The transcribed table is intact."""
    assert len(TABLE) == 93
    assert len(CRYSTALLINE) == 82


def test_delta_reproduces_table(thermo, assert_median_error):
    """Delta reproduces the published column to within rounding."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).atomic_size_difference,
        lambda row: row["delta"],
        below=0.02,
        rows_compared=85,
        worst=0.30,
    )


def test_delta_uses_atomic_radius(thermo, median_error):
    """Guo's deltas come from ``atomic_radius``."""
    published = lambda row: row["delta"]  # noqa: E731
    plain = median_error(TABLE, lambda row: thermo(row["formula"]).atomic_size_difference, published)
    cn12 = median_error(TABLE, lambda row: thermo(row["formula"]).atomic_size_difference_cn12, published)
    assert plain * 20 < cn12


def test_criterion_reads_the_plain_delta(predictor_with_deltas):
    """The criterion reads the plain delta, not the CN12 one."""
    assert predictor_with_deltas("CoCrFeMnNi", plain=9.0, cn12=1.0).model_2 == "Intermetallic"
    assert predictor_with_deltas("CoCrFeMnNi", plain=1.0, cn12=9.0).model_2 == "Solid Solution"


def test_mixing_enthalpy_reproduces_table(thermo, assert_median_error):
    """Mixing enthalpy reproduces the published column to within rounding."""
    assert_median_error(
        TABLE,
        lambda row: thermo(row["formula"]).mixing_enthalpy,
        lambda row: row["enthalpy"],
        below=0.02,
    )


def test_classification_accuracy(predictor, assert_classification):
    """The criterion reproduces the published labels."""
    assert_classification(
        CRYSTALLINE,
        predict=lambda row: predictor(row["formula"]).model_2,
        expected=lambda row: row["phase"] == "SS",
        overall=0.85,
        solid_solution=0.90,
        intermetallic=0.55,
    )
