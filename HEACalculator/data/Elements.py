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

_element_data = {
        "H": {
                "atomic_number": 1.0,
                "melting_point": 14.01,
                "atomic_volume": 14.1,
                "atomic_weight": 1.008,
                "atomic_radius": 38.0,
                "nvalence": 1.0
        },
        "He": {
                "atomic_number": 2.0,
                "melting_point": 0.95,
                "atomic_volume": 31.8,
                "atomic_weight": 4.002602,
                "atomic_radius": 32.0,
                "nvalence": 2.0
        },
        "Li": {
                "atomic_number": 3.0,
                "melting_point": 553.69,
                "atomic_volume": 13.1,
                "atomic_weight": 6.94,
                "atomic_radius": 152.0,
                "nvalence": 1.0
        },
        "Be": {
                "atomic_number": 4.0,
                "melting_point": 1551.0,
                "atomic_volume": 5.0,
                "atomic_weight": 9.0121831,
                "atomic_radius": 112.0,
                "nvalence": 2.0
        },
        "B": {
                "atomic_number": 5.0,
                "melting_point": 2573.0,
                "atomic_volume": 4.6,
                "atomic_weight": 10.81,
                "atomic_radius": 82.0,
                "nvalence": 3.0
        },
        "C": {
                "atomic_number": 6.0,
                "melting_point": 3820.0,
                "atomic_volume": 5.3,
                "atomic_weight": 12.011,
                "atomic_radius": 77.0,
                "nvalence": 4.0
        },
        "N": {
                "atomic_number": 7.0,
                "melting_point": 63.29,
                "atomic_volume": 17.3,
                "atomic_weight": 14.007,
                "atomic_radius": 75.0,
                "nvalence": 5.0
        },
        "O": {
                "atomic_number": 8.0,
                "melting_point": 54.8,
                "atomic_volume": 14.0,
                "atomic_weight": 15.999,
                "atomic_radius": 73.0,
                "nvalence": 6.0
        },
        "F": {
                "atomic_number": 9.0,
                "melting_point": 53.53,
                "atomic_volume": 17.1,
                "atomic_weight": 18.998403163,
                "atomic_radius": 71.0,
                "nvalence": 7.0
        },
        "Ne": {
                "atomic_number": 10.0,
                "melting_point": 48.0,
                "atomic_volume": 16.8,
                "atomic_weight": 20.1797,
                "atomic_radius": 154.0,
                "nvalence": 8.0
        },
        "Na": {
                "atomic_number": 11.0,
                "melting_point": 370.96,
                "atomic_volume": 23.7,
                "atomic_weight": 22.98976928,
                "atomic_radius": 186.0,
                "nvalence": 1.0
        },
        "Mg": {
                "atomic_number": 12.0,
                "melting_point": 922.0,
                "atomic_volume": 14.0,
                "atomic_weight": 24.305,
                "atomic_radius": 160.0,
                "nvalence": 2.0
        },
        "Al": {
                "atomic_number": 13.0,
                "melting_point": 933.5,
                "atomic_volume": 10.0,
                "atomic_weight": 26.9815385,
                "atomic_radius": 143.0,
                "nvalence": 3.0
        },
        "Si": {
                "atomic_number": 14.0,
                "melting_point": 1683.0,
                "atomic_volume": 12.1,
                "atomic_weight": 28.085,
                "atomic_radius": 111.0,
                "nvalence": 4.0
        },
        "P": {
                "atomic_number": 15.0,
                "melting_point": 317.3,
                "atomic_volume": 17.0,
                "atomic_weight": 30.973761998,
                "atomic_radius": 106.0,
                "nvalence": 5.0
        },
        "S": {
                "atomic_number": 16.0,
                "melting_point": 386.0,
                "atomic_volume": 15.5,
                "atomic_weight": 32.06,
                "atomic_radius": 102.0,
                "nvalence": 6.0
        },
        "Cl": {
                "atomic_number": 17.0,
                "melting_point": 172.2,
                "atomic_volume": 18.7,
                "atomic_weight": 35.45,
                "atomic_radius": 99.0,
                "nvalence": 7.0
        },
        "Ar": {
                "atomic_number": 18.0,
                "melting_point": 83.8,
                "atomic_volume": 24.2,
                "atomic_weight": 39.948,
                "atomic_radius": 188.0,
                "nvalence": 8.0
        },
        "K": {
                "atomic_number": 19.0,
                "melting_point": 336.8,
                "atomic_volume": 45.3,
                "atomic_weight": 39.0983,
                "atomic_radius": 227.0,
                "nvalence": 1.0
        },
        "Ca": {
                "atomic_number": 20.0,
                "melting_point": 1112.0,
                "atomic_volume": 29.9,
                "atomic_weight": 40.078,
                "atomic_radius": 197.0,
                "nvalence": 2.0
        },
        "Sc": {
                "atomic_number": 21.0,
                "melting_point": 1814.0,
                "atomic_volume": 15.0,
                "atomic_weight": 44.955908,
                "atomic_radius": 162.0,
                "nvalence": 3.0
        },
        "Ti": {
                "atomic_number": 22.0,
                "melting_point": 1933.0,
                "atomic_volume": 10.6,
                "atomic_weight": 47.867,
                "atomic_radius": 147.0,
                "nvalence": 4.0
        },
        "V": {
                "atomic_number": 23.0,
                "melting_point": 2160.0,
                "atomic_volume": 8.35,
                "atomic_weight": 50.9415,
                "atomic_radius": 134.0,
                "nvalence": 5.0
        },
        "Cr": {
                "atomic_number": 24.0,
                "melting_point": 2130.0,
                "atomic_volume": 7.23,
                "atomic_weight": 51.9961,
                "atomic_radius": 128.0,
                "nvalence": 6.0
        },
        "Mn": {
                "atomic_number": 25.0,
                "melting_point": 1517.0,
                "atomic_volume": 7.39,
                "atomic_weight": 54.938044,
                "atomic_radius": 127.0,
                "nvalence": 7.0
        },
        "Fe": {
                "atomic_number": 26.0,
                "melting_point": 1808.0,
                "atomic_volume": 7.1,
                "atomic_weight": 55.845,
                "atomic_radius": 126.0,
                "nvalence": 8.0
        },
        "Co": {
                "atomic_number": 27.0,
                "melting_point": 1768.0,
                "atomic_volume": 6.7,
                "atomic_weight": 58.933194,
                "atomic_radius": 125.0,
                "nvalence": 9.0
        },
        "Ni": {
                "atomic_number": 28.0,
                "melting_point": 1726.0,
                "atomic_volume": 6.6,
                "atomic_weight": 58.6934,
                "atomic_radius": 124.0,
                "nvalence": 10.0
        },
        "Cu": {
                "atomic_number": 29.0,
                "melting_point": 1356.6,
                "atomic_volume": 7.1,
                "atomic_weight": 63.546,
                "atomic_radius": 128.0,
                "nvalence": 11.0
        },
        "Zn": {
                "atomic_number": 30.0,
                "melting_point": 692.73,
                "atomic_volume": 9.2,
                "atomic_weight": 65.38,
                "atomic_radius": 134.0,
                "nvalence": 12.0
        },
        "Ga": {
                "atomic_number": 31.0,
                "melting_point": 302.93,
                "atomic_volume": 11.8,
                "atomic_weight": 69.723,
                "atomic_radius": 135.0,
                "nvalence": 3.0
        },
        "Ge": {
                "atomic_number": 32.0,
                "melting_point": 1210.6,
                "atomic_volume": 13.6,
                "atomic_weight": 72.63,
                "atomic_radius": 122.0,
                "nvalence": 4.0
        },
        "As": {
                "atomic_number": 33.0,
                "melting_point": 1090.0,
                "atomic_volume": 13.1,
                "atomic_weight": 74.921595,
                "atomic_radius": 119.0,
                "nvalence": 5.0
        },
        "Se": {
                "atomic_number": 34.0,
                "melting_point": 490.0,
                "atomic_volume": 16.5,
                "atomic_weight": 78.971,
                "atomic_radius": 116.0,
                "nvalence": 6.0
        },
        "Br": {
                "atomic_number": 35.0,
                "melting_point": 265.9,
                "atomic_volume": 23.5,
                "atomic_weight": 79.904,
                "atomic_radius": 114.0,
                "nvalence": 7.0
        },
        "Kr": {
                "atomic_number": 36.0,
                "melting_point": 116.6,
                "atomic_volume": 32.2,
                "atomic_weight": 83.798,
                "atomic_radius": 202.0,
                "nvalence": 8.0
        },
        "Rb": {
                "atomic_number": 37.0,
                "melting_point": 312.2,
                "atomic_volume": 55.9,
                "atomic_weight": 85.4678,
                "atomic_radius": 248.0,
                "nvalence": 1.0
        },
        "Sr": {
                "atomic_number": 38.0,
                "melting_point": 1042.0,
                "atomic_volume": 33.7,
                "atomic_weight": 87.62,
                "atomic_radius": 215.0,
                "nvalence": 2.0
        },
        "Y": {
                "atomic_number": 39.0,
                "melting_point": 1795.0,
                "atomic_volume": 19.8,
                "atomic_weight": 88.90584,
                "atomic_radius": 180.0,
                "nvalence": 3.0
        },
        "Zr": {
                "atomic_number": 40.0,
                "melting_point": 2125.0,
                "atomic_volume": 14.1,
                "atomic_weight": 91.224,
                "atomic_radius": 160.0,
                "nvalence": 4.0
        },
        "Nb": {
                "atomic_number": 41.0,
                "melting_point": 2741.0,
                "atomic_volume": 10.8,
                "atomic_weight": 92.90637,
                "atomic_radius": 146.0,
                "nvalence": 5.0
        },
        "Mo": {
                "atomic_number": 42.0,
                "melting_point": 2890.0,
                "atomic_volume": 9.4,
                "atomic_weight": 95.95,
                "atomic_radius": 139.0,
                "nvalence": 6.0
        },
        "Tc": {
                "atomic_number": 43.0,
                "melting_point": 2445.0,
                "atomic_volume": 8.5,
                "atomic_weight": 97.90721,
                "atomic_radius": 136.0,
                "nvalence": 7.0
        },
        "Ru": {
                "atomic_number": 44.0,
                "melting_point": 2583.0,
                "atomic_volume": 8.3,
                "atomic_weight": 101.07,
                "atomic_radius": 134.0,
                "nvalence": 8.0
        },
        "Rh": {
                "atomic_number": 45.0,
                "melting_point": 2239.0,
                "atomic_volume": 8.3,
                "atomic_weight": 102.9055,
                "atomic_radius": 134.0,
                "nvalence": 9.0
        },
        "Pd": {
                "atomic_number": 46.0,
                "melting_point": 1825.0,
                "atomic_volume": 8.9,
                "atomic_weight": 106.42,
                "atomic_radius": 137.0,
                "nvalence": 12.0
        },
        "Ag": {
                "atomic_number": 47.0,
                "melting_point": 1235.1,
                "atomic_volume": 10.3,
                "atomic_weight": 107.8682,
                "atomic_radius": 144.0,
                "nvalence": 11.0
        },
        "Cd": {
                "atomic_number": 48.0,
                "melting_point": 594.1,
                "atomic_volume": 13.1,
                "atomic_weight": 112.414,
                "atomic_radius": 151.0,
                "nvalence": 12.0
        },
        "In": {
                "atomic_number": 49.0,
                "melting_point": 429.32,
                "atomic_volume": 15.7,
                "atomic_weight": 114.818,
                "atomic_radius": 167.0,
                "nvalence": 3.0
        },
        "Sn": {
                "atomic_number": 50.0,
                "melting_point": 505.1,
                "atomic_volume": 16.3,
                "atomic_weight": 118.71,
                "atomic_radius": 145.0,
                "nvalence": 4.0
        },
        "Sb": {
                "atomic_number": 51.0,
                "melting_point": 903.9,
                "atomic_volume": 18.4,
                "atomic_weight": 121.76,
                "atomic_radius": 145.0,
                "nvalence": 5.0
        },
        "Te": {
                "atomic_number": 52.0,
                "melting_point": 722.7,
                "atomic_volume": 20.5,
                "atomic_weight": 127.6,
                "atomic_radius": 140.0,
                "nvalence": 6.0
        },
        "I": {
                "atomic_number": 53.0,
                "melting_point": 386.7,
                "atomic_volume": 25.7,
                "atomic_weight": 126.90447,
                "atomic_radius": 133.0,
                "nvalence": 7.0
        },
        "Xe": {
                "atomic_number": 54.0,
                "melting_point": 161.3,
                "atomic_volume": 42.9,
                "atomic_weight": 131.293,
                "atomic_radius": 216.0,
                "nvalence": 8.0
        },
        "Cs": {
                "atomic_number": 55.0,
                "melting_point": 301.6,
                "atomic_volume": 70.0,
                "atomic_weight": 132.90545196,
                "atomic_radius": 265.0,
                "nvalence": 1.0
        },
        "Ba": {
                "atomic_number": 56.0,
                "melting_point": 1002.0,
                "atomic_volume": 39.0,
                "atomic_weight": 137.327,
                "atomic_radius": 222.0,
                "nvalence": 2.0
        },
        "La": {
                "atomic_number": 57.0,
                "melting_point": 1194.0,
                "atomic_volume": 22.5,
                "atomic_weight": 138.90547,
                "atomic_radius": 187.0,
                "nvalence": 3.0
        },
        "Ce": {
                "atomic_number": 58.0,
                "melting_point": 1072.0,
                "atomic_volume": 21.0,
                "atomic_weight": 140.116,
                "atomic_radius": 181.8,
                "nvalence": 2.0
        },
        "Pr": {
                "atomic_number": 59.0,
                "melting_point": 1204.0,
                "atomic_volume": 20.8,
                "atomic_weight": 140.90766,
                "atomic_radius": 182.4,
                "nvalence": 2.0
        },
        "Nd": {
                "atomic_number": 60.0,
                "melting_point": 1294.0,
                "atomic_volume": 20.6,
                "atomic_weight": 144.242,
                "atomic_radius": 181.4,
                "nvalence": 2.0
        },
        "Pm": {
                "atomic_number": 61.0,
                "melting_point": 1441.0,
                "atomic_volume": "NaN",
                "atomic_weight": 144.91276,
                "atomic_radius": 183.4,
                "nvalence": 2.0
        },
        "Sm": {
                "atomic_number": 62.0,
                "melting_point": 1350.0,
                "atomic_volume": 19.9,
                "atomic_weight": 150.36,
                "atomic_radius": 180.4,
                "nvalence": 2.0
        },
        "Eu": {
                "atomic_number": 63.0,
                "melting_point": 1095.0,
                "atomic_volume": 28.9,
                "atomic_weight": 151.964,
                "atomic_radius": 180.4,
                "nvalence": 2.0
        },
        "Gd": {
                "atomic_number": 64.0,
                "melting_point": 1586.0,
                "atomic_volume": 19.9,
                "atomic_weight": 157.25,
                "atomic_radius": 180.4,
                "nvalence": 2.0
        },
        "Tb": {
                "atomic_number": 65.0,
                "melting_point": 1629.0,
                "atomic_volume": 19.2,
                "atomic_weight": 158.92535,
                "atomic_radius": 177.3,
                "nvalence": 2.0
        },
        "Dy": {
                "atomic_number": 66.0,
                "melting_point": 1685.0,
                "atomic_volume": 19.0,
                "atomic_weight": 162.5,
                "atomic_radius": 178.1,
                "nvalence": 2.0
        },
        "Ho": {
                "atomic_number": 67.0,
                "melting_point": 1747.0,
                "atomic_volume": 18.7,
                "atomic_weight": 164.93033,
                "atomic_radius": 176.2,
                "nvalence": 2.0
        },
        "Er": {
                "atomic_number": 68.0,
                "melting_point": 1802.0,
                "atomic_volume": 18.4,
                "atomic_weight": 167.259,
                "atomic_radius": 176.1,
                "nvalence": 2.0
        },
        "Tm": {
                "atomic_number": 69.0,
                "melting_point": 1818.0,
                "atomic_volume": 18.1,
                "atomic_weight": 168.93422,
                "atomic_radius": 175.9,
                "nvalence": 2.0
        },
        "Yb": {
                "atomic_number": 70.0,
                "melting_point": 1097.0,
                "atomic_volume": 24.8,
                "atomic_weight": 173.045,
                "atomic_radius": 176.0,
                "nvalence": 2.0
        },
        "Lu": {
                "atomic_number": 71.0,
                "melting_point": 1936.0,
                "atomic_volume": 17.8,
                "atomic_weight": 174.9668,
                "atomic_radius": 173.8,
                "nvalence": 2.0
        },
        "Hf": {
                "atomic_number": 72.0,
                "melting_point": 2503.0,
                "atomic_volume": 13.6,
                "atomic_weight": 178.49,
                "atomic_radius": 159.0,
                "nvalence": 4.0
        },
        "Ta": {
                "atomic_number": 73.0,
                "melting_point": 3269.0,
                "atomic_volume": 10.9,
                "atomic_weight": 180.94788,
                "atomic_radius": 146.0,
                "nvalence": 5.0
        },
        "W": {
                "atomic_number": 74.0,
                "melting_point": 3680.0,
                "atomic_volume": 9.53,
                "atomic_weight": 183.84,
                "atomic_radius": 139.0,
                "nvalence": 6.0
        },
        "Re": {
                "atomic_number": 75.0,
                "melting_point": 3453.0,
                "atomic_volume": 8.85,
                "atomic_weight": 186.207,
                "atomic_radius": 137.0,
                "nvalence": 7.0
        },
        "Os": {
                "atomic_number": 76.0,
                "melting_point": 3327.0,
                "atomic_volume": 8.43,
                "atomic_weight": 190.23,
                "atomic_radius": 135.0,
                "nvalence": 8.0
        },
        "Ir": {
                "atomic_number": 77.0,
                "melting_point": 2683.0,
                "atomic_volume": 8.54,
                "atomic_weight": 192.217,
                "atomic_radius": 135.5,
                "nvalence": 9.0
        },
        "Pt": {
                "atomic_number": 78.0,
                "melting_point": 2045.0,
                "atomic_volume": 9.1,
                "atomic_weight": 195.084,
                "atomic_radius": 138.5,
                "nvalence": 10.0
        },
        "Au": {
                "atomic_number": 79.0,
                "melting_point": 1337.58,
                "atomic_volume": 10.2,
                "atomic_weight": 196.966569,
                "atomic_radius": 144.0,
                "nvalence": 11.0
        },
        "Hg": {
                "atomic_number": 80.0,
                "melting_point": 234.28,
                "atomic_volume": 14.8,
                "atomic_weight": 200.592,
                "atomic_radius": 151.0,
                "nvalence": 12.0
        },
        "Tl": {
                "atomic_number": 81.0,
                "melting_point": 576.6,
                "atomic_volume": 17.2,
                "atomic_weight": 204.38,
                "atomic_radius": 170.0,
                "nvalence": 3.0
        },
        "Pb": {
                "atomic_number": 82.0,
                "melting_point": 600.65,
                "atomic_volume": 18.3,
                "atomic_weight": 207.2,
                "atomic_radius": 180.0,
                "nvalence": 4.0
        },
        "Bi": {
                "atomic_number": 83.0,
                "melting_point": 544.5,
                "atomic_volume": 21.3,
                "atomic_weight": 208.9804,
                "atomic_radius": 160.0,
                "nvalence": 5.0
        },
        "Po": {
                "atomic_number": 84.0,
                "melting_point": 527.0,
                "atomic_volume": 22.7,
                "atomic_weight": 209.0,
                "atomic_radius": 190.0,
                "nvalence": 6.0
        },
        "At": {
                "atomic_number": 85.0,
                "melting_point": 575.0,
                "atomic_volume": "NaN",
                "atomic_weight": 210.0,
                "atomic_radius": 202.0,
                "nvalence": 7.0
        },
        "Rn": {
                "atomic_number": 86.0,
                "melting_point": 202.0,
                "atomic_volume": "NaN",
                "atomic_weight": 222.0,
                "atomic_radius": 220.0,
                "nvalence": 8.0
        },
        "Fr": {
                "atomic_number": 87.0,
                "melting_point": 300.0,
                "atomic_volume": "NaN",
                "atomic_weight": 223.0,
                "atomic_radius": 348.0,
                "nvalence": 1.0
        },
        "Ra": {
                "atomic_number": 88.0,
                "melting_point": 973.0,
                "atomic_volume": 45.0,
                "atomic_weight": 226.0,
                "atomic_radius": 215.0,
                "nvalence": 2.0
        },
        "Ac": {
                "atomic_number": 89.0,
                "melting_point": 1320.0,
                "atomic_volume": 22.54,
                "atomic_weight": 227.0,
                "atomic_radius": 195.0,
                "nvalence": 3.0
        },
        "Th": {
                "atomic_number": 90.0,
                "melting_point": 2028.0,
                "atomic_volume": 19.8,
                "atomic_weight": 232.0377,
                "atomic_radius": 179.0,
                "nvalence": 2.0
        },
        "Pa": {
                "atomic_number": 91.0,
                "melting_point": 2113.0,
                "atomic_volume": 15.0,
                "atomic_weight": 231.03588,
                "atomic_radius": 163.0,
                "nvalence": 2.0
        },
        "U": {
                "atomic_number": 92.0,
                "melting_point": 1405.5,
                "atomic_volume": 12.5,
                "atomic_weight": 238.02891,
                "atomic_radius": 156.0,
                "nvalence": 2.0
        },
        "Np": {
                "atomic_number": 93.0,
                "melting_point": 913.0,
                "atomic_volume": 21.1,
                "atomic_weight": 237.0,
                "atomic_radius": 155.0,
                "nvalence": 2.0
        },
        "Pu": {
                "atomic_number": 94.0,
                "melting_point": 914.0,
                "atomic_volume": "NaN",
                "atomic_weight": 244.0,
                "atomic_radius": 159.0,
                "nvalence": 2.0
        },
        "Am": {
                "atomic_number": 95.0,
                "melting_point": 1267.0,
                "atomic_volume": 20.8,
                "atomic_weight": 243.0,
                "atomic_radius": 173.0,
                "nvalence": 2.0
        },
        "Cm": {
                "atomic_number": 96.0,
                "melting_point": 1340.0,
                "atomic_volume": 18.28,
                "atomic_weight": 247.0,
                "atomic_radius": 174.0,
                "nvalence": 2.0
        },
        "Bk": {
                "atomic_number": 97.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 247.0,
                "atomic_radius": 170.0,
                "nvalence": 2.0
        },
        "Cf": {
                "atomic_number": 98.0,
                "melting_point": 900.0,
                "atomic_volume": "NaN",
                "atomic_weight": 251.0,
                "atomic_radius": 186.0,
                "nvalence": 2.0
        },
        "Es": {
                "atomic_number": 99.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 252.0,
                "atomic_radius": 186.0,
                "nvalence": 2.0
        },
        "Fm": {
                "atomic_number": 100.0,
                "melting_point": 1800.0,
                "atomic_volume": "NaN",
                "atomic_weight": 257.0,
                "atomic_radius": "NaN",
                "nvalence": 2.0
        },
        "Md": {
                "atomic_number": 101.0,
                "melting_point": 1100.0,
                "atomic_volume": "NaN",
                "atomic_weight": 258.0,
                "atomic_radius": "NaN",
                "nvalence": 2.0
        },
        "No": {
                "atomic_number": 102.0,
                "melting_point": 1100.0,
                "atomic_volume": "NaN",
                "atomic_weight": 259.0,
                "atomic_radius": "NaN",
                "nvalence": 2.0
        },
        "Lr": {
                "atomic_number": 103.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 262.0,
                "atomic_radius": "NaN",
                "nvalence": 2.0
        },
        "Rf": {
                "atomic_number": 104.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 267.0,
                "atomic_radius": 131.0,
                "nvalence": 4.0
        },
        "Db": {
                "atomic_number": 105.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 268.0,
                "atomic_radius": 126.0,
                "nvalence": 5.0
        },
        "Sg": {
                "atomic_number": 106.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 271.0,
                "atomic_radius": 121.0,
                "nvalence": 6.0
        },
        "Bh": {
                "atomic_number": 107.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 274.0,
                "atomic_radius": 119.0,
                "nvalence": 7.0
        },
        "Hs": {
                "atomic_number": 108.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 269.0,
                "atomic_radius": 118.0,
                "nvalence": 8.0
        },
        "Mt": {
                "atomic_number": 109.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 276.0,
                "atomic_radius": 113.0,
                "nvalence": 9.0
        },
        "Ds": {
                "atomic_number": 110.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 281.0,
                "atomic_radius": 112.0,
                "nvalence": 10.0
        },
        "Rg": {
                "atomic_number": 111.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 281.0,
                "atomic_radius": 118.0,
                "nvalence": 11.0
        },
        "Cn": {
                "atomic_number": 112.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 285.0,
                "atomic_radius": 130.0,
                "nvalence": 12.0
        },
        "Nh": {
                "atomic_number": 113.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 286.0,
                "atomic_radius": "NaN",
                "nvalence": 3.0
        },
        "Fl": {
                "atomic_number": 114.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 289.0,
                "atomic_radius": "NaN",
                "nvalence": 4.0
        },
        "Mc": {
                "atomic_number": 115.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 288.0,
                "atomic_radius": "NaN",
                "nvalence": 5.0
        },
        "Lv": {
                "atomic_number": 116.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 293.0,
                "atomic_radius": "NaN",
                "nvalence": 6.0
        },
        "Ts": {
                "atomic_number": 117.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 294.0,
                "atomic_radius": "NaN",
                "nvalence": 7.0
        },
        "Og": {
                "atomic_number": 118.0,
                "melting_point": "NaN",
                "atomic_volume": "NaN",
                "atomic_weight": 294.0,
                "atomic_radius": "NaN",
                "nvalence": 8.0
        }
}


