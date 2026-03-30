"""Binary pair mixing enthalpy database backed by mixing_enthalpy.json."""

import importlib.resources
import json

from HEACalculator.exceptions import MissingMixingEnthalpyError

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

_data_dir = importlib.resources.files("HEACalculator.data")
with (_data_dir / "mixing_enthalpy.json").open() as _f:
    _raw = json.load(_f)

_mixing_data = {tuple(k.split("-")): v for k, v in _raw.items()}


def MixingEnthalpy(pair: tuple[str, str] | list[str]) -> float:
    """Return the pair mixing enthalpy of an element pair in kJ/mol.

    Args:
        pair (tuple or list): The element pair, e.g. ``("Fe", "Co")``.

    Returns:
        The pair mixing enthalpy in kJ/mol.

    Raises:
        TypeError: If the input is not a tuple or list.
        MissingMixingEnthalpyError: If the requested pair does not exist in the database.

    References:
        - Takeuchi, A.; Inoue, A. Classification of Bulk Metallic Glasses by Atomic Size Difference,
            Heat of Mixing and Period of Constituent Elements and Its Application to Characterization
            of the Main Alloying Element. Mater. Trans. 2005, 46(12), 2817-2829. Table 1.
    """
    if not isinstance(pair, tuple | list):
        raise TypeError("Usage: MixingEnthalpy(('X', 'Y')) where X and Y are element names.")

    _pair = tuple(sorted(pair))
    if _pair not in _mixing_data:
        raise MissingMixingEnthalpyError(f"No mixing enthalpy data for pair {_pair}")

    return _mixing_data[_pair]
