"""Shared fixtures for core module tests.

Provides a fixture chain built on the FeCoCrNi reference alloy:
``composition`` -> ``thermodynamics`` -> ``predictor``.
A standalone ``calculator`` fixture and a ``batch_calculator`` fixture
for converter tests are also provided.
"""

import pytest

from HEACalculator.core.composition import AlloyComposition
from HEACalculator.core.converter import BatchCalculator
from HEACalculator.core.hea import HEACalculator
from HEACalculator.core.models import SolidSolutionPredictor
from HEACalculator.core.thermodynamics import HEAThermodynamics

_FECOCRNI = "FeCoCrNi"
_CONVERTER_ELEMENTS = {"Al": 35.00, "Ti": 35.00, "V": 20.00, "Cr": 5.00, "Mn": 5.0}


@pytest.fixture
def composition():
    """Return an AlloyComposition for the FeCoCrNi reference alloy."""
    return AlloyComposition(_FECOCRNI)


@pytest.fixture
def thermodynamics(composition):
    """Return an HEAThermodynamics instance for the FeCoCrNi reference alloy."""
    return HEAThermodynamics(composition)


@pytest.fixture
def predictor(composition, thermodynamics):
    """Return a SolidSolutionPredictor for the FeCoCrNi reference alloy."""
    return SolidSolutionPredictor(composition, thermodynamics)


@pytest.fixture
def calculator():
    """Return a fully calculated HEACalculator for the FeCoCrNi reference alloy."""
    return HEACalculator(_FECOCRNI)


@pytest.fixture
def batch_calculator():
    """Return a BatchCalculator for a five-element Al-Ti-V-Cr-Mn alloy."""
    return BatchCalculator(_CONVERTER_ELEMENTS)
