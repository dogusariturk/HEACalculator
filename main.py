from mendeleev import element
from pymatgen import Element


def main():

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
