import unittest
import numpy as np
import os
from labpartner_uom.modulePlotter import plotter
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal

class TestPlotter(unittest.TestCase):

    def test_plot_creates_file(self):
        x = np.array([1, 2, 3])
        y = np.array([2, 4, 6])
        yerr = np.array([0.1, 0.2, 0.3])

        # Call the plot method
        plotter.plot(x, y, yerr, fit_type="lin")

        # Check if the file was created
        self.assertTrue(os.path.exists('myplot.png'))
        self.assertTrue(os.path.exists('myplot.pdf'))

        # Clean up the created files
        os.remove('myplot.png')
        os.remove('myplot.pdf')

if __name__ == '__main__':
    unittest.main()
