"""Smoke tests for the JSON-backed elements loader."""

import pytest

from HEACalculator.data import Element


class TestElementLoader:
    """Tests for the Element factory function and the JSON elements database."""

    def test_iron_atomic_weight(self, fe_element):
        """Iron's atomic weight is approximately 55.845 g/mol."""
        assert fe_element.atomic_weight == pytest.approx(55.845, abs=1e-2)

    def test_iron_melting_point(self, fe_element):
        """Iron's melting point is well above 1000 K."""
        assert fe_element.melting_point > 1000

    def test_iron_atomic_radius_positive(self, fe_element):
        """Iron's atomic radius is a strictly positive value."""
        assert fe_element.atomic_radius > 0

    def test_nickel_nvalence(self):
        """Nickel has 10 valence electrons (d-band metal)."""
        assert Element("Ni").nvalence == 10.0

    def test_missing_element_raises_key_error(self):
        """An unrecognized element symbol raises KeyError."""
        with pytest.raises(KeyError):
            Element("Xx")

    def test_invalid_input_raises_type_error(self):
        """A non-string input raises TypeError."""
        with pytest.raises(TypeError):
            Element(None)

    def test_all_118_elements_accessible(self):
        """The elements database contains exactly 118 entries."""
        from HEACalculator.data.elements import _element_data

        assert len(_element_data) == 118

    def test_iron_allen_electronegativity(self, fe_element):
        """Iron's Allen CE is 1.80 Pauling units (d-block paper, Table 4)."""
        assert fe_element.allen_electronegativity == pytest.approx(1.80, abs=1e-10)

    def test_nickel_allen_electronegativity(self):
        """Nickel's Allen CE is 1.88 Pauling units (d-block paper, Table 4)."""
        assert Element("Ni").allen_electronegativity == pytest.approx(1.88, abs=1e-10)

    def test_lanthanide_allen_electronegativity_is_nan(self):
        """La has no Allen CE data — value is NaN (lanthanides not covered by Allen papers)."""
        import math

        assert math.isnan(Element("La").allen_electronegativity)

    def test_actinide_allen_electronegativity_is_nan(self):
        """Ac has no Allen CE data — value is NaN (actinides not covered by Allen papers)."""
        import math

        assert math.isnan(Element("Ac").allen_electronegativity)
