#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 2. Arrays
# =============================================================================

import numpy as np

print("\n2. Arrays\n---------")

# 2.2 Declaring arrays
print("\n2.2 Declaring arrays\n--------------------")

a = np.array([1, 2, 3])
print(f"a = {a}")

A = np.array([ [1, 2,] , [3, 4] ])
print(f"\nA = \n{A}")

b = np.arange(1, 10, 1)
print(f"\nb = {b}")

c = np.arange(0, 21, 2)
print(f"\nc = {c}")

d = np.arange(10, 0, -1)
print(f"\nd = {d}")

# 2.2.2 Special matrices
print("\n2.2.2 Special matrices\n----------------------")
print(f"1x6 array of zeros\n\n{np.zeros(6)}")
print(f"\n4x4 array of ones\n\n{np.ones((4, 4))}")
print(f"\nThe 5x5 identity matrix\n\n{np.eye(5)}")

# 2.3 Array indexing
print("\n2.3 Array indexing\n------------------")
print(f"The first element in a is {a[0]}")
print(f"The second element in a is {a[1]}")
print(f"The last element in a is {a[-1]}")
print(f"The element in row 1 column 1 of A is {A[0,0]}")
print(f"The element in row 2 column 1 of A is {A[1,0]}")

# 2.3.1 Array sizes
print("\n2.3.1 Array sizes\n-----------------")
print(f"The 1D array a has {len(a)} elements")
print(f"The 2D array A has {A.shape[0]} rows and {A.shape[1]} columns")

# 2.3.2 Array slicing
print("\n2.3.2 Array slicing\n-------------------")
print(f"The first 4 elements of b are {b[:4]}")
print(f"The last 5 elements of b are {b[4:]}")
print(f"The middle three elements of b are {b[3:6]}")
print(f"The elements of b with even indices are {b[::2]}")
print(f"The elements of b in reverse order are {b[::-1]}")
print(f"The first row of A is {A[0,:]}")
print(f"The second column of A is {A[:,1]}")

# 2.4 Array operations
B = np.array([ [5, 6], [7, 8] ])

print("\n2.4 Array operations\n--------------------")
print(f"A = \n{A}")
print(f"\nB = \n{B}")
print(f"\nA + B =\n{A + B}")
print(f"\nA - B =\n{A - B}")
print(f"\n2A = \n{2 * A}")
print(f"\nA^T = \n{A.T}")
print(f"\nA * B = \n{A * B}")
print(f"\nAB = \n{np.dot(A, B)}")
print(f"\nABA = \n{np.linalg.multi_dot([A, B, A])}")
print(f"\nA^.2 = \n{A ** 2}")
print(f"\nA^2 = \n{np.linalg.matrix_power(A, 2)}")
print(f"\ndet(A) = \n{np.linalg.det(A)}")
print(f"\ninv(A) = \n{np.linalg.inv(A)}")
print(f"\ninv(A) * A = \n{np.dot(A, np.linalg.inv(A))}")

# 2.5 Manipulating arrays
print("\n2.5 Manipulating arrays\n-----------------------")
print(f"a = {a}")

a = np.append(a, np.array([4, 5]))
print(f"\nAppend [4, 5] to array a:\na = {a}")

C = np.append(A, B, 0)
print(f"\nAppend B to the bottom of A:\nC = \n{C}") 

D = np.append(A, B, 1)
print(f"\nAppend B to the right of A:\nD = \n{D}")

a = np.insert(a, 2, np.array([6, 7, 8]))
print(f"\nInsert [6, 7, 8] into array a:\na = {a}")

E = np.insert(A, 1, B, 0)
print(f"\nInsert B between the rows of A:\nE = \n{E}")

F = np.insert(A, 1, B.T, 1)
print(f"\nInsert B between the columns of A:\nF = \n{F}")

a = np.delete(a, [3, 4])
print(f"\nDeleting the 4th and 5th elements of a:\na = {a}")

G = np.delete(C, 2, 0)
print(f"\nDelete the 3rd row of C:\nG = \n{G}")

H = np.delete(D, 1, 1)
print(f"\nDelete the 2nd column of H:\nH = \n{H}")

a = np.sort(a)
print(f"\nSort array a into ascending order:\na = {a}")

I = np.reshape(a, (3, 2))
print(f"\nReshape array a into a 3 x 2 array:\nI = \n{I}")

J = np.reshape(a, (3, 2), 'F')
print(f"\nReshape array a into a 3 x 2 array column-by-column:\nJ = \n{J}")