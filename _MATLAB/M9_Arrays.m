% 9. Arrays

clear % Clear all variables
clc   % Clear command window

% Declaring arrays
a = [1, 2, 3]

% 2D arrays
A = [1, 2 ; 3, 4]

% Range of numbers
b = (1 : 9)

c = (0 : 2 : 20)

d = (10 : -1 : 1)

% Special matrices
fprintf("1x6 array of zeros")
zeros(1, 6)

fprintf("4x4 array of ones")
ones(4, 4)

fprintf("5x5 identity matrix")
eye(5)

% Array indexing
fprintf("The first element in a is %d \n", a(1))
fprintf("The second element in a is %d \n", a(2))
fprintf("The last element in a is %d \n", a(end))
fprintf("The element in row 1 column 1 of A is %d \n", A(1,1))
fprintf("The element in row 2 column 1 of A is %d \n", A(2, 1))

% Array sizes
fprintf("The 1D array a has %d elements\n", length(a))
fprintf("The 2D array A has %d rows and %d columns\n", size(A, 1), size(A, 2))

% 9.2.2 Array slicing
fprintf("\nThe first 4 elements of b are")
b(1:4)
fprintf("The last 5 elements of b are")
b(5:end)
fprintf("The middle three elements of b are")
b(4:6)
fprintf("The elements of b with even indices are")
b(2:2:end)
fprintf("The elements of b in reverse order are")
b(end:-1:1)
fprintf("The first row of A is")
A(1,:)
fprintf("The second column of A is")
A(:,2)

% Array operations
A
B = [5, 6 ; 7, 8]

fprintf("A + B")
A + B

fprintf("A - B")
A - B

fprintf("2A")
2 * A

fprintf("A^T")
A'

fprintf("A .* B")
A .* B

fprintf("A * B")
A * B

fprintf("ABA")
A * B * A

fprintf("A .^ 2 =")
A .^ 2

fprintf("A ^ 2 =")
A ^ 2

fprintf("det(A) = %0.2f \n", det(A))

fprintf("\ninv(A) =")
inv(A)

fprintf("\nA * inv(A)")
A * inv(A)

% Manipulating arrays
a

fprintf("\nAppend [4, 5] to array a:")
a = [a, [4, 5]]

fprintf("\nAppend B to the bottom of A:")
[A ; B]

fprintf("\nAppend B to the right of A:")
[A , B]

fprintf("\nInsert [6, 7, 8] into the array a:")
a = [a(1 : 2), [6, 7, 8], a(3:end)]

fprintf("\nInsert B between the rows of A:")
[A(1,:) ; B ; A(2,:) ]

fprintf("\nInsert B between the columns of A:")
[A(:,1), B, A(:,2) ]

fprintf("\nDelete the 4th and 5th elements of a:")
a(4 : 5) = []

C = [1, 2, 3 ; 4, 5, 6 ; 7, 8, 9]

fprintf("\nDelete the 3rd row of C:")
new_matrix = C;
new_matrix(3, :) = []

fprintf("\nDelete the last column of C:")
new_matrix = C;
new_matrix(:, end) = []

fprintf("\nSort array a into ascending order:")
a = sort(a)

fprintf("\nReshape array a into an 3 x 2 array:")
a_3x2 = reshape(a, 3, 2)

fprintf("\nReshape array a into an 3 x 2 array row by row:")
a_3x2 = reshape(a', 2, 3)'