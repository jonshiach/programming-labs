# 2. Arrays

## Vectors and matrices

In mathematics, <a href="https://jonshiach.github.io/LA-book/pages/3.0_Vectors.html" target="_blank">vectors</a> can be expressed as either a row or column of elements and <a href="https://jonshiach.github.io/LA-book/pages/1.0_Matrices.html" target="_blank">matrices</a> are a rectangular array of elements. An individual element in the vector $\mathbf{a}$ is identified by an <a href="https://jonshiach.github.io/LA-book/pages/1.0_Matrices.html#indexing-a-matrix" target="_blank">index</a> denoted using a subscript, e.g., $a_i$. The index is the position of the element in the vector starting at 1 for the first element. An individual element in a matrix is identified by two indices denoted in a subscript, e.g., $[A]_{ij}$, the first number corresponding to the row number and the second number corresponding to the column number.

$$\mathbf{a}  = \begin{pmatrix} a_1, & a_2, & \cdots & a_n \end{pmatrix}, \qquad
  \mathbf{b}  = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}, \qquad
  A           = \begin{pmatrix}
            a_{11} & a_{12} & \cdots & a_{1n} \\
            a_{21} & a_{22} & \cdots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{m1} & a_{m2} & \cdots & a_{mn}
          \end{pmatrix}.$$

In computer programming, a vector or matrix is represented using an **array**. Arrays can be one-dimensional where they contain a single row or column of elements, similar to a vector, or two-dimensional array similar to a matrix. It is possible to have higher dimensional arrays but this is not recommended as it can over complicate a program.

---

## Libraries

Python is a simple all purpose programming language designed to service the needs of a wide variety of users. As such it only has a small number of built in functions (the full list of intrinsic functions in Python can be found <a href="https://docs.python.org/3/library/functions.html" target="_blank">here</a>). Fortunately there is a wide variety of **libraries** which are a collection of functions that we can **import** into our programs so that we can make use of the functions that have been written to perform certain tasks.

To import a library we use the following

```python
import <library>
```

This will import a library which will allow us to use a function from the library. To do this we prefix the name fo the library to the name of the function we want to use, i.e.,

```python
<library>.<function>()
```

For convenience we can assign a shorthand name of the library using

```python
import <library> as <short name>
```

which then allows us to call a function using the shortened name.

```python
<short name>.function()
```

### The NumPy library

A very useful Python library for mathematicians is the <a href="https://numpy.org/doc/stable/index.html" target="_blank">NumPy</a> library (pronounced *Num-pie*). NumPy has a range of functions useful for scientific computing and working with arrays. The NumPy library can be imported using

```python
import numpy as np
```
