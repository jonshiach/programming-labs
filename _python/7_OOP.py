#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 7. Classes
# =============================================================================

# 7.1 Classes
class Member:
    name = "Joel Miller"
    ID = 12345678
    
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    def print(self):
        print("\nUniversity Member Details\n-------------------------")
        print(f"Name     : {self.name}")
        print(f"ID       : {self.ID}")
    
joel = Member

print("\n7.1 Classes\n-----------")
print(joel.name)
print(joel.ID)

# 7.1.1 Changing the attributes
ellie = Member

print("\n7.1.1 Changing the attributes\n-----------------------------")
print(ellie.name)
print(ellie.ID)

ellie.name = "Ellie Williams"
ellie.ID = "24123456"

print()
print(ellie.name)
print(ellie.ID)

# 7.1.2 Constructors
tommy = Member("Tommy Miller", 87654321)

print("\n7.1.2 Constructors\n------------------")
print(tommy.name)
print(tommy.ID)

# 7.2 Methods
abby = Member("Abby Anderson", 24135791)

print("\n7.2 Methods\n-----------")
abby.print()

# 7.3 Inheritance
class Student(Member):
    position = "student"
    
    def __init__(self, name, ID, course):
        super().__init__(name, ID)
        self.course = course
    
    def print(self):
        super().print()
        print(f"Position : {self.position}")
        print(f"Course   : {self.course}")


ellie = Student("Ellie Williams", 24123456, "Mathematics")

print("\n7.3 Inheritance\n---------------")
ellie.print()
print(type(ellie))
print(ellie.position)