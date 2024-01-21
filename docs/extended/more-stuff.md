# Advanced Options - For those who want more Customisation

## Function Fitting

```python
import labpartner_uom as lp
fit = lp.fit.do_fit(lp.fit.do_fit(x, y, func, p0=p0, yerr=yerr)

# Example
my_func = "a * sin(x) + b"
fit = lp.fit.do_fit([1, 2, 3], [4, 5, 6], my_func, p0=[1, 1], yerr=[1, 1, 1])
```

## (OLD) Linear and Quadratic Fit

```python
import labpartner_uom as lp
fit = lp.linfit.do_linear_fit(x, y, yerr)
fit = lp.quadfit.do_quadratic_fit(x, y, yerr)


# Example
fit = lp.linfit.do_linear_fit([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])
fit = lp.quadfit.do_quadratic_fit([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])
```

## Plotting

```python
import labpartner_uom as lp
lp.plotter.plot(x, y, yerr=None, xlabel="x axis", ylabel="y axis", title=None, label="data", fit_type=None, figsize=(4, 3))

# Example
lp.plotter.plot([1, 2, 3], [4, 5, 6], [0.2, 0.2, 0.3])
```
