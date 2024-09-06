# =============================================================================
# 2. Arrays
# =============================================================================

import numpy as np

# Declaring arrays
a = np.array([1, 2, 3])
print(f"a = {a} \n")

# 2D arrays
A = np.array([ [1, 2,] , [3, 4] ])
print(f"A = \n{A} \n")

# Range of numbers
b = np.arange(1, 10, 1)
print(f"b = {b} \n")

c = np.arange(0, 21, 2)
print(f"c = {c} \n")

d = np.arange(10, 0, -1)
print(f"d = {d} \n")

# Special matrices
zeros_1x6 = np.zeros(6)
print(f"1x6 array of zeros = {zeros_1x6} \n")

ones_4x4 = np.ones((4,4))
print(f"4x4 array of ones = \n\n {ones_4x4} \n")

I_5 = np.eye(5)
print(f"5x5 identity matrix = \n\n {I_5} \n")

# Array indexing
print(f"The first element in a is {a[0]}")
print(f"The second element in a is {a[1]}")
print(f"The last element in a is {a[-1]}")
print(f"The element in row 1 column 1 of A is {A[0,0]}")
print(f"The element in row 2 column 1 of A is {A[1,0]}")

# Array sizes
print(f"\nThe 1D array a has {len(a)} elements")
print(f"The 2D array A has {A.shape[0]} rows and {A.shape[1]} columns \n")

# Array slicing
print(f"The first 4 elements of b are {b[:4]}")
print(f"The last 5 elements of b are {b[4:]}")
print(f"The middle three elements of b are {b[3:6]}")
print(f"The elements of b with even indices are {b[::2]}")
print(f"The elements of b in reverse order are {b[::-1]}")
print(f"The first row of A is {A[0,:]}")
print(f"The second column of A is {A[:,1]}\n")

# Array operations
B = np.array([ [5, 6], [7, 8] ])

print(f"A = \n\n {A} \n")
print(f"B = \n\n {B} \n")

A_add_B = A + B
print(f"A + B =\n\n {A_add_B} \n")

A_sub_B = A - B
print(f"A - B =\n\n {A_sub_B} \n")

A2 = 2 * A
print(f"2A = \n\n {A2} \n")

AT = A.T
print(f"A^T = \n\n {AT} \n")

AB_elementwise = A * B
print(f"A * B = \n\n {AB_elementwise} \n")

AB = np.dot(A, B)
print(f"AB = \n\n {np.dot(A, B)} \n")

ABA = np.linalg.multi_dot([A, B, A])
print(f"ABA = \n\n {ABA} \n")

A_pow_2_elementwise = A ** 2
print(f"A^2 (elementise) = \n\n {A_pow_2_elementwise} \n")

A_pow_2= np.linalg.matrix_power(A, 2)
print(f"A^2 = \n\n {A_pow_2} \n")

detA = np.linalg.det(A)
print(f"det(A) = {detA} \n")

invA = np.linalg.inv(A)
print(f"inv(A) = \n\n {invA} \n")

# Manipulating arrays
print(f"a = {a}")

a = np.append(a, np.array([4, 5]))
print(f"Append [4, 5] to array a: a = {a} \n")

new_matrix = np.append(A, B, 0)
print(f"Append B to the bottom of A: \n\n {new_matrix} \n") 

new_matrix = np.append(A, B, 1)
print(f"Append B to the right of A: \n\n {new_matrix} \n")

a = np.insert(a, 2, np.array([6, 7, 8]))
print(f"Insert [6, 7, 8] into array a: a = {a} \n")

new_matrix = np.insert(A, 1, B, 0)
print(f"Insert B between the rows of A: \n\n {new_matrix} \n")

new_matrix = np.insert(A, 1, B.T, 1)
print(f"Insert B between the columns of A: \n\n {new_matrix} \n")

a = np.delete(a, [3, 4])
print(f"Delete the 4th and 5th elements of a: a = {a} \n")

C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"C = \n\n {C} \n")

new_matrix = np.delete(C, 2, 0)
print(f"Delete the 2nd row of C: \n\n {new_matrix} \n")

new_matrix = np.delete(C, -1, 1)
print(f"Delete the last column of C: \n\n {new_matrix} \n")

a = np.sort(a)
print(f"Sort array a into ascending order: a = {a} \n")

a_3x2 = np.reshape(a, (3, 2))
print(f"Reshape array a into a 3 x 2 array: \n\n {a_3x2} \n")

a_3x2 = np.reshape(a, (3, 2), 'F')
print(f"Reshape array a into a 3 x 2 array (down and across): \n\n {a_3x2} \n")