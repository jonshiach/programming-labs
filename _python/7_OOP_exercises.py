#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 7. Object Orientated Programming exercises
# =============================================================================

print("\n7. Object Orientated Programming Exercises\n------------------------------------------")


class Vehicle:
    speed = 0

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def accelerate(self, increase):
        self.speed = max(self.speed + increase, self.max_speed)


class Shape:
    
    def __init__(self, name, number_of_edges):
        self.name = name
        self.number_of_edges = number_of_edges
        
    def print(self):
        print(f"A {self.name} has {self.number_of_edges} edges")


# Exercise 7.1
delorean = Vehicle("Delorean", 100)
batmobile = Vehicle("Batmobile", 330)

print("\nExercise 7.1\n------------")
print(delorean.name)
print(delorean.max_speed)
print(batmobile.name)
print(batmobile.max_speed)

# Exercise 7.2
triangle = Shape('triangle', 3)
square = Shape('square', 4)
circle = Shape('circle', 0)

print("\nExercise 7.2\n------------")
print(triangle.name)
print(triangle.number_of_edges)
print(square.name)
print(square.number_of_edges)
print(circle.name)
print(circle.number_of_edges)

# Exercise 7.1
delorean = Vehicle("Delorean", 100)
batmobile = Vehicle("Batmobile", 330)
delorean.accelerate(88)
batmobile.accelerate(150)

# Exercise 7.3
print("\nExercise 7.3\n------------")
print(delorean.speed)
print(batmobile.speed)

# Exercise 7.4
print("\nExercise 7.4\n------------")
triangle.print()
square.print()
circle.print()

# Exercise 7.5
class Car(Vehicle):
    number_of_wheels = 4
    
    def print(self):
        print("\nCar details\n-----------")
        print(f"Name       : {self.name}")
        print(f"No. wheels : {self.number_of_wheels}")
        print(f"Max speed  : {self.max_speed} mph")
        

class Bicycle(Vehicle):
    number_of_wheels = 2
    
    def print(self):
        print("\nBicycle details\n-----------")
        print(f"No. wheels : {self.number_of_wheels}")
        print(f"Max speed  : {self.max_speed} mph")


print("\nExercise 7.5\n------------")
delorean = Car("Delorean", 110)
delorean.print()

# Exercise 7.6
import numpy as np

class Triangle(Shape):
    number_of_edges = 3
    
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def circumference(self):
        return self.side1 + self.side2 + self.side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return np.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    
class Rectangle(Shape):
    number_of_edges = 4
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def circumference(self):
        return 2 * self.width + 2 * self.height
    
    def area(self):
        return self.width * self.height


class Circle(Shape):
    number_of_edges = 0
    
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        return 2 * np.pi * self.radius
    
    def area(self):
        return np.pi * self.radius ** 2
    

triangle = Triangle(4, 5, 6)
rectangle = Rectangle(3, 4)

print("\nExercise 7.6\n------------")
print(triangle.circumference())
print(triangle.area())
print(rectangle)

    
