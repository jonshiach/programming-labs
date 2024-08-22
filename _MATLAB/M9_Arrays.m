clc % Clear the command window

% =========================================================================
% 2. Arrays
% =========================================================================

fprintf("9. Arrays\n---------\n")

% 9.1 Declaring arrays
fprintf("\n9.1 Declaring arrays\n--------------------")
a = [1, 2, 3]

A = [1, 2 ; 3, 4]

b = (1 : 9)

c = (0 : 2 : 20)

d = (10 : -1 : 1)

% 9.1.2 Special matrices
fprintf("9.1.2 Special matrices\n----------------------\n")
fprintf("1x6 array of zeros")

zeros(1, 6)
ones(4, 4)
eye(5)

% 9.2 Array indexing
fprintf("\n9.2 Array indexing\n------------------\n")
fprintf("The first element in a is %d \n", a(1))
fprintf("The second element in a is %d \n", a(2))
fprintf("The last element in a is %d \n", a(end))
fprintf("The element in row 1 column 1 of A is %d \n", A(1,1))
fprintf("The element in row 2 column 1 of A is %d \n", A(2, 1))

% 9.2.1 Array sizes
fprintf("\n9.2.1 Array sizes\n-----------------\n")
fprintf("The 1D array a has %d elements\n", length(a))
fprintf("The 2D array A has %d rows and %d columns\n", size(A, 1), size(A, 2))

% 9.2.2 Array slicing
fprintf("\n9.2.2 Array slicing\n-------------------\n")
fprintf("The first 4 elements of b are")
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

% 9.3 Array operations
B = [5, 6 ; 7, 8];

fprintf("\n9.3 Array operations\n--------------------\n")
A
B

fprintf("A + B =")
A + B

fprintf("A - B =")
A - B

fprintf("2A =")
2 * A

fprintf("A^T =")
A'

fprintf("A .* B =")
A .* B

fprintf("A * B = ")
A * B

fprintf("ABA =")
A * B * A

fprintf("A .^ 2 =")
A .^ 2

fprintf("A ^ 2 =")
A ^ 2

fprintf("det(A) = %0.2f \n", det(A))

fprintf("\ninv(A) =")
inv(A)

fprintf("\nA * inv(A) = \n", A * inv(A))
A * inv(A)

% 9.4 Manipulating arrays
fprintf("\n9.4 Manipulating arrays\n-----------------------\n")
a

fprintf("\nAppend [4, 5] to array a:")
a = [a, [4, 5]]

fprintf("\nAppend B to the bottom of A:")
C = [A ; B]

fprintf("\nAppend B to the right of A:")
D = [A , B]

fprintf("\nInsert [6, 7, 8] into the array a:")
a = [a(1 : 2), [6, 7, 8], a(3:end)]

fprintf("\nInset B between the rows of A:")
E = [A(1,:) ; B ; A(2,:) ]

fprintf("\nInsert B between the columns of B:")
F = [A(:,1), B, A(:,2) ]

fprintf("\nRemove the numbers 7 and 8 fron array a:")
a(4 : 5) = []

fprintf("\nDelete the 3rd row of C:")
G = C;
G(3, :) = []

fprintf("\nDelete the 2nd column of D:")
H = D;
H(:, 2) = []

fprintf("\nSort array a into ascending order:")
a = sort(a)

fprintf("\nReshape array a into an 3 x 2 array:")
I = reshape(a, 3, 2)

fprintf("\nReshape array a into an 3 x 2 array row by row:")
J = reshape(a', 2, 3)'