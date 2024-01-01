import matplotlib.pyplot as plt
from .moduleLSFR import *


class plotter:

    @staticmethod
    def plot(x, y, yerr, xlabel="x axis", ylabel="y axis", title=None, label="data", fit=None, figsize=(4, 3)):

        fig, ax = plt.subplots(1, 1, figsize=figsize)

        ax.errorbar(x, y, yerr=yerr, fmt='.', capsize=4, label=label)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        ax.set_title(title) if title is not None else None

        if fit == "lin":

            fit = linfit.do_linear_fit(x, y, yerr)
            ax.plot(x, fit[0]*x + fit[2], label='Linear Fit')

        elif fit == "quad":

            fit = linfit.do_quadratic_fit(x, y, yerr)
            ax.plot(x, fit[0]*x**2 + fit[2]*x + fit[4], label='Quadratic Fit')

        ax.legend(loc='best')

        fig.tight_layout()
        fig.savefig('myplot.png', dpi=300)
        fig.savefig('myplot.pdf')

    @staticmethod
    def print_help():

        startup_info = """
        Plotting Tool
        -------------
        This software uses the Matplotlib module to plot a set of data points.

        Usage
        -----
        To use this software, run the following command:
        import labpartner as lp
        lp.plotter.plot(x, y, yerr, xlabel="x axis", ylabel="y axis", title=None, label="data", fit=None, figsize=(4, 3))

        Example
        -------
        import labpartner as lp
        lp.plotter.plot([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])

        Returns
        -------
        A plot of the data points.
        """

        print(startup_info)
