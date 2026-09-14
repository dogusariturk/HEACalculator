"""Model 3 against Wang et al., Scr. Mater. 94 (2015) 28-31."""

from published_data import GUO_2013_TABLE_1

CRYSTALLINE = tuple(row for row in GUO_2013_TABLE_1 if row["phase"] in ("SS", "IM"))


def test_classification_accuracy(predictor, assert_classification):
    """Gamma separates the solid solutions from the intermetallics in Guo's set."""
    assert_classification(
        CRYSTALLINE,
        predict=lambda row: predictor(row["formula"]).model_3,
        expected=lambda row: row["phase"] == "SS",
        overall=0.90,
        solid_solution=0.95,
        intermetallic=0.75,
    )
