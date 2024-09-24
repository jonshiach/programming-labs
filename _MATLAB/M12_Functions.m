% 12. Functions

clear % Clear all variables
clc   % Clear command window

% Declaring functions
hello()

% Local variables
fprintf("\n")
print_name()
% fprintf("%s\n", name)

% Function arguments
fprintf("\n")
print_age(19)
print_age(20)

% Multiple arguments
fprintf("\n")
print_name_and_age("Joel", "Miller", 56)

% Arbitrary arguments
fprintf("\n")
print_names("Ellie", "Joel")
print_names("Tommy", "Dina", "Jesse")

% Return values
fprintf("\n")
double(3)
double(5)

% Multiple return values
[vol, area] = cylinder(1, 2);
fprintf("Volume       : %8.4f \n", vol)
fprintf("Surface area : %8.4f \n", area)

% Anonymous functions
triple = @(x) 3 * x;

triple(4)

% Returning an anonymous function
my_double = multiply(2);
triple = multiply(3);
quadruple = multiply(4);

fprintf("%d\n", my_double(5))
fprintf("%d\n", triple(5))
fprintf("%d\n", quadruple(5))

% Recursion
fprintf("\n6! = %d\n", my_factorial(6))

% ------------------------------------------------------------------------
function hello()

fprintf("hello world \n")

end

% -------------------------------------------------------------------------
function print_name()

name = "Ellie Williams";
fprintf("%s\n", name)

end

% -------------------------------------------------------------------------
function print_age(age)

fprintf("Age : %d \n", age)

end

% -------------------------------------------------------------------------
function print_name_and_age(first_name, last_name, age)

fprintf("Name : %s %s\n", first_name, last_name)
fprintf("Age  : %d\n", age)

end

% -------------------------------------------------------------------------
function print_names(varargin)

for i = 1 : nargin
    fprintf("%s\n", varargin{i})
end

end

% -------------------------------------------------------------------------
function y = double(x)

y = 2 * x;

end

% -------------------------------------------------------------------------
function [volume, surface_area] = cylinder(radius, height)

volume = height * pi * radius ^ 2;
surface_area = height * 2 * pi * radius;

end

% -------------------------------------------------------------------------
function anonymous_function = multiply(x)

anonymous_function = @(k) k * x;

end

% -------------------------------------------------------------------------
function y = my_factorial(n)

if n == 0 || n == 1
    y = n;
else
    y = n * my_factorial(n - 1);
end

end
