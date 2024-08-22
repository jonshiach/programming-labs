% =========================================================================
% 11. Loops Exercises
% =========================================================================

fprintf("\n11. Loops Exercises\n-------------------\n")

% Exercise 11.1
fprintf("\nExercise 11.1\n-------------\n")
for i = 1 : 10
    fprintf("hello world\n")
end

% Exercise 11.2
n = 52;
n_factorial = 1;

for i = 1 : n
    n_factorial = n_factorial * i;
end

fprintf("\nExercise 11.2\n-------------\n")
fprintf("%d! = %d\n", n, n_factorial)

% Exercise 11.3
x = pi / 4;
sinx = 0;

for n = 0 : 4
    sinx = sinx + (-1) ^ n / factorial(2 * n + 1) * x ^ (2 * n + 1);
end

fprintf("\nExercise 11.3\n--------------\n")
fprintf("sin(pi/4) = %0.16f \n", sinx)

% Exercise 11.4
i = 1;
fprintf("\nExercse 11.4\n------------\n")
while i < 11
    fprintf("hello again\n")
    i = i + 1;
end

% Exercise 11.5
x = 100;
num_steps = 0;
fprintf("\n step |   n \n--------------\n   0  | %4d \n", x)

while x > 1
    if mod(x, 2) == 0
        x = x / 2;
    else
        x = 3 * x + 1;
    end

    num_steps = num_steps + 1;
    fprintf("%4d  | %4d \n", num_steps, x)

end

% Exercise 11.6
numbers = [1009, 2123, 6269, 8441];
fprintf("\nExercise 11.6\n-------------\n")

for n = numbers
    prime = true;

    for i = 2 : n - 1
        if mod(n, i) == 0
            prime = false;
            break
        end
    end

    if prime
        fprintf("%d is prime \n", n)
    else
        fprintf("%d is not prime \n", n)
    end
end

% Exercise 11.7
fprintf("\nExercise 4.7\n------------\n")
fprintf("I'm thinking of a number between 0 and 100, guess what it is. \n")

n = randi(100);
guesses_left = 5;

while false
    guess = input(sprintf("\nYou have %d guesses remaining > ", guesses_left));
    guesses_left = guesses_left - 1;

    if guess == n
        fprintf("Congratulations, you win! \n")
        break

    elseif guess < n
        fprintf("Unlucky, your guess is less than my number \n")

    elseif guess > n
        fprintf("Unlucky, your guess is greater than my number \n")

    end

    if guesses_left == 0
        fprintf("Oh dear, you lose. My number was %d \n", n)
        break
    end
end

% Exercise 11.8
A = [3, 2, -1, 4 ; 7, -4, 0, 2];
B = [1, 0 ; 3, -2 ; 3, 6 ; -1, 4];
AB = zeros(size(A, 1), size(B, 2));

for i = 1 : size(A, 1)
    for j = 1 : size(B, 2)
        for k = 1 : size(A, 2)
            AB(i, j) = AB(i, j) + A(i, k) * B(k, j);
        end
    end
end

fprintf("\nExercise 11.8\n-------------")
A
B
AB

temp = A;
A = B;
B = temp;
BA = zeros(size(A, 1), size(B, 2));

for i = 1 : size(A, 1)
    for j = 1 : size(B, 2)
        for k = 1 : size(A, 2)
            BA(i, j) = BA(i, j) + A(i, k) * B(k, j);
        end
    end
end

BA


