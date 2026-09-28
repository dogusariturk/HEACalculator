"""Model 2 against Guo et al., Intermetallics 41 (2013) 96-103, Table 1, and its radius source."""

from published_data import GUO_2013_TABLE_1 as TABLE
from published_data import GUO_LIU_2011_TABLES_2_3

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
        below=0.01,
        rows_compared=93,
        worst=0.30,
    )


#: Rows whose printed delta Guo and Liu's own Table 1 radii do not give (9.09 vs 7.48, 16.72 vs 12.17).
GUO_LIU_MISPRINTS = ("AlCrMoTaTiZr", "Ti40Zr25Cu12Ni3Be20")


def test_delta_reproduces_guo_liu_tables(thermo, assert_median_error):
    """``atomic_radius`` is Guo and Liu (2011) Table 1, so it reproduces the deltas they computed from it."""
    rows = tuple(row for row in GUO_LIU_2011_TABLES_2_3 if row["formula"] not in GUO_LIU_MISPRINTS)
    assert len(rows) == len(GUO_LIU_2011_TABLES_2_3) - 2
    assert_median_error(
        rows,
        lambda row: thermo(row["formula"]).atomic_size_difference,
        lambda row: row["delta"],
        below=0.01,
        rows_compared=149,
        worst=0.08,
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
        rows_compared=93,
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
