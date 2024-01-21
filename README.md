# LabPartner - A Tool for Undergraduate Physics Students

[![PyPI package](https://img.shields.io/badge/pip%20install-labpartner_uom-brightgreen)](https://pypi.org/project/labpartner_uom/) [![version number](https://img.shields.io/pypi/v/labpartner_uom?color=green&label=version)](https://github.com/SiddharthSule/labpartner_uom/releases) [![Actions Status](https://github.com/SiddharthSule/labpartner_uom/workflows/Test/badge.svg)](https://github.com/SiddharthSule/labpartner_uom/actions) [![License](https://img.shields.io/github/license/SiddharthSule/labpartner_uom)](https://github.com/SiddharthSule/labpartner_uom/blob/main/LICENSE)

Struggling with Lab? Me too!

Over the course of my undergraduate studies at the University of Manchester, UK, I had three years of lab. Now, as someone who teaches those labs alongside my PhD, I thought it would be useful to automate some of the more painful parts of lab, so the students can just focus on understanding the physics and assessing their results.

This Python is Package can:
- Apply ~Linear and Quadratic~ ANY fit to Data, and Plot Results
- Propagate Errors for any Function

It is important to acknowledge that there are other similar, very useful tools (OriginPro, LSFR, your own code). I just wanted to try making something that works as an all-in-one system, effectively acting as a Lab Partner!

## Installation

To install this package, simply type:

```bash
pip install labpartner_uom
```
PyPI might use labpartner-uom, but this command does the same. Someday I hope to remove the '_uom'!

## Usage

### Data Analysis and Plotting

There are a few presets which allow you to auto-analyse your results.

```python
import labpartner_uom as lp
lp.analyse(x, y, yerr, fit="Linear")
```

This should print the results of the fitting, as well save a .png and .pdf of the plot.

Options of fits include: Linear, Quadratic, Gaussian, Exponential, Logarithmic, Sine, Cosine and more! You can also add your own functions to fit (see below for details)

### Error Propagation

To propagate errors, simply write up the function and the variables which have uncertainties.

```python
import labpartner_uom as lp
prop = lp.errorpropagator.propagate_error(func, vars)

# Example
prop = lp.errorpropagator.propagate_error("A*x**2 + B*y + C", ["x", "y"])
```

### Examples

I have given some full examples on how to use the code for a lab experiment. The first example contains a simple analysis, while the other is for free and forced oscillations, a lab I demonstrated.

You can find these examples [here](docs/examples/)

### Advanced Usage

The guide above gives you a quick result. However, there is more for advanced users:
- Customisation of Plots
- Fitting without Errors

You can find more details on this in [more-stuff.md](docs/extended/more-stuff.md)


---
Siddharth Sule, 2024

Based On Tom Chen's Example Package: https://github.com/tomchen/example_pypi_package
