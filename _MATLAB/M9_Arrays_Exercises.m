% 8. Arrays Exercises

clear % Clear all variables
clc   % Clear command window

% Exercise 9.1
fprintf("\nExercise 9.1\n------------\n")
fprintf("1.")
a = [6, 3, 4, -1]

fprintf("2.")
B = [3, 5, -2 ; 2, 4, 3 ; 7, 2, -1]

fprintf("3.")
C = [2, 0, -1, 4 ; 7, -3, 9, -5]

fprintf("4.")
D = [-4, 4, 2 ; 7, 5, -3 ; 5, 1, 6]

fprintf("5. An array of odd numbers up to and including 31")
(1:2:31)

fprintf("6. An array containing the multiples of 6 betwee 0 and 100 inclusive")
(0:6:100)

fprintf("7. An array containing the multiples of 9 between 900 and 1000 in reverse order")
(999:-9:900)

fprintf("8. A 4x8 array of 3s")
3 * ones(4, 8)

fprintf("9. A 10x10 identity matrix")
eye(10)

% Exercise 9.2
fprintf("\nExercise 9.2\n------------\n")

fprintf("1. the third element of a is %d \n", a(3))

fprintf("2. the element in row 1, column 2 of B is %d \n", B(1,2))

fprintf("3. the middle two elements of a")
a(2:3)

fprintf("4. the third column of C")
C(:,3)

fprintf("5. the matrix formed by the last two rows and columns of D")
D(end-1:end,end-1:end)

fprintf("6. the matrix B with the rows in reverse order")
B(end:-1:1,:)

fprintf("7. the first and third columns of D")
D(:,1:2:3)

% Exercise 9.3
fprintf("\nExercise 9.3\n------------\n")
fprintf("1. 2a =")
2 * a

fprintf("2. B + D =")
B + D

fprintf("3. C^T =")
C'

fprintf("4. B .* D")
B .* D

fprintf("5. DB =")
D * B

fprintf("6. DBB^T =")
D * B * B'

fprintf("7. D .^ 3 =")
D .^ 3

fprintf("8. B ^ 4 =")
B ^ 4

fprintf("9. det(B) = %0.2f \n\n", det(B))

fprintf("10. inv(B) =")
inv(B)

% Exercise 9.4
fprintf("Exercise 9.4\n------------\n")
fprintf("1. D appended to the right of B")
[B, D]

fprintf("2. The first two rows of D appended to the bottom of B")
[B ; D(1:2,:)]

fprintf("3. D inserted between the 2nd and 3rd columns of B")
[B(:,1:2), D, B(:,3:end)]

fprintf("4. B with the middle row removed")
B(2,:) = []

fprintf("5. a sorted in descending order")
a = sort(a, 'descend')

fprintf("6. C reshaped into an 8x1 array")
C = reshape(C, 8, 1)
