import unittest
import numpy as np
from labpartner.moduleLSFR import linfit, quadfit


class Testlinfit(unittest.TestCase):

    def test_calculate_chi_squared(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 6])
        yerr = np.array([0.1, 0.2, 0.3])
        m = 2
        c = 0
        expected_chi_squared = 0
        actual_chi_squared = linfit.calculate_chi_squared(x, y, yerr, m, c)
        self.assertAlmostEqual(expected_chi_squared, actual_chi_squared)

    def test_calculate_reduced_chi_squared(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 6])
        yerr = np.array([0.1, 0.2, 0.3])
        m = 2
        c = 0
        expected_reduced_chi_squared = 0
        actual_reduced_chi_squared = linfit.calculate_reduced_chi_squared(x, y, yerr, m, c)
        self.assertAlmostEqual(expected_reduced_chi_squared, actual_reduced_chi_squared)

    def test_do_linear_fit(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 6])
        yerr = np.array([0.1, 0.2, 0.3])
        output = linfit.do_linear_fit(x, y, yerr)
        self.assertEqual(len(output), 5)
        self.assertAlmostEqual(output[0], 2, places=1)
        self.assertAlmostEqual(output[2], 0, places=1)

class Testquadfit(unittest.TestCase):

    def test_calculate_chi_squared(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([1, 4, 9, 16])
        yerr = np.array([0.1, 0.2, 0.3, 0.4])
        a = 1
        b = 0
        c = 0
        expected_chi_squared = 0
        actual_chi_squared = quadfit.calculate_chi_squared(x, y, yerr, a, b, c)
        self.assertAlmostEqual(expected_chi_squared, actual_chi_squared)

    def test_calculate_reduced_chi_squared(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([1, 4, 9, 16])
        yerr = np.array([0.1, 0.2, 0.3, 0.4])
        a = 1
        b = 0
        c = 0
        expected_reduced_chi_squared = 0
        actual_reduced_chi_squared = quadfit.calculate_reduced_chi_squared(x, y, yerr, a, b, c)
        self.assertAlmostEqual(expected_reduced_chi_squared, actual_reduced_chi_squared)

    def test_do_quadratic_fit(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([1, 4, 9, 16])
        yerr = np.array([0.1, 0.2, 0.3, 0.4])
        output = quadfit.do_quadratic_fit(x, y, yerr)
        self.assertEqual(len(output), 7)
        self.assertAlmostEqual(output[0], 1, places=1)
        self.assertAlmostEqual(output[2], 0, places=1)
        self.assertAlmostEqual(output[4], 0, places=1)


if __name__ == '__main__':
    unittest.main()
