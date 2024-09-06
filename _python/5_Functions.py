# Functions

# Declaring a function
def hello():
    print("Hello world")


hello()

# Local and global variables
def print_name():
    last_name = "Williams"
    print(f"Name: {first_name} {last_name}")


print()
first_name = "Ellie"
print_name()
# print(last_name)

# Arguments
def greet(name):
    print(f"Hello {name}")
    

print()
greet("Joel")
greet("Ellie")

# Multiple arguments
def print_name_and_age(first_name, last_name, age):
    print(f"Name: {first_name} {last_name}")
    print(f"Age : {age}")
    

print()
print_name_and_age("Joel", "Miller", 56)

# Arbitrary arguments
def print_name(*args):
    for name in args:
        print(f"{name}")
        

print()
print_name("Ellie", "Joel")
print()
print_name("Tommy", "Dina", "Jesse")

# Arbitrary keyword arguments
def print_name_and_age(**kwargs):
    print(f"Name: {kwargs['first_name']} {kwargs['last_name']}")
    print(f"Age : {kwargs['age']}")
    
    
print() 
print_name_and_age(age = 23, last_name = "Anderson", first_name = "Abby")
print_name_and_age(first_name = "Tommy", age = 53, last_name = "Miller")

# Return values
def double(x):
    return 2 * x


print()
print(double(3))
print(double(5))

# Multiple return values
from numpy import pi

def circle(radius):
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    
    return area, circumference


area, circ = circle(8)

print()
print(f"Area          : {area:8.4f}")
print(f"Circumference : {circ:8.4f}")

# Lambda functions
triple = lambda x : 3 * x

print()
print(triple(4))

# Returning a lambda function
def multiply(k):
    return lambda x : k * x


double = multiply(2)
triple = multiply(3)
quadruple = multiply(4)

print()
print(double(5))
print(triple(5))
print(quadruple(5)) 

# Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)
    
 
print()
print(f"6! = {factorial(6)}")