class _Element:
    """Element class for storing element properties.

    Attributes
    ----------
    
    symbol : str
        Chemical symbol
    nvalence : int
        Number of valence electrons
    melting_point : float
        Melting temperature
    atomic_number : int
        Atomic number
    atomic_volume : float
        Atomic volume in cm^3/mol
    atomic_weight : float
        Relative atomic weight [weight]_
    atomic_radius : float
        Atomic radius in pm [radius]_

    References
    ----------
    .. [weight] IUPAC-CIAAW. Standard atomic weights. URL: http://www.ciaaw.org/atomic-weights.htm.
    .. [radius] John C Slater. Atomic Radii in Crystals. The Journal of Chemical Physics, 41(10):3199, 1964. URL: http://scitation.aip.org/content/aip/journal/jcp/41/10/10.1063/1.1725697, doi:10.1063/1.1725697.
    """

    def __init__(self, symbol, melting_point, atomic_number, atomic_volume, atomic_weight, atomic_radius, nvalence):
        self.symbol = symbol
        self.melting_point = melting_point
        self.atomic_number = atomic_number
        self.atomic_volume = atomic_volume
        self.atomic_weight = atomic_weight
        self.atomic_radius = atomic_radius
        self.nvalence = nvalence

    def __getattribute__(self, symbol):
        try:
            return super(_Element, self).__getattribute__(symbol)
        except AttributeError:
            print(f"Object has no attribute '{symbol}'")

    def __getitem__(self, key):
        return self.__dict__.get(key)

    def __repr__(self):
        return f'\n{self.symbol}\n'\
               f'\tMelting point: {self.melting_point} K\n'\
               f'\tAtomic number: {self.atomic_number}\n'\
               f'\tAtomic volume: {self.atomic_volume} cm^3/mol\n'\
               f'\tAtomic weight: {self.atomic_weight}\n'\
               f'\tAtomic radius: {self.atomic_radius} pm\n'\
               f'\tValence electrons: {self.nvalence}\n'


_elements = {x: _Element(x, _element_data[x]['melting_point'], _element_data[x]['atomic_number'], _element_data[x]['atomic_volume'],
                         _element_data[x]['atomic_weight'], _element_data[x]['atomic_radius'], _element_data[x]['nvalence']) for x in _element_data}
globals().update(_elements)

__all__ = list(_elements.keys())
