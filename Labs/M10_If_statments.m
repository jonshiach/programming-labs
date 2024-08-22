clear % Clear all variables
clc   % Clear command window

% =========================================================================
% 10. If Statements
% =========================================================================

fprintf("\n10. If Statements\n-----------------\n")

% 10.1 Conditional statements
x = 1;
y = 2;

fprintf("\n10.1 Conditional statements\n---------------------------\n")
fprintf("%d == %d : %d \n", x, y, x == y)
fprintf("%d ~= %d : %d \n", x, y, x ~= y)
fprintf("%d > %d  : %d \n", x, y, x > y)
fprintf("%d < %d  : %d \n", x, y, x < y)
fprintf("%d >= %d : %d \n", x, y, x >= y)
fprintf("%d <= %d : %d \n", x, y, x <= y)

% 10.2 Logical Operators
fprintf("\n10.2 Logical operators\n----------------------\n\n")
fprintf(" x | y | x or y | x and y | not x | not y \n")
fprintf("------------------------------------------ \n")

x = 0;
y = 0;
fprintf(" %d | %d |   %d    |    %d    |   %d   |   %d\n", x, y, x || y, x && y, ~x, ~y)

x = 0;
y = 1;
fprintf(" %d | %d |   %d    |    %d    |   %d   |   %d\n", x, y, x || y, x && y, ~x, ~y)

x = 1;
y = 0;
fprintf(" %d | %d |   %d    |    %d    |   %d   |   %d\n", x, y, x || y, x && y, ~x, ~y)

x = 1;
y = 1;
fprintf(" %d | %d |   %d    |    %d    |   %d   |   %d\n", x, y, x || y, x && y, ~x, ~y)

% 10.3 If statements
x = 2;
y = 3;

fprintf("\n10.3 If statements\n------------------\n")
if x < y
    fprintf("%d is less than %d\n", x, y)
end

% 10.3.1 Else-if statements
hour = 21;

fprintf("\n10.3.1 Else-if statements\n-------------------------\n")
if hour < 12
    fprintf("Good morning, how are you today? \n")
   
elseif hour < 18
    fprintf("Good afternoon, are you having a good day? \n")

else
    fprintf("Good evening, did you have a good day? \n")

end