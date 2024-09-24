# Exercise 5.1
def loving_it():
    print("I'm writing Python programs and I'm loving it.")


print("\nExercise 5.1\n------------")
loving_it()

# -----------------------------------------------------------------------------
# Exercise 5.2
def odd_or_even(x):
    if x % 2 == 0:
        print(f"{x} is an even number")
        
    else:
        print(f"{x} is an odd number")
        

print("\nExercise 5.2\n------------")
odd_or_even(2)
odd_or_even(5)
odd_or_even(0)

# -----------------------------------------------------------------------------
# Exercise 5.3
def isprime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
            break
    
    if prime:
        print(f"{x} is a prime number")
        
    else:
        print(f"{x} is not a prime number")
            
    
print("\nExercise 5.3\n------------")
isprime(3469)
isprime(6137)

# -----------------------------------------------------------------------------
# Exercise 5.4
def mean(*args):
    
    # Calculate mean
    n = len(args)
    mean = 0
    
    for x in args:
        mean += x
        
    mean /= n
    
    # Output mean
    print(f"mean = {mean:0.4f}")
    
    
print("\nExercise 5.4\n------------")
mean(1, 2, 3, 4)
mean(5, 3, 7, 5, 8, 2, 4, 2, 1)

# -----------------------------------------------------------------------------
# Exercise 5.5
import numpy as np

def norm(vec):
    sum_ = 0
    for x in vec:
        sum_ += x * x
        
    return np.sqrt(sum_)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])

print("\nExercise 5.5\n------------")
print(f"1. The magnitude of the vector {a} is {norm(a):0.4f}")
print(f"2. The magnitude of the vector {b} is {norm(b):0.4f}")

# -----------------------------------------------------------------------------
# Exercise 5.6
def gcd(x, y):
    while y > 0:
        x, y = y, y % x
        
    return x

print("\nExercise 5.6\n------------")
print(f"1. The GCD of 9 and 15 is {gcd(9, 15)}")
print(f"2. The GCD of 14 and 245 is {gcd(14, 245)}")

# -----------------------------------------------------------------------------
# Exercise 5.7
def sqrt(x):
    x0, x1 = 0, 1
    while abs(x0 - x1) > 5e-5:
        x0 = x1
        x1 = (x1 + x / x1) / 2
        
    return x1


print("\nExercise 5.7\n------------")
print(f"1. sqrt({144}) = {sqrt(144):0.6f}")
print(f"2. sqrt({12345}) = {sqrt(12345):0.6f}")

# -----------------------------------------------------------------------------
# Exercise 5.8
f = lambda x : 2 * x ** 2 - 3 * x + 4

print("\nExercise 5.8\n------------")
print(f(2))
print(f(3))

# -----------------------------------------------------------------------------
# Exercise 5.9
def power_function(n):
    return lambda x : x ** n

square = power_function(2)
cube = power_function(3)
quartic = power_function(4)

print("\nExercise 5.9\n-----------")
print(square(123))
print(cube(123))
print(quartic(123))

# -----------------------------------------------------------------------------
# Exercise 5.10
def fibonacci(n):
    if n == 1:
        return 0
    
    elif n == 2:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

print("\nExercise 5.10\n-------------")
print(f"1. The 10th Fibonacci number is {fibonacci(10)}")
print(f"2. The 20th Fibonacci number is {fibonacci(20)}")
print(f"3. The 40th Fibonacci number is {fibonacci(40)}")

# -----------------------------------------------------------------------------
# Exercise 5.11
def det(A):
    m, n = A.shape
    if m != n:
        print("Error! A must be a square array.")
        return 0
    
    if n == 1:
        return A[0,0]
    
    elif n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    else:
        detA = 0
        for i in range(n):
            Ai = np.delete(A, i, 1)  # remove column i
            Ai = np.delete(Ai, 0, 0) # remove row 1
            detA += (-1) ** (i + 2) * A[0,i] * det(Ai)
        
        return detA

        

A = np.array([[1, 2], [3, 4]])    
B = np.array([[-3, -3, 4], [6, -1, 3], [-2, 6, 0]])    
C = np.array([[5, 2, -2, 6], [-1, -1, 3, -1], [5, -1, 0, 1], [0, -3, 5, 2]])

print("\nExercise 5.11\n-------------") 
print(f"1. det(A) = {det(A)}")
print(f"2. det(B) = {det(B)}")
print(f"3. det(C) = {det(C)}")
            
