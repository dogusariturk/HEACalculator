"""Batch composition unit converter (at% <-> wt% <-> vol%)."""

from __future__ import annotations

import numpy as np

from HEACalculator.data import Element

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"


class BatchCalculator:
    """Converts alloy compositions between atomic, weight, and volume percentages.

    Args:
        selected_elements (dict): A dictionary mapping element symbols to atomic percents.
    """

    def __init__(self, selected_elements: dict[str, float]) -> None:
        """Initialize with a dict of element symbols to atomic percents."""
        self.elements = selected_elements.keys()
        self.values = np.fromiter(selected_elements.values(), dtype=float)
        _element_data = [Element(elm) for elm in self.elements]
        self.at_wt_list = np.array([e.atomic_weight for e in _element_data])
        self.density_list = np.array([e.atomic_weight / e.atomic_volume for e in _element_data])

    def at_to_wt(self) -> np.ndarray:
        """Convert from atomic percent to weight percent.

        Returns:
            numpy.ndarray: Weight percentages in the same element order as the input.
        """
        _sum_product = np.dot(self.values, self.at_wt_list)
        return 100 * self.at_wt_list * self.values / _sum_product

    def at_to_vol(self) -> np.ndarray:
        """Convert from atomic percent to volume percent.

        Returns:
            numpy.ndarray: Volume percentages in the same element order as the input.
        """
        _sum_product = np.dot(self.values, self.at_wt_list / self.density_list)
        return 100 * (self.values * self.at_wt_list / self.density_list) / _sum_product

    def wt_to_at(self) -> np.ndarray:
        """Convert from weight percent to atomic percent.

        Returns:
            numpy.ndarray: Atomic percentages in the same element order as the input.
        """
        _sum_divide = np.sum(np.divide(self.values, self.at_wt_list))
        return 100 * (self.values / self.at_wt_list) / _sum_divide

    def wt_to_vol(self) -> np.ndarray:
        """Convert from weight percent to volume percent.

        Returns:
            numpy.ndarray: Volume percentages in the same element order as the input.
        """
        _sum_divide = np.sum(np.divide(self.values, self.density_list))
        return 100 * (self.values / self.density_list) / _sum_divide

    def vol_to_at(self) -> np.ndarray:
        """Convert from volume percent to atomic percent.

        Returns:
            numpy.ndarray: Atomic percentages in the same element order as the input.
        """
        _sum_product = np.dot(self.values, self.density_list / self.at_wt_list)
        return 100 * (self.values * self.density_list / self.at_wt_list) / _sum_product

    def vol_to_wt(self) -> np.ndarray:
        """Convert from volume percent to weight percent.

        Returns:
            numpy.ndarray: Weight percentages in the same element order as the input.
        """
        _sum_product = np.dot(self.values, self.density_list)
        return 100 * (self.values * self.density_list) / _sum_product
