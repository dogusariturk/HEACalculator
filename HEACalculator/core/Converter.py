#!/usr/bin/env python3

# Copyright (C) 2022  Doguhan Sariturk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np

from HEACalculator.data import Element

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"


class BatchCalculator:
    """Class for converting at% to wt% and vol%

    Parameters
    ----------
    selected_elements: dict
        A dictionary of elements and their respective atomic percents.

    """

    def __init__(self, selected_elements):
        self.elements = selected_elements.keys()
        self.values = np.fromiter(selected_elements.values(), dtype=float)
        self.at_wt_list = np.array([Element(elm).atomic_weight for elm in self.elements])
        self.density_list = np.array([Element(elm).atomic_weight / Element(elm).atomic_volume for elm in self.elements])

    def at_to_wt(self):
        """Converts from at% to wt%

        Returns
        -------
        float
            wt%
        """
        _sum_product = np.dot(self.values, self.at_wt_list)
        return 100 * self.at_wt_list * self.values / _sum_product

    def at_to_vol(self):
        """Converts from at% to vol%

        Returns
        -------
        float
            vol%
        """
        _sum_product = np.dot(self.values, self.at_wt_list / self.density_list)
        return 100 * (self.values * self.at_wt_list / self.density_list) / _sum_product

    def wt_to_at(self):
        """Converts from wt% to at%

        Returns
        -------
        float
            at%
        """
        _sum_divide = np.sum(np.divide(self.values, self.at_wt_list))
        return 100 * (self.values / self.at_wt_list) / _sum_divide

    def wt_to_vol(self):
        """Converts from wt% to vol%

        Returns
        -------
        float
            vol%
        """
        _sum_divide = np.sum(np.divide(self.values, self.density_list))
        return 100 * (self.values / self.density_list) / _sum_divide

    def vol_to_at(self):
        """Converts from vol% to at%

        Returns
        -------
        float
            at%
        """
        _sum_product = np.dot(self.values, self.density_list / self.at_wt_list)
        return 100 * (self.values * self.density_list / self.at_wt_list) / _sum_product

    def vol_to_wt(self):
        """Converts from vol% to wt%

        Returns
        -------
        float
            wt%
        """
        _sum_product = np.dot(self.values, self.density_list)
        return 100 * (self.values * self.density_list) / _sum_product
