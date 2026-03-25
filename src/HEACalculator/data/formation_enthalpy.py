"""Binary pair formation enthalpy database backed by formation_enthalpy.json."""

import importlib.resources
import json

from HEACalculator.exceptions import MissingFormationEnthalpyError

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

_data_dir = importlib.resources.files("HEACalculator.data")
with (_data_dir / "formation_enthalpy.json").open() as _f:
    _raw = json.load(_f)

_formation_enthalpy_data = {tuple(k.split("-")): v for k, v in _raw.items()}


def FormationEnthalpy(pair: tuple[str, str] | list[str]) -> float:
    """Return the pair formation enthalpy of an element pair in meV/atom.

    Args:
        pair (tuple or list): The element pair, e.g. ``("Fe", "Co")``.

    Returns:
        float: The pair formation enthalpy in meV/atom.

    Raises:
        TypeError: If the input is not a tuple or list.
        MissingFormationEnthalpyError: If the requested pair does not exist in the database.

    References:
        Troparevsky, M.C.; Morris, J.R.; Kent, P.R.C.; Lupini, A.R.; Stocks, G.M. Phys. Rev. X 2015, 5(1), 011041.
    """
    if not isinstance(pair, tuple | list):
        raise TypeError("Usage: FormationEnthalpy(('X', 'Y')) where X and Y are element names.")

    _pair = tuple(sorted(pair))
    if _pair not in _formation_enthalpy_data:
        raise MissingFormationEnthalpyError(f"No formation enthalpy data for pair {_pair}")

    return _formation_enthalpy_data[_pair]
