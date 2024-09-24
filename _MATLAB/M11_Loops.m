% 11. Loops

clear % Clear all variables
clc   % Clear command window

% For loops
subjects = ["linear algebra", "programming", "calculus"];

for subject = subjects
    fprintf("%s\n", subject)
end

fprintf("\n")

for i = 1 : 5
    fprintf("%d\n", i)
end

% Fibonacci sequence
a = 0;
b = 1;
fprintf("\n%i\n%i", a, b)

for i = 3 : 20
    c = a + b;
    fprintf("%1i\n", c)
    a = b;
    b = c;
end


% While loops
i = 1;

fprintf("\n")
while i < 6
    fprintf("%d\n", i)
    i = i + 1;
end

% Approximating the golden ratio
a = 1;
b = 1;
new_phi = 1;
old_phi = 0;
fprintf("\n%0.6f", new_phi)

while abs(new_phi - old_phi) > 1e-6
    c = a + b;
    a = b;
    b = c;
    old_phi = new_phi;
    new_phi = b / a;
    fprintf("%0.6f\n", new_phi)
end

% The break command
fprintf("\n")

for i = 1 : 5
    if i == 4
        break
    end

    fprintf("%1i\n", i)
end

% The continue command
fprintf("\n")

for i = 1 : 5
    if i == 4
        continue
    end

    fprintf("%1i\n", i)
end

% Nested loops
multiplication_square = ones(10, 10);

for i = 1 : 10
    for j = 1 : 10
        multiplication_square(i, j) = i * j;
    end
end

multiplication_square