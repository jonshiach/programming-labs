# Arrays

In mathematics, <a href="https://jonshiach.github.io/LA-book/pages/3.0_Vectors.html" target="_blank">vectors</a> can be expressed as either a row or column of elements and <a href="https://jonshiach.github.io/LA-book/pages/1.0_Matrices.html" target="_blank">matrices</a> are a rectangular array of elements. An individual element in the vector $\mathbf{a}$ is identified by an <a href="https://jonshiach.github.io/LA-book/pages/1.0_Matrices.html#indexing-a-matrix" target="_blank">index</a> denoted using a subscript, e.g., $a_i$. The index is the position of the element in the vector starting at 1 for the first element. An individual element in a matrix is identified by two indices denoted in a subscript, e.g., $[A]_{ij}$, the first number corresponding to the row number and the second number corresponding to the column number.

$$\mathbf{a}  = \begin{pmatrix} a_1, & a_2, & \cdots & a_n \end{pmatrix}, \qquad
  \mathbf{b}  = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}, \qquad
  A           = \begin{pmatrix}
            a_{11} & a_{12} & \cdots & a_{1n} \\
            a_{21} & a_{22} & \cdots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{m1} & a_{m2} & \cdots & a_{mn}
          \end{pmatrix}.$$

In computer programming, a vector or matrix is represented using an **array**. Arrays can be one-dimensional (1D) where they contain a single row or column of elements, similar to a vector, or two-dimensional (2D) similar to a matrix. It is possible to have higher dimensional arrays but this is not recommended as it can over complicate a program.

MATLAB is actually short for MATrix LABoratory and was originally designed for working with matrices and arrays. Unlike Python, MATLAB does not need any additional libraries to deal with arrays.
