"""Element property database backed by elements.json."""

import importlib.resources
import json
from dataclasses import dataclass

from HEACalculator.exceptions import ElementNotFoundError

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

_data_dir = importlib.resources.files("HEACalculator.data")
with (_data_dir / "elements.json").open() as _f:
    _element_data = json.load(_f)


@dataclass(frozen=True)
class _Element:
    r"""Container for physical and chemical properties of a single element.

    Attributes:
        symbol: Chemical symbol.
        melting_point: Melting temperature in Kelvin.
        atomic_number: Atomic number.
        atomic_volume: Atomic volume in cm$^3$/mol.
        atomic_weight: Relative atomic weight.
        atomic_radius: Slater atomic radius in pm.
        atomic_radius_cn12: Goldschmidt CN12-corrected metallic radius in pm (NaN if unavailable).
        nvalence: Number of valence electrons.
        allen_electronegativity: Allen configuration energy in Pauling units (NaN if unavailable).
        pauling_electronegativity: Pauling electronegativity (NaN if unavailable).

    References:
        1. IUPAC-CIAAW. Standard atomic weights. [https://www.ciaaw.org/atomic-weights.htm](https://www.ciaaw.org/atomic-weights.htm).
        2. Slater, J.C. Atomic Radii in Crystals. J. Chem. Phys. 1964, 41(10), 3199.
        3. Smithells Metals Reference Book, 8th ed., Table 4.1 (Goldschmidt CN12 corrected).
        4. Mann, J.B.; Meek, T.L.; Allen, L.C. J. Am. Chem. Soc. 2000, 122, 2780-2783.
        5. Mann, J.B.; Meek, T.L.; Knight, E.T.; Capitani, J.F.; Allen, L.C. J. Am. Chem. Soc. 2000, 122, 5132-5137.
        6. Haynes, W.M. CRC Handbook of Chemistry and Physics, 95th ed.; CRC Press: London, 2014. ISBN 9781482208689.
    """

    symbol: str
    melting_point: float
    atomic_number: int
    atomic_volume: float
    atomic_weight: float
    atomic_radius: float
    atomic_radius_cn12: float
    nvalence: float
    allen_electronegativity: float
    pauling_electronegativity: float

    def __str__(self) -> str:
        """Return a human-readable summary of the element's properties.

        Returns:
            Multi-line summary of the stored element properties.
        """
        return (
            f"\n{self.symbol}\n"
            f"\tMelting point: {self.melting_point} K\n"
            f"\tAtomic number: {self.atomic_number}\n"
            f"\tAtomic volume: {self.atomic_volume} cm^3/mol\n"
            f"\tAtomic weight: {self.atomic_weight}\n"
            f"\tAtomic radius: {self.atomic_radius} pm\n"
            f"\tValence electrons: {self.nvalence}\n"
            f"\tAllen electronegativity: {self.allen_electronegativity}\n"
            f"\tPauling electronegativity: {self.pauling_electronegativity}\n"
        )


_elements: dict[str, _Element] = {
    name: _Element(
        symbol=name,
        melting_point=float(props["melting_point"]),
        atomic_number=props["atomic_number"],
        atomic_volume=float(props["atomic_volume"]),
        atomic_weight=props["atomic_weight"],
        atomic_radius=float(props["atomic_radius"]),
        atomic_radius_cn12=float(props["atomic_radius_cn12"]),
        nvalence=props["nvalence"],
        allen_electronegativity=float(props["allen_electronegativity"]),
        pauling_electronegativity=float(props["pauling_electronegativity"]),
    )
    for name, props in _element_data.items()
}


def Element(name: str) -> _Element:
    """Return an element object containing its physical and chemical properties.

    Args:
        name: The element symbol, e.g. ``"Fe"``.

    Returns:
        Frozen dataclass containing the element's properties.

    Raises:
        TypeError: If the input is not a string.
        ElementNotFoundError: If the requested element does not exist in the database.
    """
    if not isinstance(name, str):
        raise TypeError("Usage: Element(X) where X is the element name.")
    if name not in _elements:
        raise ElementNotFoundError(f"Element not found in database: '{name}'")
    return _elements[name]
