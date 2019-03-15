import numpy as np
import pandas as pd


__HEADER = ['H', 'Li', 'Be', 'B', 'C', 'N', 'Na', 'Mg', 'Al', 'Si', 'P', 'K', 'Ca',
            'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge',
            'As', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag',
            'Cd', 'In', 'Sn', 'Sb', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
            'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
            'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Th',
            'U', 'Pu']

__data = pd.read_csv('mixing.csv', names=__HEADER)
__df = pd.DataFrame(np.triu(__data) + np.triu(__data, 1).T,
                    index=__HEADER, columns=__HEADER)
