# Exercise 4.1
print("Exercise 4.1\n------------")

for _ in range(10):
    print("hello world")
    
# -----------------------------------------------------------------------------
# Exercise 4.2
print("\nExercise 4.2\n------------")
n, n_factorial = 52, 1

for i in range(n):
    n_factorial *= i + 1
    
print(f"{n}! = {n_factorial}")

# -----------------------------------------------------------------------------
# Exercise 4.3
print("\nExercise 4.3\n-------------")

import math

x = math.pi / 4
sinx = 0

for n in range(5):
    sinx += (-1) ** n / math.factorial(2 * n + 1) * x ** (2 * n + 1)
    
print(f"sin(pi / 4) = {math.sin(x)}")

# -----------------------------------------------------------------------------
# Exercise 4.4
print("\nExercise 4.4\n------------")

i = 0
while i < 10:
    print("hello again")
    i += 1
  
# -----------------------------------------------------------------------------  
# Exercise 4.5
print("\nExercise 4.5\n------------")

x = 100
num_steps = 0

print(f" step |   n\n--------------\n    0 | {x:4d}")

while x > 1:
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
        
    num_steps += 1
    
    print(f" {num_steps:4d} | {x:4d}")
    
print(f"\nThe sequence took {num_steps} steps to reach 1.")

# -----------------------------------------------------------------------------
# Exercise 4.6
print("\nExercise 4.6\n------------")

import numpy as np

numbers = np.array([1009, 2123, 6269, 8441])

for n in numbers:
    prime = True
        
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    
    if prime:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")

# -----------------------------------------------------------------------------
# Exercise 4.7
print("\nExercise 4.7\n------------")
print("I'm thinking of a number between 0 and 100, guess what it is.")

n = np.random.randint(0, 100)
guesses_left = 5

while False: # Change to False to avoid having to run the game each time
    guess = int(input(f"\nYou have {guesses_left} guesses remaining > "))
    guesses_left -= 1
    
    if guess == n:
        print("Congratulations, you win!")
        break
    
    elif guess < n:
        print("Unlucky, your guess is less than my number.")
        
    elif guess > n:
        print("Unlucky, your guess is greater than my number.")
        
    if guesses_left == 0:
        print("Oh dear, you lose.")
        break
      
# -----------------------------------------------------------------------------  
# Exercise 4.8
print("\nExercise 4.8\n------------")

A = np.array([[3, 2, -1, 4], [7, -4, 0, 2]])
B = np.array([[1, 0], [3, -2], [3, 6], [-1, 4]])
AB = np.zeros((A.shape[0], B.shape[1]))

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            AB[i,j] += A[i,k] * B[k,j] 
            
print(f"AB = \n\n {AB} \n")

BA = np.zeros((B.shape[0], A.shape[1]))
for i in range(B.shape[0]):
    for j in range(A.shape[1]):
        for k in range(B.shape[1]):
            BA[i,j] += B[i,k] * A[k,j] 
            
print(f"2. AB = \n\n {BA}")