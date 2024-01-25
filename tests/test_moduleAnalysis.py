import unittest
from unittest.mock import patch
import numpy as np
import labpartner_uom as lp
import os

class TestAnalyse(unittest.TestCase):

    @patch('labpartner_uom.moduleAnalysis.analysis')
    def test_analyse(self, mock_plot):
        # Test with fit="Linear"
        lp.analyse([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], fit="Linear")
        mock_plot.assert_called_with([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], "A*x + B")

        # Test with fit="Quadratic"
        lp.analyse([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], fit="Quadratic")
        mock_plot.assert_called_with([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], "A*x**2 + B*x + C")

        # Add more tests as needed for other fit types and edge cases

class TestFit(unittest.TestCase):

    def test_do_fit(self):
        my_func = "a * sin(x) + b"
        x = [1, 2, 3]
        y = [4, 5, 6]
        p0 = [1, 1]
        yerr = [1, 1, 1]
        expected_result = [np.array([-1.93611801,  6.22097308]), np.array([1.33433151, 0.96059825]), 0.6440378595120685]

        a = lp.analysis(x, y, yerr, my_func)
        a.do_fit(predictions=p0)

        result = [a.popt, a.perr, a.rcs]

        for i in range(len(result)):
            np.testing.assert_allclose(result[i], expected_result[i], rtol=1e-5)

class TestPlotter(unittest.TestCase):

    def test_plot_creates_file(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 6])
        yerr = np.array([0.1, 0.2, 0.3])

        # Call the plot method
        #a = lp.analysis(x, y, yerr, "a*x + b")
        #a.do_fit()
        #a.make_plot()
        lp.analyse(x, y, yerr, "Linear")

        # Check if the file was created
        self.assertTrue(os.path.exists('myplot.png'))
        self.assertTrue(os.path.exists('myplot.pdf'))

        # Clean up the created files
        os.remove('myplot.png')
        os.remove('myplot.pdf')


if __name__ == '__main__':
    unittest.main()
