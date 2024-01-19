from .modulePlotter import *
import numpy as np

def analyse(x, y, yerr, fit=None, *args, **kwargs):

    if fit=="Linear":
        fit_type = "A*x + B"
    elif fit=="Quadratic":
        fit_type = "A*x**2 + B*x + C"
    elif fit=="Cubic":
        fit_type = "A*x**3 + B*x**2 + C*x + D"
    elif fit=="Exponential":
        fit_type = "A*exp(B*x) + C"
    elif fit=="Logarithmic":
        fit_type = "A*ln(x) + B"
    elif fit=="Sine":
        fit_type = "A*sin(B*x + C) + D"
    elif fit=="Cosine":
        fit_type = "A*cos(B*x + C) + D"
    elif fit=="Gaussian":
        fit_type = "A*exp(-(x-B)**2/(2*C**2)) + D"
    else:
        fit_type = fit

    # Call the original plot function with all arguments passed to the wrapper
    plotter.plot(x, y, yerr, fit_type=fit_type, *args, **kwargs)

def analyse_from_file(filename, fit, *args, **kwargs):

    # Load the data from the file
    data = np.loadtxt(filename, delimiter=",")

    if data.shape[1] < 3:
        raise ValueError("The data file must have at least 3 columns. Make sure the columns are separated by commas.")

    # Call the original plot function with all arguments passed to the wrapper
    plotter.plot(data[:,0], data[:,1], data[:,2], fit_type=fit, *args, **kwargs)
