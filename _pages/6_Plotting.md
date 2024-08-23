# Plotting

We can use Python to produce plots of data and save them to a file. Here we will look at how we can create the most common types of plots.

`````{grid}
````{grid-item}
:columns: 4
```{figure} ../_images/6_Line_plot_6.png
Line plot
```
````

````{grid-item}
:columns: 4
```{figure} ../_images/6_Multiple_plots_2.png
Multiple line plot
````

````{grid-item}
:columns: 4
```{figure} ../_images/6_Scatter_plot_1.png
Scatter plot
````

````{grid-item}
:columns: 4
```{figure} ../_images/6_Surface_plot_4.png
Surface plot
````

````{grid-item}
:columns: 4
```{figure} ../_images/6_Contour_plot_3.png
Contour plot
````

````{grid-item}
:columns: 4
```{figure} ../_images/6_Image_plot_2.png
Image plot
````
`````

---

## matplotlib

<a href="https://matplotlib.org/" target="_blank">matplotlib</a> is a library of functions that allows us to produce plots of data within a Python program. Like with other libraries, we need to import it using the `import` command. For example, to import the `matplotlib` module `pyplot` which is used for the most common plots we use the following code

```python
import matplotlib.pyplot as plt
```

This will allow us to call `pyplot` functions using the precursor `plt.`.
