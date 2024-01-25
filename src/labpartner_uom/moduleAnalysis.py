import numpy as np
import sympy as sp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import re
import os
import pandas as pd
from typing import List, Union


class analysis:

    def __init__(self, x: Union[List[float], np.ndarray],
                 y: Union[List[float], np.ndarray],
                 yerr: Union[List[float], np.ndarray],
                 func_text: str):

        self.x = np.array(x)
        self.y = np.array(y)
        self.yerr = np.array(yerr)

        self.func_text = func_text
        self.func = None
        self.params = None

        self.popt = None
        self.perr = None
        self.rcs = None

        self.outfilename = "myplot"

    def func_wrapper(self, x_in, *params):
        return self.func(x_in, *params)

    def calculate_chi_squared(self):
        chi_squared = 0
        for i in range(len(self.x)):
            chi_squared += ((self.y[i] - self.func(self.x[i],
                            *self.popt)) / self.yerr[i]) ** 2
        return chi_squared

    def calculate_reduced_chi_squared(self):
        chi_squared = self.calculate_chi_squared()
        return chi_squared / (len(self.x) - len(self.popt))

    def do_fit(self, predictions=None, bounds=None):

        # Extract parameter names from func_text
        params = re.findall(r'\b[a-zA-Z]\b', self.func_text)

        # Remove 'x' from params if it's there
        params = [p for p in params if p != 'x']

        # Store Params
        self.params = params

        # Create symbols for x and the parameters
        sym = sp.symbols(' '.join(['x'] + params))

        # Create the function
        self.func = sp.lambdify(sym, self.func_text, 'numpy')

        if predictions is None:
            predictions = [1 for p in params]

        if bounds is None:
            b0 = [-np.inf for p in params]
            b1 = [np.inf for p in params]
            bounds = (b0, b1)

        # Perform the fit
        # if predictions and bounds are None, set to defaults
        self.popt, pcov = curve_fit(self.func_wrapper,
                                    self.x, self.y,
                                    sigma=self.yerr,
                                    p0=predictions,
                                    bounds=bounds,
                                    max_nfev=10000,
                                    absolute_sigma=True)

        # Get errors from pcov
        self.perr = np.sqrt(np.diag(pcov))

        # Calculate reduced chi-squared
        self.rcs = self.calculate_reduced_chi_squared()

    def save_figure(self, fig, outfilename):

        if os.path.exists(f"{outfilename}.png") \
                or os.path.exists(f"{outfilename}.pdf"):

            i = 1

            while os.path.exists(f"{outfilename}({i}).png") \
                    or os.path.exists(f"{outfilename}({i}).pdf"):

                i += 1

            fig.savefig(f"{outfilename}({i}).png", dpi=300)
            fig.savefig(f"{outfilename}({i}).pdf", dpi=300)

        else:

            fig.savefig(f"{outfilename}.png", dpi=300)
            fig.savefig(f"{outfilename}.pdf", dpi=300)

    def make_plot(self, xlabel="x axis", ylabel="y axis", title=None,
                  label="data", figsize=(6, 4), outfilename="myplot"):

        fig, ax = plt.subplots(1, 1, figsize=figsize)

        ax.errorbar(self.x, self.y, yerr=self.yerr,
                    fmt='.', capsize=2, label=label)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        ax.set_title(title) if title is not None else None

        ax.plot(self.x, self.func(self.x, *self.popt),
                label='Fit: ' + self.func_text)

        ax.legend(loc='best')

        fig.tight_layout()
        self.save_figure(fig, outfilename)

        self.outfilename = outfilename

    def give_output(self):

        print("----------------------------------------")
        print("Fit Results")
        print("Fit = " + self.func_text)
        print("Fit Parameters: ", self.params)
        print("Fit Parameter Values: ", self.popt)
        print("Fit Parameter Errors: ", self.perr)
        print("Reduced Chi-Squared: ", self.rcs)
        print("")
        print("Plot saved as " + self.outfilename +
              ".png and " + self.outfilename + ".pdf")
        print("----------------------------------------")

# ------------------------------------------------------------------------------
# Wrapper function for the analysis class!
# ------------------------------------------------------------------------------


def analyse(x, y, yerr, fit, *args, **kwargs):

    if fit == "Linear":
        fit_type = "A*x + B"
    elif fit == "Quadratic":
        fit_type = "A*x**2 + B*x + C"
    elif fit == "Cubic":
        fit_type = "A*x**3 + B*x**2 + C*x + D"
    elif fit == "Exponential":
        fit_type = "A*exp(B*x) + C"
    elif fit == "Logarithmic":
        fit_type = "A*ln(x) + B"
    elif fit == "Sine":
        fit_type = "A*sin(B*x + C) + D"
    elif fit == "Cosine":
        fit_type = "A*cos(B*x + C) + D"
    elif fit == "Gaussian":
        fit_type = "A*exp(-(x-B)**2/(2*C**2)) + D"
    else:
        fit_type = fit

    # Create an analysis object
    a = analysis(x, y, yerr, fit_type)

    # Perform the fit
    a.do_fit(*args, **kwargs)

    # Make the plot
    a.make_plot(*args, **kwargs)

    # Give the output
    a.give_output()


def analyse_from_file(filename, fit, *args, **kwargs):

    # Check if the file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    # Check if the file is readable
    if not os.access(filename, os.R_OK):
        raise PermissionError(f"The file {filename} is not readable.")

    # Load the data from the file
    try:
        data = pd.read_csv(filename, delimiter=",")
    except Exception as e:
        raise ValueError(
            f"Unable to load data from the file {filename}. Error: {str(e)}")

    # Check if the data has at least 3 columns
    if data.shape[1] < 3:
        raise ValueError(
            "The data file must have at least 3 columns. Make sure the columns are separated by commas.")

    # Check if the data can be converted to a float
    try:
        data = data.astype(float)
    except ValueError:
        raise ValueError("The data in the file must be numeric.")

    # Convert the DataFrame to a NumPy array
    data = data.values

    # Call the original plot function with all arguments passed to the wrapper
    analyse(data[:, 0], data[:, 1], data[:, 2], fit, *args, **kwargs)
