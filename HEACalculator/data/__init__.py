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

from HEACalculator.data.Elements import _Element, _element_data
from HEACalculator.data.FormationEnthalpy import FormationEnthalpy
from HEACalculator.data.MixingEnthalpy import MixingEnthalpy

__author__ = 'Doguhan Sariturk'
__email__ = 'dogu.sariturk@gmail.com'

__all__ = ['MixingEnthalpy', 'FormationEnthalpy', 'Element']


def Element(name=None):
    """Function to access properties of an element

    Parameters
    ----------
    name : str, optional
        The element name for which the properties should be returned, by default None

    Raises
    ------
    SyntaxError
        If the input parameter is missing or not an instance of an str

    KeyError
        If the requested element does not exist in the database

    Returns
    -------
    _Element
        _Element class that stores the element properties
    """
    if name is None or not isinstance(name, str):
        raise SyntaxError('Usage: Element(X) where X is the element name.')
    if name not in _element_data:
        raise KeyError('The requested element does not exist in the elements database.')

    return _Element(name,
                    _element_data[name]['melting_point'],
                    _element_data[name]['atomic_number'],
                    _element_data[name]['atomic_volume'],
                    _element_data[name]['atomic_weight'],
                    _element_data[name]['atomic_radius'],
                    _element_data[name]['nvalence'])
