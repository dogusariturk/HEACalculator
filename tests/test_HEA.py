from unittest import TestCase

from HEACalculator.core.HEA import HEACalculator


class TestHEACalculator(TestCase):

    def setUp(self):
        self.res = HEACalculator('FeCoCrNi')
        self.res.calculate()

    # def test_calculate(self):
    #     b = ['FeCoCrNi', '8.16', '1.82', '-3.75', '8.25', '11.53', '1858.00', '5.71', 'FCC', 'Yes']

    def test_formula(self):
        self.assertEqual(self.res.formula, 'FeCoCrNi')

    def test_mixing_enthalpy(self):
        self.assertEqual(self.res.mixing_enthalpy, -3.75)

    # def test_formation_enthalpy(self):
    #     self.assertEqual(self.res.formation_enthalpy)

    def test_density(self):
        self.assertAlmostEqual(self.res.density, 8.16, 2)

    def test_valance_electron_concentration(self):
        self.assertAlmostEqual(self.res.valance_electron_concentration, 8.25, 2)

    def test_melting_temperature(self):
        self.assertEqual(self.res.melting_temperature, 1858)

    def test_atomic_size_difference(self):
        self.assertAlmostEqual(self.res.atomic_size_difference, 1.82, 2)

    # def test_min_formation_enthalpy(self):
    #     self.assertEqual(self.res.min_formation_enthalpy)

    def test_mixing_entropy(self):
        self.assertAlmostEqual(self.res.mixing_entropy, 11.53, 2)

    def test_microstructure(self):
        self.assertEqual(self.res.microstructure, 'FCC')

    # def test_gamma_parameter(self):
    #     self.assertEqual(self.res.gamma_parameter)

    def test_omega_parameter(self):
        self.assertAlmostEqual(self.res.omega_parameter, 5.71, 2)

    # def test_lambda_parameter(self):
    #     self.assertEqual(self.res.lambda_parameter)
    #
    # def test_phi_parameter(self):
    #     self.assertEqual(self.res.phi_parameter)
