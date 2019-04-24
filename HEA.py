#!python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019  Doguhan Sariturk
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
import pandas as pd

from scipy import constants
from mendeleev import element
from thermo import nested_formula_parser
from prettytable import PrettyTable

__author__ = 'Dogu Sariturk'
__version__ = "0.0.1"
__email__ = 'dogu.sariturk@gmail.com'
__status__ = 'Development'


class HEA:
    """

    Attributes
    ----------
    formula : str
        The formula of the alloy, in at%

    _alloy : str
        The formula of the alloy, in at%

    mixing_entropy : float
        The formula of the alloy, in at%

    mixing_enthalpy : float
        The formula of the alloy, in at%

    melting_temperature : float
        The formula of the alloy, in at%

    delta : float
        The formula of the alloy, in at%

    omega : float
        The formula of the alloy, in at%

    VEC : float
        The formula of the alloy, in at%

    density : float
        The formula of the alloy, in at%

    crystalStructure : str
        The formula of the alloy, in at%

    isSolidSolution : bool
        The formula of the alloy, in at%

    """

    _data = pd.read_csv('data/mixing.csv')
    _tab = PrettyTable(
        field_names=["Alloy", "Density", "Delta", "Hmix", "Smix", "VEC", "Tm", "Phases"])

    def __init__(self, formula):
        """
        Initilize HEA class with the alloy formula and related attributes.

        Parameters
        ----------
        alloy : str
            The formula of the alloy, in at%

        """
        self.formula = formula
        self._alloy = nested_formula_parser(formula)
        self.mixing_entropy = self.configurationalEntropy()
        self.mixing_enthalpy = self.enthalpyOfMixing()
        self.melting_temperature = self.meltingTemperature()
        self.delta = self.atomicSizeDifference()
        self.omega = self.omegaCalculation()
        self.VEC = self.valenceElectronConcentration()
        self.density = self.density()
        self.crystalStructure = self.crystalStructure()
        self.isSolidSolution = self.isSolidSolution()

    def configurationalEntropy(self):
        """Return the mixing entropy of the alloy."""
        # TODO: Non equiatomic alloys.
        if len(set(self._alloy.values())) == 1:
            return constants.R * np.log(len(self._alloy))
        else:
            pass

    def enthalpyOfMixing(self):
        """

        Return the mixing enthalpy of the alloy.


        References
        ----------

        """
        list_of_pairs = [(a, b)
                         for a in self._alloy for b in self._alloy if a != b and (a, b) != (b, a)]
        enthalpy = [self._data.at[a] for a in list_of_pairs]
        return sum(2 * y / (len(self._alloy) ** 2) for y in enthalpy)

    def atomicSizeDifference(self):
        """

        Return the atomic size difference of the alloy, i.e. delta.

        References
        ----------

        """
        # FIXME:
        delta = sum((num / sum(self._alloy.values())) * (1 - (element(elm).atomic_radius /
                                                              self.averageAtomicRadius()))**2 for elm, num in self._alloy.items())
        return np.sqrt(delta) * 100

    def averageAtomicRadius(self):
        """

        Return the average atomic radius of the alloy.

        References
        ----------


        """
        return sum(num / sum(self._alloy.values()) * (element(elm).atomic_radius) for elm, num in self._alloy.items())

    def valenceElectronConcentration(self):
        """

        Return the valence electron concentration of the alloy.

        References
        ----------


        """
        return sum(num / sum(self._alloy.values()) * element(elm).nvalence() for elm, num in self._alloy.items())

    def omegaCalculation(self):
        """Return the omega value of the alloy."""
        return (self.meltingTemperature() * self.configurationalEntropy()) / (abs(self.enthalpyOfMixing()) * 1000)

    def meltingTemperature(self):
        """

        Return the approximate melting temperature of the alloy.

        References
        ----------

        """
        t_melting = sum(num / sum(self._alloy.values()) * (element(elm).melting_point)
                        for elm, num in self._alloy.items())
        return t_melting

    def isSolidSolution(self):
        """Return True if the alloy forms solid solution."""
        if self.omegaCalculation() >= 1.1:
            if self.atomicSizeDifference() < 6.6:
                if (self.enthalpyOfMixing() < 5 and self.enthalpyOfMixing() > -15):
                    return 'Yes'
        else:
            return 'No'

    def density(self):
        """

        Return the approximate density of the alloy.

        References
        ----------

        """
        # element(x).density for x in self._alloy.keys()
        # (at% * at.wt) of x / (at% * at.wt) of all
        pass

    def crystalStructure(self):
        """Return the predicted crystal structure of the alloy."""
        # TODO: Amorphous phases and Intermetallics --> Prog. Nat. Sci: Mat. Int. 21(2011) 433-446
        if self.VEC > 8:
            return 'FCC'
        if self.VEC < 6.87:
            return 'BCC'
        else:
            return 'BCC+FCC'

    def printResults(self):

        print(self.formula)
        print(
            '\n\t S_mixing\t\t= {:7.2f} [J/K mol]'.format(self.mixing_entropy))
        print('\t H_mixing\t\t= {:7.2f} [kJ/mol]'.format(self.mixing_enthalpy))
        print('\t Delta\t\t\t= {:7.2f} [%]'.format(self.delta))
        print('\t VEC\t\t\t= {:7.2f}'.format(self.VEC))
        print('\t Omega\t\t\t= {:7.3f}'.format(self.omega))
        print('\t T_melting\t\t= {:7.3f} [K]'.format(self.melting_temperature))
        print('\t Density\t\t=')
        print('\t Crystal Structure\t=   {}\n'.format(self.crystalStructure))

    def prettyPrint(self):
        self._tab.add_row([self.formula, "TODO", self.delta, self.mixing_enthalpy,
                           self.mixing_entropy, self.VEC, self.melting_temperature, self.crystalStructure])

    def table(self):
        print(self._tab)
