import unittest

from labpartner_uom.moduleErrorProp import errorpropagator


class TestErrorProp(unittest.TestCase):

    def test_error_prop(self):

        self.assertEqual(
            errorpropagator.propagate_error("x + y", ["x", "y"]),
            "Δf = sqrt((1 Δx)**2 + (1 Δy)**2)"
        )

        self.assertEqual(
            errorpropagator.propagate_error("x**2", ["x"]),
            "Δf = 2*x Δx"
        )

        self.assertEqual(
            errorpropagator.propagate_error("x**2 + y**2", ["x", "y"]),
            "Δf = sqrt((2*x Δx)**2 + (2*y Δy)**2)"
        )

        self.assertEqual(
            errorpropagator.propagate_error("m*x + c", ["x"]),
            "Δf = m Δx"
        )

        self.assertEqual(
            errorpropagator.propagate_error("log(x)", ["x"]),
            "Δf = 1/x Δx"
        )

        self.assertEqual(
            errorpropagator.propagate_error("exp(x)", ["x"]),
            "Δf = exp(x) Δx"
        )

        self.assertEqual(
            errorpropagator.propagate_error("sin(x)", ["x"]),
            "Δf = cos(x) Δx"
        )

        self.assertEqual(
            errorpropagator.propagate_error("cos(x)", ["x"]),
            "Δf = -sin(x) Δx"
        )

        self.assertEqual(
            errorpropagator.propagate_error("tan(x)", ["x"]),
            "Δf = tan(x)**2 + 1 Δx"
        )


if __name__ == '__main__':
    unittest.main()
