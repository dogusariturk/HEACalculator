"""Paper-facing radius tables used by the solid-solution models."""

from __future__ import annotations

import importlib.resources
import json

_data_dir = importlib.resources.files("HEACalculator.data")
with (_data_dir / "model_radii.json").open() as _f:
    _model_radii = json.load(_f)

_KITTEL_RADII = _model_radii["kittel_paper_set_pm"]
_SMITHELLS_RADII = _model_radii["smithells_paper_set_pm"]


def model_atomic_radius(symbol: str, default: float) -> float:
    """Return the paper-specific atomic radius for *symbol*, falling back to *default*.

    Returns:
        Paper override for the atomic radius in pm, or ``default`` when unavailable.
    """
    return float(_KITTEL_RADII.get(symbol, default))


def model_atomic_radius_cn12(symbol: str, default: float) -> float:
    """Return the paper-specific CN12 atomic radius for *symbol*, falling back to *default*.

    Returns:
        Paper override for the CN12 radius in pm, or ``default`` when unavailable.
    """
    return float(_SMITHELLS_RADII.get(symbol, default))
