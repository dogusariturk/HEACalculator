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

    def test_neodymium_symbol_is_available(self):
        """Neodymium is stored under its correct IUPAC symbol, Nd."""
        assert Element("Nd").atomic_number == 60.0

    def test_missing_element_raises_key_error(self):
        """An unrecognized element symbol raises KeyError."""
        with pytest.raises(KeyError):
            Element("Xx")

    def test_invalid_input_raises_type_error(self):
        """A non-string input raises TypeError."""
        with pytest.raises(TypeError):
            Element(None)  # ty: ignore[invalid-argument-type]

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

    def test_lowercase_symbol_raises_element_not_found_error(self):
        """A lowercase element symbol raises ElementNotFoundError (symbols are case-sensitive)."""
        from HEACalculator.exceptions import ElementNotFoundError

        with pytest.raises(ElementNotFoundError):
            Element("fe")

    def test_symbol_with_leading_space_raises_element_not_found_error(self):
        """An element symbol with leading whitespace raises ElementNotFoundError."""
        from HEACalculator.exceptions import ElementNotFoundError

        with pytest.raises(ElementNotFoundError):
            Element(" Fe")

    def test_element_str_contains_symbol(self):
        """The __str__ representation of an element includes its chemical symbol."""
        assert "Fe" in str(Element("Fe"))

    def test_element_str_contains_melting_point(self):
        """The __str__ representation includes the melting point label."""
        assert "Melting point" in str(Element("Fe"))

    def test_element_str_contains_allen_electronegativity(self):
        """The __str__ representation includes the Allen electronegativity label."""
        assert "Allen electronegativity" in str(Element("Fe"))


class TestElementFieldValues:
    """Tests for specific numeric field values and NaN handling."""

    def test_iron_pauling_electronegativity(self, fe_element):
        """Iron's Pauling electronegativity is 1.83 (CRC Handbook 95th ed.)."""
        assert fe_element.pauling_electronegativity == pytest.approx(1.83, abs=1e-2)

    def test_iron_atomic_number(self, fe_element):
        """Iron has atomic number 26."""
        assert fe_element.atomic_number == 26

    def test_iron_ea(self, fe_element):
        """Iron has 2 outer s+p electrons (4s^2, no outer p)."""
        assert fe_element.ea == pytest.approx(2.0)

    def test_iron_atomic_volume_positive(self, fe_element):
        """Iron's atomic volume is strictly positive."""
        assert fe_element.atomic_volume > 0

    def test_iron_atomic_radius_cn12_positive(self, fe_element):
        """Iron's CN12 radius is a finite positive value."""
        import math

        assert math.isfinite(fe_element.atomic_radius_cn12)
        assert fe_element.atomic_radius_cn12 > 0

    def test_iron_nvalence(self, fe_element):
        """Iron has 8 valence electrons (3d^6 + 4s^2)."""
        assert fe_element.nvalence == 8.0

    def test_noble_gas_ea_is_nan(self):
        """Noble gas (Ar) has no Hume-Rothery e/a — value is NaN."""
        import math

        assert math.isnan(Element("Ar").ea)

    def test_noble_gas_pauling_electronegativity_is_nan(self):
        """Noble gas (He) has no Pauling electronegativity — value is NaN."""
        import math

        assert math.isnan(Element("He").pauling_electronegativity)

    def test_noble_gas_cn12_radius_is_nan(self):
        """Noble gas (He) has no metallic CN12 radius — value is NaN."""
        import math

        assert math.isnan(Element("He").atomic_radius_cn12)

    def test_element_is_immutable(self, fe_element):
        """Frozen dataclass raises an error when an attribute assignment is attempted."""
        with pytest.raises((AttributeError, TypeError)):
            fe_element.symbol = "X"  # type: ignore[misc]
