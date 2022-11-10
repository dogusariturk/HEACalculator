from unittest import TestCase

import numpy as np

from HEACalculator.core import Converter


class TestConverterCalculator(TestCase):

    selected_elements = {'Al': 35.00, 'Ti': 35.00, 'V': 20.00, 'Cr': 5.00, 'Mn': 5.0}

    def test_at_to_wt(self):
        res = Converter.BatchCalculator(self.selected_elements)
        a = res.AtToWt()
        b = [22.6290124, 40.14533628, 24.41364194, 6.22976438, 6.582245]
        self.assertIsNone(np.testing.assert_array_almost_equal(a, b))

    def test_at_to_vol(self):
        res = Converter.BatchCalculator(self.selected_elements)
        a = res.AtToVol()
        b = [36.41660597, 38.60160233, 17.37592342, 3.76131516, 3.84455312]
        self.assertIsNone(np.testing.assert_array_almost_equal(a, b))

    def test_wt_to_at(self):
        res = Converter.BatchCalculator(self.selected_elements)
        a = res.WtToAt()
        b = [49.73565038, 28.03485419, 15.05305795, 3.68693687, 3.48950061]
        self.assertIsNone(np.testing.assert_array_almost_equal(a, b))

    def test_wt_to_vol(self):
        res = Converter.BatchCalculator(self.selected_elements)
        a = res.WtToVol()
        b = [51.13348886, 30.55215096, 12.92256822, 2.74057456, 2.6512174]
        self.assertIsNone(np.testing.assert_array_almost_equal(a, b))

    def test_vol_to_at(self):
        res = Converter.BatchCalculator(self.selected_elements)
        a = res.VolToAt()
        b = [33.12747199, 31.25233207, 22.67063951, 6.54563762, 6.40391881]
        self.assertIsNone(np.testing.assert_array_almost_equal(a, b))

    def test_vol_to_wt(self):
        res = Converter.BatchCalculator(self.selected_elements)
        a = res.VolToWt()
        b =[21.09668111, 35.30837845, 27.25804055, 8.03307574, 8.30382414]
        self.assertIsNone(np.testing.assert_array_almost_equal(a, b))
