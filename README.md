# LabPartner - A Tool for Undergraduate Physics Students

[![PyPI package](https://img.shields.io/badge/pip%20install-example--pypi--package-brightgreen)](https://pypi.org/project/example-pypi-package/) [![version number](https://img.shields.io/pypi/v/example-pypi-package?color=green&label=version)](https://github.com/SiddharthSule/labpartner/releases) [![Actions Status](https://github.com/SiddharthSule/labpartner/workflows/Test/badge.svg)](https://github.com/SiddharthSule/labpartner/actions) [![License](https://img.shields.io/github/license/SiddharthSule/labpartner)](https://github.com/SiddharthSule/labpartner/blob/main/LICENSE)

Struggling with Lab? Me too!

Over the course of my undergraduate studies at the University of Manchester, UK, I had three years of lab. Now, as someone who teaches those labs alongside my PhD, I thought it would be useful to automate some of the more painful parts of lab, so the students can just focus on understanding the physics and assessing their results.

This Python is Package can:
- Propagate Errors for any Function
- Apply ~Linear and Quadratic~ ANY fit to a set of Data
- Plot Results in the style of Lab Reports

It is important to acknowledge that there are other very useful tools (OriginPro, LSFR, your own code). I just wanted to try making something that works as an all-in-one system, effectively acting as a Lab Partner!

## Installation

This should be working in a few weeks time. To install this package, simply type:

```bash
pip install labpartner
```

## Usage

The code is based on Numpy, Sympy and Matplotlib. Try to have your x, y and y error data as Numpy arrays.

### Error Propagation

```python
import labpartner as lp
prop = lp.errorpropagator.propagate_error(func, vars)

# Example
prop = lp.errorpropagator.propagate_error("A*x**2 + B*y + C", ["x", "y"])
```

### Function Fitting

```python
import labpartner as lp
fit = lp.fit.do_fit(lp.fit.do_fit(x, y, func, p0=p0, yerr=yerr)

# Example
my_func = "a * sin(x) + b"
fit = lp.fit.do_fit([1, 2, 3], [4, 5, 6], my_func, p0=[1, 1], yerr=[1, 1, 1])
```

### (OLD) Linear and Quadratic Fit

```python
import labpartner as lp
fit = lp.linfit.do_linear_fit(x, y, yerr)
fit = lp.quadfit.do_quadratic_fit(x, y, yerr)


# Example
fit = lp.linfit.do_linear_fit([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])
fit = lp.quadfit.do_quadratic_fit([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])
```

### Plotting

```python
import labpartner as lp
lp.plotter.plot(x, y, yerr=None, xlabel="x axis", ylabel="y axis", title=None, label="data", fit_type=None, figsize=(4, 3))

# Example
lp.plotter.plot([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])
```

---
Siddharth Sule, 2024

Based On Tom Chen's Example Package: https://github.com/tomchen/example_pypi_package
