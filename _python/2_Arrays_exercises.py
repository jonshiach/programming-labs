import numpy as np

# Exercise 2.1
print("\nExercise 2.1\n------------")

a = np.array([6, 3, 4, -1])
print(f"1. a = {a} \n")

B = np.array([[3, 5, -2], [2, 4, 3], [7, 2, -1]])
print(f"2. B = \n\n {B} \n")

C = np.array([[2, 0, -1, 4], [7, -3, 9, -5]])
print(f"3. C = \n\n {C} \n")

D = np.array([[-4, 4, 2], [7, 5, -3], [5, 1, 6]])
print(f"4. D = \n\n {D} \n")

odd = np.arange(1, 32, 2)
print(f"5. Odd numbers upto and including 31:\n\n {odd} \n")

mult_6 = np.arange(0, 100, 6)
print(f"6. Multiples of 6 between 0 and 100:\n\n {np.arange(0, 100, 6)} \n")

mult_9 = np.arange(999, 899, -9)
print(f"7. Multiples of 9 between 900 and 1000 in reverse order: \n\n {mult_9} \n")

threes = 3 * np.ones((4, 8))
print(f"8. A 4x8 array of 3s: \n\n {threes} \n")

I_10 = np.eye(10)
print(f"9. A 10x10 identity matrix: \n\n {I_10} \n")

# Exercise 2.2
print("\nExercise 2.2\n------------")
print(f"1. a(3) = {a[2]}")
print(f"2. B(1,2) = {B[0,1]}")
print(f"3. Middle two elements of a = {a[1:3]}")
print(f"4. 3rd column of C = {C[:,2]}")
print(f"5. Last 2 rows and columns of D: \n\n {D[-2:,-2:]} \n")
print(f"6. B with rows in reverse order: \n\n {B[::-1,:]} \n")
print(f"7. 1st and 3rd columns of D: \n\n {D[:,0::2]}")

# Exercise 2.3
print("\nExercise 2.3\n------------")
print(f"1. 2a = {2 * a} \n")
print(f"2. B + D = \n\n {B + D} \n")
print(f"3. C^T = \n\n {C.T} \n")
print(f"4. B * D = \n\n {B * D} \n")
print(f"5. DB = \n\n {np.dot(D, B)} \n")
print(f"6. DBB^T = \n\n {np.linalg.multi_dot((D, B, B.T))} \n")
print(f"7. D.^3 = \n\n {D ** 3} \n")
print(f"8. B^4 = \n\n {np.linalg.matrix_power(B, 4)} \n")
print(f"9. det(B) = {np.linalg.det(B)} \n")
print(f"10. inv(D) = \n\n {np.linalg.inv(D)} \n")

# Exercise 2.4
print("\nExercise 2.4\n------------")

new_matrix = np.append(B, D, 1)
print(f"1. D appended to the right of B:\n\n {new_matrix} \n")

new_matrix = np.insert(B, 2, D.T, 1)
print(f"2. D inserted between the 2nd and 3rd columns of B: \n\n {new_matrix} \n")

new_matrix = np.delete(B, 1, 0)
print(f"3. B with the middle row deleted: \n\n {new_matrix} \n")

a= np.sort(a)
print(f"4. a sorted in descending order: {a} \n")

new_matrix = np.reshape(C, (8, 1))
print(f"5. C reshaped into an 8x1 array:\n\n {new_matrix} \n")







