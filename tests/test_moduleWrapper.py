import unittest
from unittest.mock import patch
from labpartner_uom.moduleWrapper import analyse

class TestAnalyse(unittest.TestCase):

    @patch('labpartner_uom.modulePlotter.plotter.plot')
    def test_analyse(self, mock_plot):
        # Test with fit="Linear"
        analyse([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], fit="Linear")
        mock_plot.assert_called_with([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], fit_type="A*x + B")

        # Test with fit="Quadratic"
        analyse([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], fit="Quadratic")
        mock_plot.assert_called_with([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], fit_type="A*x**2 + B*x + C")

        # Test with fit=None
        analyse([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3])
        mock_plot.assert_called_with([1, 2, 3], [1, 2, 3], [0.1, 0.2, 0.3], fit_type=None)

        # Add more tests as needed for other fit types and edge cases

if __name__ == '__main__':
    unittest.main()
