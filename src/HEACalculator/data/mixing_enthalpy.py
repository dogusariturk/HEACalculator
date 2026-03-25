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
        float: The pair mixing enthalpy in kJ/mol.

    Raises:
        TypeError: If the input is not a tuple or list.
        MissingMixingEnthalpyError: If the requested pair does not exist in the database.

    References:
        de Boer, F.R.; Pettifor, D.G. Cohesion in Metals. Elsevier Science Publishers B.V., Netherlands, 1988.
    """
    if not isinstance(pair, tuple | list):
        raise TypeError("Usage: MixingEnthalpy(('X', 'Y')) where X and Y are element names.")

    _pair = tuple(sorted(pair))
    if _pair not in _mixing_data:
        raise MissingMixingEnthalpyError(f"No mixing enthalpy data for pair {_pair}")

    return _mixing_data[_pair]
