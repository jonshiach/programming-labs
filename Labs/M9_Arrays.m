% =========================================================================
% 2. Arrays
% =========================================================================

fprintf("\n9. Arrays\n---------\n")

% 9.1 Declaring arrays
fprintf("9.1 Declaring arrays\n--------------------")
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

% 9.4 Manipulating arrays
fprintf("\n9.4 Manipulating arrays\n-----------------------\n")
a
a = [a, [4, 5]]

C = [A, B]

D = [A ; B]

a = [a(1 : 2), [6, 7, 8], a(3:end)]

E = [A(1,:) ; B ; A(2,:) ]

F = [A(:,1), B, A(:,2) ]

a = sort(a)

a = sort(a, 'descend')

a = (1:6)
G = reshape(a, 3, 2)