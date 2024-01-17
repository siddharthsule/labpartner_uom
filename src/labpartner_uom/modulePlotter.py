import matplotlib.pyplot as plt
from .moduleLSFR import *


class plotter:

    @staticmethod
    def plot(x, y, yerr, xlabel="x axis", ylabel="y axis", title=None, label="data", fit_type=None, p0=None, figsize=(4, 3)):

        rcs = 0
        fig, ax = plt.subplots(1, 1, figsize=figsize)

        ax.errorbar(x, y, yerr=yerr, fmt='.', capsize=4, label=label)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        ax.set_title(title) if title is not None else None

        if fit_type == "lin":

            fit = linfit.do_linear_fit(x, y, yerr)
            ax.plot(x, fit[0]*x + fit[2], label='Linear Fit')

        elif fit_type == "quad":

            fit = linfit.do_quadratic_fit(x, y, yerr)
            ax.plot(x, fit[0]*x**2 + fit[2]*x + fit[4], label='Quadratic Fit')

        elif fit_type == None:

            pass

        else:

            fit_res = fit.do_fit(x, y, fit_type, p0, yerr=yerr)

            # ----------------------------------------------------------
            # Duplicate code, should really remove

            # Extract parameter names from func_text
            params = re.findall(r'\b[a-z]\b', fit_type)

            # Remove 'x' from params if it's there
            params = [p for p in params if p != 'x']

            # Create symbols for x and the parameters
            sym = sp.symbols(' '.join(['x'] + params))

            # Create the function
            func = sp.lambdify(sym, fit_type, 'numpy')

            # Create a wrapper function for curve_fit
            def func_wrapper(x, *params):
                return func(x, *params)

            # ----------------------------------------------------------

            ax.plot(x, func_wrapper(x, *fit_res[0]), label='Fit:' + fit_type)

            print("----------------------------------------")
            print("Fit Results")
            print("Fit = " + fit_type)
            print("Fit Parameters = " + params)
            print("Fit Parameter Values = " + fit_res[0])
            print("Fit Parameter Errors = " + fit_res[1])
            print("Reduced Chi-Squared = " + fit_res[2])
            print("----------------------------------------")




        ax.legend(loc='best')

        fig.tight_layout()
        fig.savefig('myplot.png', dpi=300)
        fig.savefig('myplot.pdf')
        print("Plot saved as myplot.png and myplot.pdf!")
        print("----------------------------------------")

    @staticmethod
    def print_help():

        startup_info = """
        Plotting Tool
        -------------
        This software uses the Matplotlib module to plot a set of data points.

        Usage
        -----
        To use this software, run the following command:
        import labpartner_uom as lp
        lp.plotter.plot(x, y, yerr, xlabel="x axis", ylabel="y axis", title=None, label="data", fit=None, figsize=(4, 3))

        Example
        -------
        import labpartner_uom as lp
        lp.plotter.plot([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])

        Returns
        -------
        A plot of the data points.
        """

        print(startup_info)
