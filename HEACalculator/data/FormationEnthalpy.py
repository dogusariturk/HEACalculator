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


__author__ = 'Doguhan Sariturk'
__email__ = 'dogu.sariturk@gmail.com'

_formation_enthalpy_data = {('Al', 'Mg'): -33.0, ('Mg', 'Sc'): 2.0, ('Mg', 'Ti'): 20.0, ('Mg', 'V'): 171.0,
                            ('Cr', 'Mg'): 160.0, ('Mg', 'Mn'): 87.0, ('Fe', 'Mg'): 77.0, ('Co', 'Mg'): -31.0,
                            ('Mg', 'Ni'): -723.0, ('Cu', 'Mg'): -147.0, ('Mg', 'Zn'): -139.0, ('Mg', 'Y'): 4.0,
                            ('Mg', 'Zr'): -31.0, ('Mg', 'Nb'): 105.0, ('Mg', 'Mo'): 164.0, ('Mg', 'Ru'): 4.0,
                            ('Mg', 'Rh'): -478.0, ('Mg', 'Pd'): -742.0, ('Ag', 'Mg'): -255.0, ('Cd', 'Mg'): -109.0,
                            ('La', 'Mg'): -140.0, ('Hf', 'Mg'): -7.0, ('Mg', 'Ta'): 122.0, ('Mg', 'W'): 234.0,
                            ('Mg', 'Re'): 67.0, ('Mg', 'Os'): 43.0, ('Ir', 'Mg'): -369.0, ('Mg', 'Pt'): -872.0,
                            ('Au', 'Mg'): -612.0, ('Al', 'Sc'): -444.0, ('Al', 'Ti'): -428.0, ('Al', 'V'): -282.0,
                            ('Al', 'Cr'): -138.0, ('Al', 'Mn'): -278.0, ('Al', 'Fe'): -369.0, ('Al', 'Co'): -629.0,
                            ('Al', 'Ni'): -677.0, ('Al', 'Cu'): -224.0, ('Al', 'Zn'): -520.0, ('Al', 'Y'): -544.0,
                            ('Al', 'Zr'): -539.0, ('Al', 'Nb'): -288.0, ('Al', 'Mo'): -168.0, ('Al', 'Ru'): -678.0,
                            ('Al', 'Rh'): -1101.0, ('Al', 'Pd'): -874.0, ('Ag', 'Al'): -76.0, ('Al', 'Cd'): -1938.0,
                            ('Al', 'La'): -360.0, ('Al', 'Hf'): -444.0, ('Al', 'Ta'): -320.0, ('Al', 'W'): -161.0,
                            ('Al', 'Re'): -257.0, ('Al', 'Os'): -577.0, ('Al', 'Ir'): -944.0, ('Al', 'Pt'): -960.0,
                            ('Al', 'Au'): -466.0, ('Sc', 'Ti'): 38.0, ('Sc', 'V'): 83.0, ('Cr', 'Sc'): 119.0,
                            ('Mn', 'Sc'): -142.0, ('Fe', 'Sc'): -281.0, ('Co', 'Sc'): -359.0, ('Ni', 'Sc'): -525.0,
                            ('Cu', 'Sc'): -284.0, ('Sc', 'Zn'): -380.0, ('Sc', 'Y'): 18.0, ('Sc', 'Zr'): -29.0,
                            ('Nb', 'Sc'): 61.0, ('Mo', 'Sc'): -11.0, ('Ru', 'Sc'): -540.0, ('Rh', 'Sc'): -1035.0,
                            ('Pd', 'Sc'): -906.0, ('Ag', 'Sc'): -309.0, ('Cd', 'Sc'): -296.0, ('La', 'Sc'): 33.0,
                            ('Hf', 'Sc'): -10.0, ('Sc', 'Ta'): 75.0, ('Sc', 'W'): 44.0, ('Re', 'Sc'): -341.0,
                            ('Os', 'Sc'): -400.0, ('Ir', 'Sc'): -1032.0, ('Pt', 'Sc'): -1232.0, ('Au', 'Sc'): -822.0,
                            ('Ti', 'V'): 37.0, ('Cr', 'Ti'): -372.0, ('Mn', 'Ti'): -277.0, ('Fe', 'Ti'): -418.0,
                            ('Co', 'Ti'): -386.0, ('Ni', 'Ti'): -435.0, ('Cu', 'Ti'): -147.0, ('Ti', 'Zn'): -198.0,
                            ('Ti', 'Y'): 111.0, ('Ti', 'Zr'): 24.0, ('Nb', 'Ti'): 11.0, ('Mo', 'Ti'): -167.0,
                            ('Ru', 'Ti'): -763.0, ('Rh', 'Ti'): -790.0, ('Pd', 'Ti'): -646.0, ('Ag', 'Ti'): -65.0,
                            ('Cd', 'Ti'): -69.0, ('La', 'Ti'): -170.0, ('Hf', 'Ti'): -10.0, ('Ta', 'Ti'): 31.0,
                            ('Ti', 'W'): -82.0, ('Re', 'Ti'): -189.0, ('Os', 'Ti'): -713.0, ('Ir', 'Ti'): -847.0,
                            ('Pt', 'Ti'): -934.0, ('Au', 'Ti'): -430.0, ('Cr', 'V'): -88.0, ('Mn', 'V'): -286.0,
                            ('Fe', 'V'): -176.0, ('Co', 'V'): -199.0, ('Ni', 'V'): -250.0, ('Cu', 'V'): 54.0,
                            ('V', 'Zn'): -51.0, ('V', 'Y'): 143.0, ('V', 'Zr'): 26.0, ('Nb', 'V'): -56.0,
                            ('Mo', 'V'): -127.0, ('Ru', 'V'): -321.0, ('Rh', 'V'): -393.0, ('Pd', 'V'): -275.0,
                            ('Ag', 'V'): 147.0, ('Cd', 'V'): 133.0, ('La', 'V'): 170.0, ('Hf', 'V'): 7.0,
                            ('Ta', 'V'): -122.0, ('V', 'W'): -97.0, ('Re', 'V'): -148.0, ('Os', 'V'): -361.0,
                            ('Ir', 'V'): -505.0, ('Pt', 'V'): -564.0, ('Au', 'V'): -43.0, ('Cr', 'Mn'): -110.0,
                            ('Cr', 'Fe'): -8.0, ('Co', 'Cr'): 5.0, ('Cr', 'Ni'): -30.0, ('Cr', 'Cu'): 108.0,
                            ('Cr', 'Zn'): 44.0, ('Cr', 'Y'): 150.0, ('Cr', 'Zr'): -150.0, ('Cr', 'Nb'): -47.0,
                            ('Cr', 'Mo'): 42.0, ('Cr', 'Ru'): 4.0, ('Cr', 'Rh'): -129.0, ('Cr', 'Pd'): -82.0,
                            ('Ag', 'Cr'): 129.0, ('Cd', 'Cr'): 113.0, ('Cr', 'La'): 173.0, ('Cr', 'Hf'): -362.0,
                            ('Cr', 'Ta'): -130.0, ('Cr', 'W'): 26.0, ('Cr', 'Re'): 4.0, ('Cr', 'Os'): -22.0,
                            ('Cr', 'Ir'): -238.0, ('Cr', 'Pt'): -261.0, ('Au', 'Cr'): 25.0, ('Fe', 'Mn'): 9.0,
                            ('Co', 'Mn'): -19.0, ('Mn', 'Ni'): -115.0, ('Cu', 'Mn'): 29.0, ('Mn', 'Zn'): -25.0,
                            ('Mn', 'Y'): 40.0, ('Mn', 'Zr'): -192.0, ('Mn', 'Nb'): -153.0, ('Mn', 'Mo'): -136.0,
                            ('Mn', 'Ru'): -15.0, ('Mn', 'Rh'): -188.0, ('Mn', 'Pd'): -251.0, ('Ag', 'Mn'): 97.0,
                            ('Cd', 'Mn'): 90.0, ('La', 'Mn'): 129.0, ('Hf', 'Mn'): -268.0, ('Mn', 'Ta'): -254.0,
                            ('Mn', 'W'): -92.0, ('Mn', 'Re'): -139.0, ('Mn', 'Os'): -40.0, ('Ir', 'Mn'): -199.0,
                            ('Mn', 'Pt'): -362.0, ('Au', 'Mn'): -111.0, ('Co', 'Fe'): -60.0, ('Fe', 'Ni'): -97.0,
                            ('Cu', 'Fe'): 65.0, ('Fe', 'Zn'): -23.0, ('Fe', 'Y'): -71.0, ('Fe', 'Zr'): -290.0,
                            ('Fe', 'Nb'): -2505.0, ('Fe', 'Mo'): -484.0, ('Fe', 'Ru'): 41.0, ('Fe', 'Rh'): -57.0,
                            ('Fe', 'Pd'): -116.0, ('Ag', 'Fe'): 176.0, ('Cd', 'Fe'): 159.0, ('Fe', 'La'): 18.0,
                            ('Fe', 'Hf'): -354.0, ('Fe', 'Ta'): -3468.0, ('Fe', 'W'): -554.0, ('Fe', 'Re'): -25.0,
                            ('Fe', 'Os'): 11.0, ('Fe', 'Ir'): -63.0, ('Fe', 'Pt'): -244.0, ('Au', 'Fe'): 70.0,
                            ('Co', 'Ni'): -21.0, ('Co', 'Cu'): 54.0, ('Co', 'Zn'): -58.0, ('Co', 'Y'): -198.0,
                            ('Co', 'Zr'): -324.0, ('Co', 'Nb'): -150.0, ('Co', 'Mo'): -52.0, ('Co', 'Ru'): 52.0,
                            ('Co', 'Rh'): 12.0, ('Co', 'Pd'): -10.0, ('Ag', 'Co'): 154.0, ('Cd', 'Co'): 134.0,
                            ('Co', 'La'): -128.0, ('Co', 'Hf'): -401.0, ('Co', 'Ta'): -253.0, ('Co', 'W'): -84.0,
                            ('Co', 'Re'): -72.0, ('Co', 'Os'): 34.0, ('Co', 'Ir'): 3.0, ('Co', 'Pt'): -107.0,
                            ('Au', 'Co'): 84.0, ('Cu', 'Ni'): -6.0, ('Ni', 'Zn'): -256.0, ('Ni', 'Y'): -437.0,
                            ('Ni', 'Zr'): -463.0, ('Nb', 'Ni'): -316.0, ('Mo', 'Ni'): -100.0, ('Ni', 'Ru'): 40.0,
                            ('Ni', 'Rh'): 2.0, ('Ni', 'Pd'): -6.0, ('Ag', 'Ni'): 98.0, ('Cd', 'Ni'): -14.0,
                            ('La', 'Ni'): -339.0, ('Hf', 'Ni'): -544.0, ('Ni', 'Ta'): -746.0, ('Ni', 'W'): -116.0,
                            ('Ni', 'Re'): -116.0, ('Ni', 'Os'): 32.0, ('Ir', 'Ni'): -38.0, ('Ni', 'Pt'): -99.0,
                            ('Au', 'Ni'): 44.0, ('Cu', 'Zn'): -92.0, ('Cu', 'Y'): -258.0, ('Cu', 'Zr'): -169.0,
                            ('Cu', 'Nb'): -29.0, ('Cu', 'Mo'): 83.0, ('Cu', 'Ru'): 108.0, ('Cu', 'Rh'): -4.0,
                            ('Cu', 'Pd'): -126.0, ('Ag', 'Cu'): 47.0, ('Cd', 'Cu'): 3.0, ('Cu', 'La'): -229.0,
                            ('Cu', 'Hf'): -186.0, ('Cu', 'Ta'): 28.0, ('Cu', 'W'): 129.0, ('Cu', 'Re'): 83.0,
                            ('Cu', 'Os'): 141.0, ('Cu', 'Ir'): 24.0, ('Cu', 'Pt'): -167.0, ('Au', 'Cu'): -49.0,
                            ('Y', 'Zn'): -405.0, ('Zn', 'Zr'): -301.0, ('Nb', 'Zn'): -160.0, ('Mo', 'Zn'): 42.0,
                            ('Ru', 'Zn'): -150.0, ('Rh', 'Zn'): -391.0, ('Pd', 'Zn'): -571.0, ('Ag', 'Zn'): -62.0,
                            ('Cd', 'Zn'): 32.0, ('La', 'Zn'): -374.0, ('Hf', 'Zn'): -233.0, ('Ta', 'Zn'): -88.0,
                            ('W', 'Zn'): 58.0, ('Re', 'Zn'): 8.0, ('Os', 'Zn'): 21.0, ('Ir', 'Zn'): -238.0,
                            ('Pt', 'Zn'): -570.0, ('Au', 'Zn'): -222.0, ('Y', 'Zr'): 40.0, ('Nb', 'Y'): 143.0,
                            ('Mo', 'Y'): 100.0, ('Ru', 'Y'): -318.0, ('Rh', 'Y'): -863.0, ('Pd', 'Y'): -923.0,
                            ('Ag', 'Y'): -346.0, ('Cd', 'Y'): -358.0, ('La', 'Y'): 3.0, ('Hf', 'Y'): 65.0,
                            ('Ta', 'Y'): 181.0, ('W', 'Y'): 148.0, ('Re', 'Y'): -211.0, ('Os', 'Y'): -304.0,
                            ('Ir', 'Y'): -804.0, ('Pt', 'Y'): -1252.0, ('Au', 'Y'): -889.0, ('Nb', 'Zr'): 21.0,
                            ('Mo', 'Zr'): -138.0, ('Ru', 'Zr'): -644.0, ('Rh', 'Zr'): -811.0, ('Pd', 'Zr'): -816.0,
                            ('Ag', 'Zr'): -126.0, ('Cd', 'Zr'): -123.0, ('La', 'Zr'): 99.0, ('Hf', 'Zr'): -22.0,
                            ('Ta', 'Zr'): 36.0, ('W', 'Zr'): -145.0, ('Re', 'Zr'): -358.0, ('Os', 'Zr'): -524.0,
                            ('Ir', 'Zr'): -830.0, ('Pt', 'Zr'): -1087.0, ('Au', 'Zr'): -580.0, ('Mo', 'Nb'): -133.0,
                            ('Nb', 'Ru'): -249.0, ('Nb', 'Rh'): -548.0, ('Nb', 'Pd'): -435.0, ('Ag', 'Nb'): 70.0,
                            ('Cd', 'Nb'): 71.0, ('La', 'Nb'): 145.0, ('Hf', 'Nb'): 23.0, ('Nb', 'Ta'): -10.0,
                            ('Nb', 'W'): -76.0, ('Nb', 'Re'): -202.0, ('Nb', 'Os'): -276.0, ('Ir', 'Nb'): -830.0,
                            ('Nb', 'Pt'): -721.0, ('Au', 'Nb'): -157.0, ('Mo', 'Ru'): -57.0, ('Mo', 'Rh'): -248.0,
                            ('Mo', 'Pd'): -100.0, ('Ag', 'Mo'): 238.0, ('Cd', 'Mo'): 176.0, ('La', 'Mo'): 212.0,
                            ('Hf', 'Mo'): -171.0, ('Mo', 'Ta'): -193.0, ('Mo', 'W'): -8.0, ('Mo', 'Re'): -2.0,
                            ('Mo', 'Os'): -52.0, ('Ir', 'Mo'): -338.0, ('Mo', 'Pt'): -366.0, ('Au', 'Mo'): 141.0,
                            ('Rh', 'Ru'): -8.0, ('Pd', 'Ru'): 47.0, ('Ag', 'Ru'): 203.0, ('Cd', 'Ru'): 112.0,
                            ('La', 'Ru'): -290.0, ('Hf', 'Ru'): -819.0, ('Ru', 'Ta'): -332.0, ('Ru', 'W'): -66.0,
                            ('Re', 'Ru'): -87.0, ('Os', 'Ru'): -16.0, ('Ir', 'Ru'): -54.0, ('Pt', 'Ru'): -33.0,
                            ('Au', 'Ru'): 162.0, ('Pd', 'Rh'): 37.0, ('Ag', 'Rh'): 80.0, ('Cd', 'Rh'): -162.0,
                            ('La', 'Rh'): -790.0, ('Hf', 'Rh'): -864.0, ('Rh', 'Ta'): -611.0, ('Rh', 'W'): -273.0,
                            ('Re', 'Rh'): -181.0, ('Os', 'Rh'): -8.0, ('Ir', 'Rh'): -21.0, ('Pt', 'Rh'): -24.0,
                            ('Au', 'Rh'): 76.0, ('Ag', 'Pd'): -63.0, ('Cd', 'Pd'): -419.0, ('La', 'Pd'): -838.0,
                            ('Hf', 'Pd'): -879.0, ('Pd', 'Ta'): -480.0, ('Pd', 'W'): -123.0, ('Pd', 'Re'): -57.0,
                            ('Os', 'Pd'): 67.0, ('Ir', 'Pd'): 40.0, ('Pd', 'Pt'): -36.0, ('Au', 'Pd'): -95.0,
                            ('Ag', 'Cd'): -66.0, ('Ag', 'La'): -307.0, ('Ag', 'Hf'): -122.0, ('Ag', 'Ta'): 107.0,
                            ('Ag', 'W'): 331.0, ('Ag', 'Re'): 178.0, ('Ag', 'Os'): 257.0, ('Ag', 'Ir'): 171.0,
                            ('Ag', 'Pt'): -39.0, ('Ag', 'Au'): -85.0, ('Cd', 'La'): -381.0, ('Cd', 'Hf'): -84.0,
                            ('Cd', 'Ta'): 94.0, ('Cd', 'W'): 286.0, ('Cd', 'Re'): 154.0, ('Cd', 'Os'): 220.0,
                            ('Cd', 'Ir'): 23.0, ('Cd', 'Pt'): -320.0, ('Au', 'Cd'): -182.0, ('Hf', 'La'): 114.0,
                            ('La', 'Ta'): 166.0, ('La', 'W'): 299.0, ('La', 'Re'): 76.0, ('La', 'Os'): -162.0,
                            ('Ir', 'La'): -735.0, ('La', 'Pt'): -1198.0, ('Au', 'La'): -837.0, ('Hf', 'Ta'): 49.0,
                            ('Hf', 'W'): -171.0, ('Hf', 'Re'): -407.0, ('Hf', 'Os'): -709.0, ('Hf', 'Ir'): -949.0,
                            ('Hf', 'Pt'): -1155.0, ('Au', 'Hf'): -566.0, ('Ta', 'W'): -114.0, ('Re', 'Ta'): -226.0,
                            ('Os', 'Ta'): -330.0, ('Ir', 'Ta'): -688.0, ('Pt', 'Ta'): -758.0, ('Au', 'Ta'): -93.0,
                            ('Re', 'W'): 7.0, ('Os', 'W'): -56.0, ('Ir', 'W'): -350.0, ('Pt', 'W'): -343.0,
                            ('Au', 'W'): 232.0, ('Os', 'Re'): -89.0, ('Ir', 'Re'): -274.0, ('Pt', 'Re'): -232.0,
                            ('Au', 'Re'): 166.0, ('Ir', 'Os'): -8.0, ('Os', 'Pt'): 22.0, ('Au', 'Os'): 232.0,
                            ('Ir', 'Pt'): 11.0, ('Au', 'Ir'): 154.0, ('Au', 'Pt'): 8.0}

formation_enthalpy_data_elements = ['Mg', 'Al', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                                    'Y', 'Zr', 'Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'La', 'Hf', 'Ta',
                                    'W', 'Re', 'Os', 'Ir', 'Pt', 'Au']


def FormationEnthalpy(pair=None):
    """Function to return the Pair Formation Enthalpy of a element-pair

    Parameters
    ----------
    pair : tuple or list, optional
        The element pair for which the Pair Formation Enthalpy should be returned, by default None

    Returns
    -------
    float or str
        The Pair Formation Enthalpy, if the pair exists in the database, 'NaN' otherwise.


    References
    ----------
    M.C. Troparevsky, J.R. Morris, P.R.C. Kent, A.R. Lupini, G.M. Stocks, Phys. Rev. X 5 (1) (2015) 011041.
    """
    _pair = tuple(sorted(pair))

    if _pair is None:
        print("Usage: FormationEnthalpy(('X1', 'X2')) where X1 and X2 are element names.")
    elif _pair in _formation_enthalpy_data.keys():
        return _formation_enthalpy_data[_pair]
    else:
        return "NaN"
