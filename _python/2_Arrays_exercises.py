#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 2. Arrays Exercises
# =============================================================================

import numpy as np

# -----------------------------------------------------------------------------
# Exercise 2.1

print("\nExercise 2.1\n--------------")

a = np.array([6, 3, 4, -1])
print(f"\n1. a = {a}")

B = np.array([[3, 5, -2], [2, 4, 3], [7, 2, -1]])
print(f"\n2. B = \n{B}")

C = np.array([[2, 0, -1, 4], [7, -3, 9, -5]])
print(f"\n3. C = \n{C}")

D = np.array([[-4, 4, 2], [7, 5, -3], [5, 1, 6]])
print(f"\n4. D = \n{D}")

print(f"\n5. Odd numbers upto and including 31:\n\n{np.arange(1, 32, 2)}")
print(f"\n6. Multiples of 4 between 0 and 100:\n\n{np.arange(0, 100, 6)}")
print(f"\n7. Multiples of 9 between 900 and 1000 in reverse order:\n\n{np.arange(999, 899, -9)}")
print(f"\n8. A 4x8 array of 3s:\n\n{3 * np.ones((4,8))}")
print(f"\n9. A 10x10 identity matrix:\n\n{np.eye(10)}")

# -----------------------------------------------------------------------------
# Exercise 2.2
print("\nExercise 2.2\n---------")
print(f"\na = {a}\n\nB = \n{B}\n\nC = \n{C}\n\nD = \n{D}")
print(f"\n1. the third element of a: {a[2]}")
print(f"\n2. the element in row 1, columns 2 of B: {B[0,1]}")
print(f"\n3. the middle two elements of a: {a[2:4]}")
print(f"\n4. the third column of C: {C[:,2]}")
print(f"\n5. the matrix formed by the last two rows and columns of D:\n\n{D[1:,1:]}")
print(f"\n6. the matrix B with the rows in reverse order:\n\n{B[::-1,:]}")
print(f"\n7. the first and third columns of D:\n\n{D[:,0::2]}")

# -----------------------------------------------------------------------------
# Exercise 2.3
print("\nExercise 2.3\n------------")
print(f"\na = {a}\n\nB = \n{B}\n\nC = \n{C}\n\nD = \n{D}")
print(f"\n1. 2a = {2 * a}")
print(f"\n2. B + D = \n{B + D}")
print(f"\n3. C^T = \n{C.T}")
print(f"\n4. B * D = \n{B * D}")
print(f"\n5. DB = \n{np.dot(D, B)}")
print(f"\n6. DBB^T = \n{np.linalg.multi_dot((D, B, B.T))}")
print(f"\n7. D.^3 = \n{D ** 3}")
print(f"\n8. B^4 = \n{np.linalg.matrix_power(B, 4)}")
print(f"\n9. det(B) = {np.linalg.det(B)}")
print(f"\n10. inv(D) = \n{np.linalg.inv(D)}")

# -----------------------------------------------------------------------------
# Exercise 2.4
print("\nExercise 2.4\n------------")
print(f"\na = {a}\n\nB = \n{B}\n\nC = \n{C}\n\nD = \n{D}")
print(f"\n1. D appended to the right of B:\n\n{np.append(B, D, 1)}")
print(f"\n2. D inserted between the 2nd and 3rd columns of B:\n\n{np.insert(B, 2, D.T, 1)}")
print(f"\n3. B with the middle row deleted:\n\n{np.delete(B, 1, 0)}")
print(f"\n4. a sorted in descending order: {np.sort(a)[::-1]}")
print(f"\n5. C reshaped into an 8x1 array:\n\n{np.reshape(C, (8, 1))}")







