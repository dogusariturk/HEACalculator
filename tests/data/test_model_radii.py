"""Tests for the paper-specific model radius lookup tables."""

from HEACalculator.data import Element
from HEACalculator.data.model_radii import model_atomic_radius, model_atomic_radius_cn12


def test_kittel_paper_radius_set_uses_paper_values():
    """The Kittel radius table returns the published model values for supported elements."""
    assert model_atomic_radius("Al", Element("Al").atomic_radius) == 143.0
    assert model_atomic_radius("Co", Element("Co").atomic_radius) == 125.0
    assert model_atomic_radius("Cr", Element("Cr").atomic_radius) == 128.0
    assert model_atomic_radius("Fe", Element("Fe").atomic_radius) == 126.0
    assert model_atomic_radius("Ni", Element("Ni").atomic_radius) == 124.0
    assert model_atomic_radius("Ti", Element("Ti").atomic_radius) == 147.0
    assert model_atomic_radius("Zr", Element("Zr").atomic_radius) == 160.0


def test_smithells_paper_radius_set_reproduces_model_4_values():
    """The Smithells CN12 radius table reproduces the published model values."""
    assert model_atomic_radius_cn12("Al", Element("Al").atomic_radius_cn12) == 143.2
    assert model_atomic_radius_cn12("Co", Element("Co").atomic_radius_cn12) == 125.1
    assert model_atomic_radius_cn12("Cr", Element("Cr").atomic_radius_cn12) == 124.9
    assert model_atomic_radius_cn12("Fe", Element("Fe").atomic_radius_cn12) == 124.1
    assert model_atomic_radius_cn12("Mn", Element("Mn").atomic_radius_cn12) == 135.0
    assert model_atomic_radius_cn12("Ni", Element("Ni").atomic_radius_cn12) == 124.6
    assert model_atomic_radius_cn12("V", Element("V").atomic_radius_cn12) == 131.6


def test_model_radius_falls_back_to_element_database():
    """Missing paper overrides fall back to the element database values."""
    assert model_atomic_radius("Ag", Element("Ag").atomic_radius) == Element("Ag").atomic_radius
    assert model_atomic_radius_cn12("Ag", Element("Ag").atomic_radius_cn12) == Element("Ag").atomic_radius_cn12
