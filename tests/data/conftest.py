"""Shared fixtures for data module tests."""

import pytest

from HEACalculator.data import Element


@pytest.fixture
def fe_element():
    """Return the Element record for iron (Fe).

    Returns:
        Dataclass instance for iron, as returned by ``Element("Fe")``.
    """
    return Element("Fe")


@pytest.fixture
def fe_co_pair():
    """Return a sorted (Fe, Co) pair tuple for pairwise lookup tests.

    Returns:
        Two-element tuple ``("Fe", "Co")`` for use with
            ``MixingEnthalpy``, ``MiedemaEnthalpy``, and related data functions.
    """
    return ("Fe", "Co")
