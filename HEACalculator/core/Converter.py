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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# You should have received a copy of the GNU General Public License

import numpy as np

from HEACalculator.data import Element


class BatchCalculator:
    def __init__(self, selected_elements):
        self.elements = selected_elements.keys()
        self.values = np.fromiter(selected_elements.values(), dtype=float)
        self.at_wt_list = np.array([Element(elm).atomic_weight for elm in self.elements])
        self.density_list = np.array([Element(elm).atomic_weight / Element(elm).atomic_volume for elm in self.elements])

    def AtToWt(self):
        _sum_product = np.dot(self.values, self.at_wt_list)
        return 100 * self.at_wt_list * self.values / _sum_product

    def AtToVol(self):
        _sum_product = np.dot(self.values, self.at_wt_list / self.density_list)
        return 100 * (self.values * self.at_wt_list / self.density_list) / _sum_product

    def WtToAt(self):
        _sum_divide = np.sum(np.divide(self.values, self.at_wt_list))
        return 100 * (self.values / self.at_wt_list) / _sum_divide

    def WtToVol(self):
        _sum_divide = np.sum(np.divide(self.values, self.density_list))
        return 100 * (self.values / self.density_list) / _sum_divide

    def VolToAt(self):
        _sum_product = np.dot(self.values, self.density_list / self.at_wt_list)
        return 100 * (self.values * self.density_list / self.at_wt_list) / _sum_product

    def VolToWt(self):
        _sum_product = np.dot(self.values, self.density_list)
        return 100 * (self.values * self.density_list) / _sum_product
