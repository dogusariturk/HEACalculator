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

import itertools
import math

import numpy as np

from HEACalculator.core.helpers import nested_formula_parser
from HEACalculator.data import Element
from HEACalculator.data.FormationEnthalpy import FormationEnthalpy
from HEACalculator.data.MixingEnthalpy import MixingEnthalpy

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"
__version__ = "1.3.0"

GAS_CONSTANT = 8.314462618
J_PER_MOL_TO_EV_PER_ATOM = 0.0103642688 / 1000


class HEACalculator:
    """General class for the high entropy alloys.

    Parameters
    ----------
    formula : str
        Alloy formula.

    Attributes
    ----------

    mixing_enthalpy: float
        Mixing enthalpy of the alloy. [1]_

    density: float
        Approximate density of the alloy.

    valance_electron_concentration: int
        Valence electron concentration of the alloy.

    melting_temperature: float
        Approximate melting temperature of the alloy.

    atomic_size_difference: float
        Atomic size difference of the alloy. [2]_

    mixing_entropy: float
        Mixing entropy of the alloy.

    omega_parameter: float
        Omega parameter. [3]_

    gamma_parameter: float
        Atomic size difference of the alloy. According to [4]_

    lambda_parameter: float
        Parameter focuses on the configurational entropy and the atomic size difference. [5]_

    microstructure: str
        Expected crystal structure of the alloy. [6]_

    formation_enthalpy: float
        Binary enthalpy of formation of ordered compounds of the system, in meV/atom. [7]_

    min_formation_enthalpy: float
        Minimum binary enthalpy of formation of ordered compounds of the system, in meV/atom. [7]_

    model_1: str
        Criteria for the formation of SSS HEAs. [3]_

    model_2: str
        Criteria for the formation of SSS HEAs. [8]_

    model_3: str
        Criteria for the formation of SSS HEAs. [4]_

    model_4: str
        Criteria for the formation of SSS HEAs. [5]_

    model_5: str
        Criteria for the formation of SSS HEAs. [9]_

    model_6: str
        Criteria for the formation of SSS HEAs. [7]_

    model_7: str
        Criteria for the formation of SSS HEAs. [10]_

    model_8: str
        Criteria for the formation of SSS HEAs. [11]_

    References
    ----------
    .. [1] Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P.K.; Lu, Z.P. Prog. Mater. Sci. 2014, 61.
    .. [2] S.S.Fang, X. S. Xiao, L. Xia, W. H. Li, Y. D. Dong,J. Non-Cryst. Solids 2003, 321, 120.
    .. [3] Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233–238.
    .. [4] Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T.; Scr. Mater. 94 (2015) 28–31.
    .. [5] Singh, A.K.; Kumar N.; Dwivedi A.; Subramaniam A.; Intermetallics 53 (2014) 112–119.
    .. [6] Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
    .. [7] Troparevsky, M. C.; Morris, J. R.; Kent, P. R. C.; Lupini, A. R.; Stocks, G. M.; Phys. Rev. X, 5(1) (2015)
    .. [8] S. Guo, Q. Hu, C. Ng, C.T. Liu, Intermetallics 41 (0) (2013) 96–103.
    .. [9] Y.F. Ye, Q. Wang, J. Lu, C.T. Liu, Y. Yang, Scr. Mater. 104 (2015) 53–55.
    .. [10] O.N. Senkov, D.B. Miracle, J. Alloys Compd. 658 (2016) 603–607.
    .. [11] D.J.M. King, S.C. Middleburgh, A.G. McGregor, M.B. Cortie, Acta Mater. 104 (2016) 172–179.
    """

    def __init__(self, formula):
        self.formula = formula

        self._alloy = nested_formula_parser(self.formula)
        self._atomic_percentage = {elm: num / sum(self._alloy.values()) for (elm, num) in self._alloy.items()}
        self._pair_list = list(itertools.combinations(self._alloy, 2))
        self._pair_percentage = [(self._alloy[each[0]] / sum(self._alloy.values())) *
                                 (self._alloy[each[1]] / sum(self._alloy.values())) for each in self._pair_list]
        self._atomic_radius_list = [Element(elm).atomic_radius for elm in self._alloy]
        self._average_atomic_radius = sum([percentage * radius
                                           for percentage, radius in
                                           zip(self._atomic_percentage.values(), self._atomic_radius_list)])

        self.mixing_enthalpy = None
        self.formation_enthalpy = None
        self.density = None
        self.valance_electron_concentration = None
        self.melting_temperature = None
        self.atomic_size_difference = None
        self.min_formation_enthalpy = None
        self.mixing_entropy = None
        self.microstructure = None

        self.gamma_parameter = None
        self.omega_parameter = None
        self.lambda_parameter = None
        self.phi_parameter = None

        self.model_1 = None
        self.model_2 = None
        self.model_3 = None
        self.model_4 = None
        self.model_5 = 'Not Implemented Yet'
        self.model_6 = None
        self.model_7 = None
        self.model_8 = 'Not Implemented Yet'

        self.calculate()

    def calculate(self):
        """This method calculates phenomenological parameters based on thermodynamics and physics
        in order to predict the formation of solid solutions in High Entropy Alloys (HEAs)

        Raises
        ------
        TypeError
            If one of the entries are not in the database
        """
        self.mixing_enthalpy = self.get_mixing_enthalpy()
        self.formation_enthalpy = self.get_formation_enthalpy()
        self.min_formation_enthalpy = self.get_min_formation_enthalpy()
        self.density = self.get_density()
        self.valance_electron_concentration = self.get_valance_electron_concentration()
        self.melting_temperature = self.get_melting_temperature()
        self.atomic_size_difference = self.get_atomic_size_difference()
        self.mixing_entropy = self.get_mixing_entropy()

        self.gamma_parameter = self.get_gamma()
        self.omega_parameter = self.get_omega()
        self.lambda_parameter = self.get_lambda()
        # self.phi_parameter = self.get_phi()

        self.microstructure = self.get_microstructure()

        self.model_1 = self.get_model_1_result()
        self.model_2 = self.get_model_2_result()
        self.model_3 = self.get_model_3_result()
        self.model_4 = self.get_model_4_result()
        # self.model_5 = self.get_model_5_result()
        self.model_6 = self.get_model_6_result()
        self.model_7 = self.get_model_7_result()
        # self.model_8 = self.get_model_8_result()

    def get_mixing_enthalpy(self):
        """Returns the enthalpy of mixing of the alloy

        Returns
        -------
        float
            The mixing enthalpy of the alloy in kJ/mol
        """
        pair_mixing_enthalpy = [MixingEnthalpy(pair) for pair in self._pair_list]
        return 4 * sum(
                [percent * enthalpy for percent, enthalpy in zip(self._pair_percentage, pair_mixing_enthalpy)])

    def get_formation_enthalpy(self):
        """Returns the enthalpy of formation of the alloy

        Returns
        -------
        float
            The formation enthalpy of the alloy in meV/atom
        """
        pair_formation_enthalpy = [FormationEnthalpy(pair) for pair in self._pair_list]
        return 4 * sum(
                [percent * enthalpy for percent, enthalpy in zip(self._pair_percentage, pair_formation_enthalpy)])

    def get_density(self):
        """Returns the density of the alloy

        Returns
        -------
        float
            The density of the alloy in g/cm^3
        """
        total_weight = sum(Element(elm).atomic_weight * af for elm, af in self._alloy.items())
        total_volume = sum(Element(elm).atomic_volume * af for elm, af in self._alloy.items())
        return total_weight / total_volume

    def get_valance_electron_concentration(self):
        """Returns the valance electron concentration (VEC) of the alloy

        Returns
        -------
        float
            The valance electron concentration (VEC) of the alloy
        """
        nvalence_list = [Element(elm).nvalence for elm in self._alloy]
        return sum(
                [percentage * valence for percentage, valence in
                 zip(self._atomic_percentage.values(), nvalence_list)])

    def get_melting_temperature(self):
        """Returns the melting temperature of the alloy in Kelvin

        Returns
        -------
        float
            The melting temperature of the alloy in Kelvin
        """
        melting_temperature_list = [Element(elm).melting_point for elm in self._alloy]
        return math.ceil(sum([percentage * melting_temp
                              for percentage, melting_temp in
                              zip(self._atomic_percentage.values(), melting_temperature_list)]))

    def get_atomic_size_difference(self):
        """Returns the atomic size difference, delta, of the alloy

        Returns
        -------
        float
            The atomic size difference, delta, of the alloy
        """
        _delta = sum([percentage * (1 - (radius / self._average_atomic_radius)) ** 2
                      for percentage, radius in zip(self._atomic_percentage.values(), self._atomic_radius_list)])
        return math.sqrt(_delta) * 100

    def get_min_formation_enthalpy(self):
        """Returns the minimum binary enthalpy of formation of ordered compounds of the system in meV/atom

        Returns
        -------
        float
            The minimum binary enthalpy of formation of ordered compounds of the system in meV/atom
        """
        pair_formation_enthalpy = [FormationEnthalpy(pair) for pair in self._pair_list]
        return min(pair_formation_enthalpy)

    def get_mixing_entropy(self):
        """Returns the entropy of mixing of the alloy in J/K.mol

        Returns
        -------
        float
            The mixing entropy of the alloy in J/K.mol
        """
        return -1 * GAS_CONSTANT * sum(
                list(self._atomic_percentage.values()) * np.log(list(self._atomic_percentage.values())))

    def get_gamma(self):
        """Returns the Gamma parameter, atomic size difference of the alloy. According to [12]_

        Returns
        -------
        float
            The Gamma parameter, atomic size difference of the alloy

        References
        ----------
        .. [12] Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T.; Scr. Mater. 94 (2015) 28–31.
        """
        smallest_solid_angle = (1 - np.sqrt(
                (((min(self._atomic_radius_list) + self._average_atomic_radius) ** 2) - (
                        self._average_atomic_radius ** 2)) / (
                        (min(self._atomic_radius_list) + self._average_atomic_radius) ** 2)))
        largest_solid_angle = (1 - np.sqrt(
                (((max(self._atomic_radius_list) + self._average_atomic_radius) ** 2) - (
                        self._average_atomic_radius ** 2)) / (
                        (max(self._atomic_radius_list) + self._average_atomic_radius) ** 2)))
        return smallest_solid_angle / largest_solid_angle

    def get_omega(self, temperature=None):
        """Returns the Omega parameter. According to [13]_

        Parameters
        ----------
        temperature : float, optional
            The critical temperature for which the omega parameter should be calculated
            By default None, which implies to the melting temperature of the alloy

        Returns
        -------
        float
            The Omega parameter

        References
        ----------
        .. [13] Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233–238.
        """
        if self.melting_temperature is None:
            self.melting_temperature = self.get_melting_temperature()

        if self.mixing_entropy is None:
            self.mixing_entropy = self.get_mixing_entropy()

        if self.mixing_enthalpy is None:
            self.mixing_enthalpy = self.get_mixing_enthalpy()

        if temperature is None:
            return (self.melting_temperature * self.mixing_entropy) / (abs(self.mixing_enthalpy) * 1000)

        return (temperature * self.mixing_entropy) / (abs(self.mixing_enthalpy) * 1000)

    def get_lambda(self):
        """Returns the Lambda parameter focuses on the configurational entropy and the atomic size difference.

        Returns
        -------
        float
            The Lambda parameter, according to [14]_

        References
        ----------
        .. [14] Singh, A.K.; Kumar N.; Dwivedi A.; Subramaniam A.; Intermetallics 53 (2014) 112–119.
        """
        if self.mixing_entropy is None:
            self.mixing_entropy = self.get_mixing_entropy()

        if self.atomic_size_difference is None:
            self.atomic_size_difference = self.get_atomic_size_difference()

        return self.mixing_entropy / (self.atomic_size_difference ** 2)

    def get_phi(self):
        """Returns the Phi parameter. According to [15]_

        Warnings
        --------
        This method is not implemented yet

        Returns
        -------
        float
            The Phi parameter

        References
        ----------
        .. [15] Y.F. Ye, Q. Wang, J. Lu, C.T. Liu, Y. Yang, Scr. Mater. 104 (2015) 53–55.
        """
        # if self.density is None:
        #     self.density = self.get_density()
        # if self.mixing_enthalpy is None:
        #     self.mixing_enthalpy = self.get_mixing_enthalpy()
        # if self.melting_temperature is None:
        #     self.melting_temperature = self.get_melting_temperature()
        # if self.mixing_entropy is None:
        #     self.mixing_entropy = self.get_mixing_entropy()
        #
        # xi = {elm: (1 / 6) * np.pi * self.density * ((2 * Element(elm).atomic_radius) ** 3) * percentage for
        #       (percentage, elm) in zip(self._atomic_percentage.values(), self._alloy.keys())}
        # sum_xi = sum(xi.values())
        # delta_ij = {pair: (((xi[pair[0]] * xi[pair[1]]) ** (1 / 2)) / sum_xi) * (
        #         (2 * Element(pair[0]).atomic_radius - 2 * Element(pair[1]).atomic_radius) ** 2 / (
        #          2 * Element(pair[0]).atomic_radius * 2 * Element(pair[1]).atomic_radius)) * (
        #                           (self._atomic_percentage[pair[0]] * self._atomic_percentage[pair[1]]) ** (
        #                           1 / 2)) for pair in self._pair_list}
        # y3 = sum((xi[elm] / sum_xi ** (2 / 3) * (self._atomic_percentage[elm] ** (1 / 3))) ** 3 for elm in
        #          self._alloy.keys())
        # y2 = sum(delta_ij[pair] * sum((xi[each] / sum_xi) * (
        #         (2 * Element(pair[0]).atomic_radius * 2 * Element(pair[1]).atomic_radius) ** (1 / 2) /
        #         (2 * Element(each).atomic_radius)) for each in self._alloy.keys()) for pair in
        #          self._pair_list)
        # y1 = sum(delta_ij[pair] * (2 * Element(pair[0]).atomic_radius + 2 * Element(pair[1]).atomic_radius) * (
        #         2 * Element(pair[0]).atomic_radius * 2 * Element(pair[1]).atomic_radius) ** (-1 * 1 / 2) for
        #          pair in self._pair_list)
        # Z = ((1 + sum_xi + sum_xi ** 2) - (3 * sum_xi * (y1 + (y2 * sum_xi))) - ((sum_xi ** 3) * y3)) * (
        #         (1 - sum_xi) ** (-3))
        # F_term = ((-3 / 2) * (1 - y1 + y2 + y3)) + \
        #          ((3 * y2 + 2 * y3) * ((1 - sum_xi) ** (-1))) + \
        #          ((3 / 2) * (1 - y1 - y2 - ((1 / 3) * y3)) * ((1 - sum_xi) ** (-2))) + \
        #          ((y3 - 1) * np.log(1 - sum_xi))
        # s_E = GAS_CONSTANT * (F_term - np.log(Z) - (3 - 2 * sum_xi) * (1 - sum_xi) ** (-2) + 3 +
        #                       np.log((1 + sum_xi + sum_xi ** 2 - sum_xi ** 3) * (1 - sum_xi) ** (-3)))
        # s_H = abs(self.mixing_enthalpy) / self.melting_temperature
        # return (self.mixing_entropy - s_H) / abs(s_E)
        raise NotImplementedError

    def get_microstructure(self):
        """Returns the expected crystal structure of the alloy. According to [16]_

        Returns
        -------
        str
            The expected crystal structure of the alloy

        References
        ----------
        .. [16] Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
        """
        if self.valance_electron_concentration is None:
            self.valance_electron_concentration = self.get_valance_electron_concentration()

        if 2.5 <= self.valance_electron_concentration <= 3.5:
            return "HCP"
        if self.valance_electron_concentration >= 8.0:
            return "FCC"
        if self.valance_electron_concentration <= 6.87:
            return "BCC"

        return "BCC+FCC"

    def get_model_1_result(self):
        """Returns the solid solution / intermetallic prediction according to [17]_

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [17] X. Yang, Y. Zhang, Mater. Chem. Phys. 132 (2) (2012) 233–238.
        """
        if self.omega_parameter is None:
            self.omega_parameter = self.get_omega()

        if self.atomic_size_difference is None:
            self.atomic_size_difference = self.get_atomic_size_difference()

        return 'Solid Solution' if self.omega_parameter >= 1.1 and self.atomic_size_difference <= 6.6 else 'Intermetallic'

    def get_model_2_result(self):
        """Returns the solid solution / intermetallic prediction according to [18]_

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [18] S. Guo, Q. Hu, C. Ng, C.T. Liu, Intermetallics 41 (0) (2013) 96–103.
        """
        if self.mixing_enthalpy is None:
            self.mixing_enthalpy = self.get_mixing_enthalpy()

        if self.atomic_size_difference is None:
            self.atomic_size_difference = self.get_atomic_size_difference()

        return 'Solid Solution' \
            if -11.6 < self.mixing_enthalpy < 3.2 and self.atomic_size_difference < 6.6 else 'Intermetallic'

    def get_model_3_result(self):
        """Returns the solid solution / intermetallic prediction according to [19]_

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [19] Z. Wang, Y. Huang, Y. Yang, J. Wang, C.T. Liu, Scr. Mater. 94 (2015) 28–31.
        """
        if self.omega_parameter is None:
            self.omega_parameter = self.get_omega()

        if self.gamma_parameter is None:
            self.gamma_parameter = self.get_gamma()

        return 'Solid Solution' if self.omega_parameter >= 1.1 and self.gamma_parameter < 1.175 else 'Intermetallic'

    def get_model_4_result(self):
        """Returns the solid solution / intermetallic prediction according to [20]_

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [20] A.K. Singh, N. Kumar, A. Dwivedi, A. Subramaniam, Intermetallics 53 (2014) 112–119.
        """
        if self.lambda_parameter is None:
            self.lambda_parameter = self.get_lambda()

        return 'Solid Solution' if self.lambda_parameter > 0.96 else 'Intermetallic'

    def get_model_5_result(self):
        """Returns the solid solution / intermetallic prediction according to [21]_

        Warnings
        --------
        This method is not implemented yet

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [21] Y.F. Ye, Q. Wang, J. Lu, C.T. Liu, Y. Yang, Scr. Mater. 104 (2015) 53–55.
        """
        # if self.phi_parameter is None:
        #     self.phi_parameter = self.get_phi()
        #
        # return 'Solid Solution' if self.phi_parameter > 20 else 'Intermetallic'
        raise NotImplementedError

    def get_model_6_result(self):
        """Returns the solid solution / multiple phase prediction according to [22]_

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [22] Troparevsky, M. C.; Morris, J. R.; Kent, P. R. C.; Lupini, A. R.; Stocks, G. M.; Phys. Rev. X, 5(1) (2015)
        """
        if self.melting_temperature is None:
            self.melting_temperature = self.get_melting_temperature()

        if self.min_formation_enthalpy is None:
            self.min_formation_enthalpy = self.get_min_formation_enthalpy()

        _critical_temperature = self.melting_temperature * 0.55
        return 'Solid Solution' \
            if (-1 * 1000 * _critical_temperature * self.mixing_entropy * J_PER_MOL_TO_EV_PER_ATOM) \
               < float(self.min_formation_enthalpy) < 37 \
            else 'Multiple Phases'

    def get_model_7_result(self, k_2=0.6, annealing_temperature=None):
        """Returns the solid solution / intermetallic prediction according to [23]_

        Parameters
        ----------
        k_2 : float, optional
            The parameter that corresponds to the ratio of intermetallic and mixing entropies

        annealing_temperature : float, optional
            The critical temperature for which the omega parameter should be calculated
            By default None, which implies to the 60% of the melting temperature of the alloy

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [23] O.N. Senkov, D.B. Miracle, J. Alloys Compd. 658 (2016) 603–607.
        """
        if self.formation_enthalpy is None:
            self.formation_enthalpy = self.get_formation_enthalpy()

        if annealing_temperature is None:
            annealing_temperature = self.melting_temperature * 0.6

        k_1 = self.formation_enthalpy / self.mixing_enthalpy

        omega = self.get_omega(temperature=annealing_temperature)
        k_1_cr = (omega * (1 - k_2)) + 1

        return 'Solid Solution' if k_1_cr > k_1 else 'Intermetallic'

    def get_model_8_result(self):
        """Returns the solid solution / intermetallic prediction according to [24]_

        Warnings
        --------
        This method is not implemented yet

        Returns
        -------
        str
            Solid Solution or Intermetallic

        References
        ----------
        .. [24] D.J.M. King, S.C. Middleburgh, A.G. McGregor, M.B. Cortie, Acta Mater. 104 (2016) 172–179.
        """
        raise NotImplementedError

    def get_list(self):
        """Returns a list of all the properties of the alloy

        Returns
        -------
        list
            All the calculated properties of the alloy
        """
        return_list = [self.formula]
        for item in [
                self.density,
                self.atomic_size_difference,
                self.omega_parameter,
                self.valance_electron_concentration,
                self.mixing_enthalpy,
                self.mixing_entropy,
                self.formation_enthalpy,
                self.melting_temperature,
        ]:
            return_list.append("%.2f" % item)
        return_list.append(self.microstructure)
        for item in [
                self.model_1,
                self.model_2,
                self.model_3,
                self.model_4,
                self.model_5,
                self.model_6,
                self.model_7,
                self.model_8,
        ]:
            return_list.append(item)
        return return_list

    def __str__(self):
        return f'{self.formula:=^48}\n' \
               f'{"Density":25}: {self.density: >10.2} g/cm^3\n' \
               f'{"Delta":25}: {self.atomic_size_difference:>10.2f} \n' \
               f'{"Omega":25}: {self.omega_parameter:>10.2f} \n' \
               f'{"Gamma":25}: {self.gamma_parameter:>10.2f} \n' \
               f'{"Lambda":25}: {self.lambda_parameter:>10.2f} \n' \
               f'{"VEC":25}: {self.valance_electron_concentration:>10.2f} \n' \
               f'{"Mixing Enthalpy":25}: {self.mixing_enthalpy: >10.2f} kJ/mol\n' \
               f'{"Mixing Entropy":25}: {self.mixing_entropy: >10.2f} J/K.mol\n' \
               f'{"Formation Enthalpy":25}: {self.formation_enthalpy: >10.2f} meV/atom\n' \
               f'{"Min. Formation Enthalpy":25}: {self.min_formation_enthalpy: >10.2f} meV/atom\n' \
               f'{"Melting Temperature":25}: {self.melting_temperature: >10} K\n' \
               f'{"Predictions":=^48}\n' \
               f'{"Microstructure":25}:     {self.microstructure} \n' \
               f'{"Model 1":25}:     {self.model_1}\n' \
               f'{"Model 2":25}:     {self.model_2}\n' \
               f'{"Model 3":25}:     {self.model_3}\n' \
               f'{"Model 4":25}:     {self.model_4}\n' \
               f'{"Model 5":25}:     {self.model_5}\n' \
               f'{"Model 6":25}:     {self.model_6}\n' \
               f'{"Model 7":25}:     {self.model_7}\n' \
               f'{"Model 8":25}:     {self.model_8}\n'
