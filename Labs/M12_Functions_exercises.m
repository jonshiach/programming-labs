% =========================================================================
% 12. Functions Exercises
% =========================================================================

fprintf("\n12. Functions Exercises\n-------------------\n")

% Exercise 12.1
fprintf("\nExercise 12.1\n-------------\n")
loving_it()

% Exercise 12.2
fprintf("\nExercise 12.2\n-------------\n")
odd_or_even(2)
odd_or_even(5)
odd_or_even(0)

% Exercise 12.3
fprintf("\nExercise 12.3\n-------------\n")
my_isprime(3469)
my_isprime(6137)

% Exercise 12.4
fprintf("\nExercise 12.4\n-------------\n")
my_mean(1, 2, 3, 4)
my_mean(5, 3, 7, 5, 8, 2, 4, 2, 1)

% Exercise 12.5
fprintf("\nExercise 12.5\n-------------\n")
my_norm([1, 2, 3])
my_norm([4, 5, 6, 7])

% Exercise 12.6
fprintf("\nExercise 12.6\n-------------\n")
my_gcd(14, 245)
my_gcd(2414, 54145)

% Exercise 12.7
fprintf("\nExercise 12.7\n-------------\n")
my_sqrt(144)
my_sqrt(12345)

% Exercise 12.8
quadratic = @(x) 2 * x ^ 2 - 3 * x + 4;

fprintf("\nExercise 12.8\n-------------\n")
quadratic(2)
quadratic(3)

% Exercise 12.9
square = power_function(2);
cube = power_function(3);
quartic = power_function(4);

fprintf("\nExercise 12.9\n-------------\n")
square(123)
cube(123)
quartic(123)

% Exercise 12.10
fprintf("\nExercise 12.10\n--------------\n")
fprintf("1. The 10th Fibonacci number is %d\n", fibonacci(10))
fprintf("2. The 20th Fibonacci number is %d\n", fibonacci(20))
fprintf("3. The 40th Fibonacci number is %d\n", fibonacci(40))

% Exercise 12.11
A = [1, 2 ; 3, 4];
B = [-3, -3, 4 ; 6, -1, 3 ; -2, 6, 0];
C = [5, 2, -2, 6 ; -1, -1, 3, -1 ; 5, -1, 0, 1 ; 0, -3, 5, 2];

fprintf("\nExercise 12.11\n--------------\n")
fprintf("1. det(A) = %0.4f\n", my_det(A))
fprintf("2. det(B) = %0.4f\n", my_det(B))
fprintf("3. det(C) = %0.4f\n", my_det(C))

% ------------------------------------------------------------------------
function loving_it()

fprintf("I'm writing MATLAB programs and I'm loving it. \n")

end

% -------------------------------------------------------------------------
function odd_or_even(number)

if mod(number, 2) == 0
    fprintf("%d is an even number\n", number)
else
    fprintf("%d is an odd number\n", number)
end

end

% -------------------------------------------------------------------------
function my_isprime(number)

prime = true;

for i = 2 : number - 1
    if mod(number, i) == 0
        prime = false;
        break
    end
end

if prime
    fprintf("%d is a prime number\n", number)
else
    fprintf("%d is not a prime number\n", number)
end

end

% -------------------------------------------------------------------------
function my_mean(varargin)

sum_ = 0;
for i = 1 : nargin
    sum_ = sum_ + varargin{i};
end

fprintf("mean = %0.4f\n", sum_ / nargin)
end

% -------------------------------------------------------------------------
function norm = my_norm(vector)

norm = 0;

for i = vector
    norm = norm + i ^ 2;
end

norm = sqrt(norm);

end

% -------------------------------------------------------------------------
function x = my_gcd(x, y)

while y > 0
    r = mod(x, y);
    x = y;
    y = r;
end

end

% -------------------------------------------------------------------------
function x1 = my_sqrt(x)

x0 = 0;
x1 = 1;

while abs(x1 - x0) > 5e-5
    x0 = x1;
    x1 = (x1 + x / x1) / 2;
end

end

% -------------------------------------------------------------------------
function anonymous_function = power_function(k)

anonymous_function = @(x) x ^ k;

end

% -------------------------------------------------------------------------
function f = fibonacci(n)

if n == 1
    f = 0;

elseif n == 2
    f = 1;

else
    f = fibonacci(n - 1) + fibonacci(n - 2);
end

end

% -------------------------------------------------------------------------
function detA = my_det(A)

[m, n] = size(A);

if m ~= n
    error("Error! A must be a square array")

elseif n == 2
    detA = A(1,1) * A(2,2) - A(1,2) * A(2,1);

else
    detA = 0;
    
    for i = 1 : n
        Ai = [A(2:end,1:i-1), A(2:end,i+1:end)];
        detA = detA + (-1) ^ (i + 1) * A(1,i) * my_det(Ai);
    end
end

end
