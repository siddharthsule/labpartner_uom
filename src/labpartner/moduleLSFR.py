import numpy as np


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
