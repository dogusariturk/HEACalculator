import numpy as np
from scipy import constants
from mendeleev import element
from pymatgen import Element
from mixing import __df
from thermo import nested_formula_parser, atom_fractions, mass_fractions, molecular_weight
from thermo.utils import ws_to_zs

# inp = input('Alloy: ')

atoms = nested_formula_parser('AlTiVMnSi')

# afracs = atom_fractions(atoms)
# ws = (mass_fractions(atoms))


def main():

    def configurationalEntropy(atoms):
        if len(set(atoms.values())) == 1:
            return constants.R * np.log(len(atoms))
        else:
            pass

    def averageAtomicRadius(atoms):
        sumAtomicRadius = sum(
            Element(x).atomic_radius_calculated for x in atoms)
        return sumAtomicRadius / len(atoms)

    def valanceElectronConcentration(atoms):
        sumVEC = sum(element(x).nvalence() for x in atoms)
        return sumVEC / len(atoms)

    print('\n\t S_conf = {} J/K mol'.format(configurationalEntropy(atoms)))
    print('\t H_mixing = {} J/mol'.format(enthalpyOfMixing(atoms)))
    print('\t delta = {} %'.format(atomicSizeDifference(atoms)))
    print('\t VEC = {}'.format(valanceElectronConcentration(atoms)))


if __name__ == '__main__':
    main()
