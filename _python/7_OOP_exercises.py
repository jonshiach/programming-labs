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
        print(f"\nShape           : {self.name}")
        print(f"Number of edges : {self.number_of_edges}")


# Exercise 7.1
delorean  = Vehicle("Delorean", 100)
batmobile = Vehicle("Batmobile", 330)

print("\nExercise 7.1\n------------")
print(f"name      : {delorean.name}\nmax speed : {delorean.max_speed}\n")
print(f"name      : {batmobile.name}\nmax speed : {batmobile.max_speed}")

# Exercise 7.2
triangle = Shape('triangle', 3)
square   = Shape('square', 4)
circle   = Shape('circle', 0)

print("\nExercise 7.2\n------------")
print(f"Shape     : {triangle.name}\nNo. edges : {triangle.number_of_edges}\n")
print(f"Shape     : {square.name}\nNo. edges : {square.number_of_edges}\n")
print(f"Shape     : {circle.name}\nNo. edges : {circle.number_of_edges}\n")


# Exercise 7.3
delorean  = Vehicle("Delorean", 100)
batmobile = Vehicle("Batmobile", 330)

delorean.accelerate(88)
batmobile.accelerate(150)

print("\nExercise 7.3\n------------")
print(f"The speed of the Delorean is {delorean.speed} mph.")
print(f"The speed of the Batmobile is {batmobile.speed} mph.")

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
        print("\nBicycle details\n---------------")
        print(f"Name       : {self.name}")
        print(f"No. wheels : {self.number_of_wheels}")
        print(f"Max speed  : {self.max_speed} mph")


print("\nExercise 7.5\n------------")
chitty = Car("Chitty Chitty Bang Bang", 50)
bmx    = Bicycle("BMX", 20)
chitty.print()
bmx.print()

# Exercise 7.6
import numpy as np

class Triangle(Shape):
    name            = "triangle"
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
    
    def print(self):
        super().print()
        print(f"Side lengths    : {self.side1}, {self.side2}, {self.side3}")
        print(f"Area            : {self.area():0.4f}")
        print(f"Circumference   : {self.circumference():0.4f}")
    
    
class Rectangle(Shape):
    name            = "rectangle" 
    number_of_edges = 4
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def circumference(self):
        return 2 * self.width + 2 * self.height
    
    def area(self):
        return self.width * self.height

    def print(self):
        super().print()
        print(f"Side lengths    : {self.width}, {self.height}")
        print(f"Area            : {self.area():0.4f}")
        print(f"Circumference   : {self.circumference():0.4f}")

class Circle(Shape):
    name            = "circle"
    number_of_edges = 0
    
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        return 2 * np.pi * self.radius
    
    def area(self):
        return np.pi * self.radius ** 2
    
    def print(self):
        super().print()
        print(f"Radius          : {self.radius}")
        print(f"Area            : {self.area():0.4f}")
        print(f"Circumference   : {self.circumference():0.4f}")

triangle  = Triangle(3, 4, 5)
rectangle = Rectangle(16, 9)
circle    = Circle(5)

print("\nExercise 7.6\n------------")
triangle.print()
rectangle.print()
circle.print()
    
