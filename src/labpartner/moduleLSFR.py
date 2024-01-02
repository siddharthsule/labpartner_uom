import re
import numpy as np
import sympy as sp
from scipy.optimize import curve_fit

class linfit:

    @staticmethod
    def calculate_chi_squared(x, y, yerr, m, c):
        chi_squared = 0
        for i in range(len(x)):
            chi_squared += ((y[i] - (m * x[i] + c)) / yerr[i]) ** 2
        return chi_squared

    @staticmethod
    def calculate_reduced_chi_squared(x, y, yerr, m, c):
        chi_squared = linfit.calculate_chi_squared(x, y, yerr, m, c)
        return chi_squared / (len(x) - 2)

    @staticmethod
    def do_linear_fit(x, y, yerr=None, no_yerr=False):

        if no_yerr:
            yerr = np.ones(len(y))

        popt, pcov = np.polyfit(x, y, 1, w=1/yerr, cov=True)

        m = popt[0]
        c = popt[1]

        m_err = np.sqrt(pcov[0][0])
        c_err = np.sqrt(pcov[1][1])

        rcs = linfit.calculate_reduced_chi_squared(x, y, yerr, m, c)

        output = [m, m_err, c, c_err, rcs]
        return output

    @classmethod
    def print_help(cls):

        startup_info = """
        Linear Fit Tool
        ---------------
        This software uses the NumPy module to perform a linear
        fit on a set of data points.

        Usage
        -----
        To use this software, run the following command:
        import labpartner as lp
        fit = lp.linfit.do_linear_fit(x, y, yerr=None, no_yerr=False)

        Example
        -------
        import labpartner as lp
        fit = lp.linfit.do_linear_fit([1, 2, 3], [4, 5, 6])

        Returns
        -------
        fit: List containing the following elements:
        m: Gradient of the line of best fit
        m_err: Error on the gradient
        c: y-intercept of the line of best fit
        c_err: Error on the y-intercept
        rcs: Reduced chi-squared value
        """

        print(startup_info)


class quadfit:

    @staticmethod
    def calculate_chi_squared(x, y, yerr, a, b, c):
        chi_squared = 0
        for i in range(len(x)):
            chi_squared += ((y[i] - (a * x[i] ** 2 +
                            b * x[i] + c)) / yerr[i]) ** 2
        return chi_squared

    @staticmethod
    def calculate_reduced_chi_squared(x, y, yerr, a, b, c):
        chi_squared = quadfit.calculate_chi_squared(x, y, yerr, a, b, c)
        return chi_squared / (len(x) - 3)

    @staticmethod
    def do_quadratic_fit(x, y, yerr=None, no_yerr=False):

        if no_yerr:
            yerr = np.ones(len(y))

        popt, pcov = np.polyfit(x, y, 2, w=1/yerr, cov=True)

        a = popt[0]
        b = popt[1]
        c = popt[2]

        a_err = np.sqrt(pcov[0][0])
        b_err = np.sqrt(pcov[1][1])
        c_err = np.sqrt(pcov[2][2])

        rcs = quadfit.calculate_reduced_chi_squared(x, y, yerr, a, b, c)

        output = [a, a_err, b, b_err, c, c_err, rcs]
        return output

    @staticmethod
    def print_help():

        startup_info = """
        Quadratic Fit Tool
        ------------------
        This software uses the NumPy module to perform a quadratic
        fit on a set of data points.

        Usage
        -----
        To use this software, run the following command:
        import labpartner as lp
        fit = lp.quadfit.do_quadratic_fit(x, y, yerr=None, no_yerr=False)

        Example
        -------
        import labpartner as lp
        fit = lp.quadfit.do_quadratic_fit([1, 2, 3], [4, 5, 6])

        Returns
        -------
        fit: List containing the following elements:
        a: Coefficient of x^2
        a_err: Error on the coefficient of x^2
        b: Coefficient of x
        b_err: Error on the coefficient of x
        c: Constant term
        c_err: Error on the constant term
        rcs: Reduced chi-squared value
        """

class fit:

    @staticmethod
    def calculate_chi_squared(x, y, yerr, func, popt):
        chi_squared = 0
        for i in range(len(x)):
            chi_squared += ((y[i] - func(x[i], *popt)) / yerr[i]) ** 2
        return chi_squared

    @staticmethod
    def calculate_reduced_chi_squared(x, y, yerr, func, popt):
        chi_squared = fit.calculate_chi_squared(x, y, yerr, func, popt)
        return chi_squared / (len(x) - len(popt))

    @staticmethod
    def do_fit(x, y, func_text, p0=None, yerr=None, no_yerr=False):

        if no_yerr:
            yerr = np.ones(len(y))

        # Extract parameter names from func_text
        params = re.findall(r'\b[a-z]\b', func_text)

        # Remove 'x' from params if it's there
        params = [p for p in params if p != 'x']

        # Create symbols for x and the parameters
        sym = sp.symbols(' '.join(['x'] + params))

        # Create the function
        func = sp.lambdify(sym, func_text, 'numpy')

        # Create a wrapper function for curve_fit
        def func_wrapper(x, *params):
            return func(x, *params)

        if p0 == None:
            p0 = np.ones(len(params))

        # Perform the fit
        popt, pcov = curve_fit(func_wrapper, x, y, p0=p0, sigma=yerr)

        # Get errors from pcov
        perr = np.sqrt(np.diag(pcov))

        # Calculate reduced chi-squared
        rcs = fit.calculate_reduced_chi_squared(x, y, yerr, func, popt)

        output = [popt, perr, rcs]
        return output

    @staticmethod
    def print_help():

        startup_info = """
        Fit Tool
        --------
        This software uses the SciPy module to perform a fit
        on a set of data points.

        Usage
        -----
        To use this software, run the following command:
        import labpartner as lp
        fit = lp.fit.do_fit(x, y, func, p0, yerr=yerr)

        Example
        -------
        import labpartner as lp
        fit = lp.fit.do_fit([1, 2, 3], [4, 5, 6], lambda x, a, b: a * x + b, [1, 1])

        Returns
        -------
        fit: List containing the following elements:
        popt: List of best-fit parameters
        pcov: Covariance matrix
        rcs: Reduced chi-squared value
        """
