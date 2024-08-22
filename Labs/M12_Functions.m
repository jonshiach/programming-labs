% =========================================================================
% 12. Functions
% =========================================================================

% 12.1 Declaring functions
fprintf("12. Functions\n-------------\n")
hello()

% 12.1.1 Local variables
fprintf("\n12.1.1 Local variables\n----------------------\n")
print_name()
% fprintf("%s\n", name)

% 12.2 Function arguments
fprintf("\n12.2 Function arguments\n-----------------------\n")
print_age(19)
print_age(20)

% 12.2.1 Multiple arguments
fprintf("\n12.2.1 Multiple arguments\n-------------------------\n")
print_name_and_age("Joel", "Miller", 56)

% 12.2.2 Arbitrary arguments
fprintf("\n12.2.2 Arbitrary arguments\n--------------------------\n")
print_names("Ellie", "Joel")
print_names("Tommy", "Dina", "Jesse")

% 12.3 Return values
fprintf("\n12.3 Return values\n------------------\n")
double(3)
double(5)

% 12.3.1 Multiple return values
fprintf("\n12.3.1 Multiple return values\n-----------------------------\n")

[vol, area] = cylinder(1, 2);
fprintf("Volume       : %8.4f \n", vol)
fprintf("Surface area : %8.4f \n", area)

% 12.4 Anonymous functions
triple = @(x) 3 * x;

fprintf("\n12.4 Anonymous functions\n-----------------------\n")
triple(4)

% 12.4.1 Returning an anonymous function
my_double = multiply(2);
triple = multiply(3);
quadruple = multiply(4);

fprintf("\n12.4.1 Returning an anonymous function\n--------------------------------------\n")
fprintf("%d\n", my_double(5))
fprintf("%d\n", triple(5))
fprintf("%d\n", quadruple(5))

% 12.5 Recursion
fprintf("\n12.5 Recursion\n--------------\n")
fprintf("6! = %d\n", my_factorial(6))

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
