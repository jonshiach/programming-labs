% =========================================================================
% 11. Loops
% =========================================================================

fprintf("11. Loops\n---------\n")

% 10.1 For loops
subjects = ["linear algebra", "programming", "calculus"];

fprintf("\n11.1 For loops\n--------------\n")

for subject = subjects
    fprintf("%s\n", subject)
end

fprintf("\n")

for i = 1 : 5
    fprintf("%d\n", i)
end

% 11.1.1 Fibonacci sequence
F = [0, 1];

for n = 3 : 20
    F = [F, F(n-1) + F(n-2)];
end

fprintf("\n11.1.2 Fibonacci sequence\n------------------\n")
F

% 11.2 While loops
fprintf("\n11.2 While loops\n----------------\n")
i = 1;

while i < 6
    fprintf("%d\n", i)
    i = i + 1;
end

% Fibonacci number less than 1 million
F = [0, 1];

while F(end) + F(end - 1) < 1e6
    F = [F, F(end) + F(end - 1)];
end

fprintf("\nFibonacci numbers less than 1 million\n-------------------------------------\n")
F

% 11.3.1 The break command
for n = 3 : length(F)
    phi_estimate1 = F(n) / F(n - 1);
    phi_estimate2 = F(n+1) / F(n);

    if abs(phi_estimate1 - phi_estimate2) < 1e-6
        break
    end
end

fprintf("\n11.3.1 The break command\n------------------------\n")
fprintf("The estimated value of phi is %0.8f \n", phi_estimate2)
fprintf("The actual value of phi is %0.8f \n", (1 + sqrt(5)) / 2)

% 11.3.2 The continue command
sum_ = 0;

for n = F
    if mod(n, 2) == 1
        continue
    end

    sum_ = sum_ + n
end

fprintf("\n11.3.2 The continue command\n---------------------------\n")
fprintf("the sum of the even Fibonacci numbers less than 1 million is %d \n", sum_)

% 11.4 Nested loops
multiplication_square = ones(10, 10)

for i = 1 : 10
    for j = 1 : 10
        multiplication_square(i, j) = i * j;
    end
end

fprintf("\n11.4 Nested loops\n-----------------\n")
fprintf("10x10 multiplication square: \n")
multiplication_square