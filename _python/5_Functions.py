#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 5. Functions
# =============================================================================

print("\n5. Functions\n------------")

# 5.1 Declaring a function
print("\n5.1 Declaring a function\n------------------------")

def hello():
    print("Hello world")


hello()

# 5.1.1 Local and global variables
def print_name():
    last_name = "Williams"
    print(f"Name: {first_name} {last_name}")


print("\n5.1.1 Local and global variables\n--------------------------------")
first_name = "Ellie"
print_name()

# print(last_name)

# 5.2 Arguments
def greet(name):
    print(f"Hello {name}")
    
print("\n5.2 Function arguments\n----------------------")
greet("Joel")
greet("Ellie")

# 5.2.1 Multiple arguments
def print_name_and_age(first_name, last_name, age):
    print(f"Name: {first_name} {last_name}")
    print(f"Age : {age}")
    
    
print("\n5.2.1 Multiple arguments\n------------------------")
print_name_and_age("Joel", "Miller", 56)

# 5.2.2 Arbitrary arguments
def print_name(*args):
    for name in args:
        print(f"{name}")
        

print("\n5.2.2 Arbitrary arguments\n-------------------------")
print_name("Ellie", "Joel")
print_name("Tommy", "Dina", "Jesse")

# 5.2.3 Arbitrary keyword arguments
def print_name_and_age(**kwargs):
    print(f"Name: {kwargs['first_name']} {kwargs['last_name']}")
    print(f"Age : {kwargs['age']}")
    
    
print("\n5.2.3 Arbitrary keyword arguments\n---------------------------------")
print_name_and_age(age = 23, last_name = "Anderson", first_name = "Abby")
print_name_and_age(first_name = "Tommy", age = 53, last_name = "Miller")

# 5.3 Return values
def double(x):
    return 2 * x


print("\n5.3 Return values\n-----------------")
print(double(3))
print(double(5))

# 5.3.1 Multiple return values
def circle(radius):
    pi = 3.141592653589793
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    
    return area, circumference


area, circ = circle(8)

print("\n5.3.1 Multiple return values\n----------------------------")
print(f"Area          : {area:8.4f}")
print(f"Circumference : {circ:8.4f}")

# 5.4 Lambda functions
triple = lambda x : 3 * x

print("\n5.4 Lambda functions\n--------------------")
print(triple(4))

# 5.4.1 Returning a lambda function
def multiply(k):
    return lambda x : k * x


double = multiply(2)
triple = multiply(3)
quadruple = multiply(4)

print("\n5.4.1 Returning a lambda function\n---------------------------------")
print(double(5))
print(triple(5))
print(quadruple(5)) 

# 5.5 Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)
    
 
print("\n5.5 Recursion\n-------------")
print(f"6! = {factorial(6)}")