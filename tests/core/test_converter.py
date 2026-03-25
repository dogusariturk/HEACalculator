"""Tests for BatchCalculator composition conversion routines.

All conversions are verified against pre-computed reference values for a
five-element Al35–Ti35–V20–Cr5–Mn5 alloy (at% as input).
"""

import numpy as np


class TestBatchCalculator:
    """Round-trip and one-way conversion tests for BatchCalculator."""

    def test_at_to_wt(self, batch_calculator):
        """At% to wt% conversion matches reference values within default tolerance."""
        result = batch_calculator.at_to_wt()
        expected = [22.6290124, 40.14533628, 24.41364194, 6.22976438, 6.582245]
        np.testing.assert_array_almost_equal(result, expected)

    def test_at_to_vol(self, batch_calculator):
        """At% to vol% conversion matches reference values within default tolerance."""
        result = batch_calculator.at_to_vol()
        expected = [36.41660597, 38.60160233, 17.37592342, 3.76131516, 3.84455312]
        np.testing.assert_array_almost_equal(result, expected)

    def test_wt_to_at(self, batch_calculator):
        """wt% to at% conversion matches reference values within default tolerance."""
        result = batch_calculator.wt_to_at()
        expected = [49.73565038, 28.03485419, 15.05305795, 3.68693687, 3.48950061]
        np.testing.assert_array_almost_equal(result, expected)

    def test_wt_to_vol(self, batch_calculator):
        """wt% to vol% conversion matches reference values within default tolerance."""
        result = batch_calculator.wt_to_vol()
        expected = [51.13348886, 30.55215096, 12.92256822, 2.74057456, 2.6512174]
        np.testing.assert_array_almost_equal(result, expected)

    def test_vol_to_at(self, batch_calculator):
        """vol% to at% conversion matches reference values within default tolerance."""
        result = batch_calculator.vol_to_at()
        expected = [33.12747199, 31.25233207, 22.67063951, 6.54563762, 6.40391881]
        np.testing.assert_array_almost_equal(result, expected)

    def test_vol_to_wt(self, batch_calculator):
        """vol% to wt% conversion matches reference values within default tolerance."""
        result = batch_calculator.vol_to_wt()
        expected = [21.09668111, 35.30837845, 27.25804055, 8.03307574, 8.30382414]
        np.testing.assert_array_almost_equal(result, expected)
