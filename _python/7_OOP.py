# 7. Object Orientated Programmign

# Classes
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

print(joel.name)
print(joel.ID)

# Changing the attributes
ellie = Member

print()
print(ellie.name)
print(ellie.ID)

ellie.name = "Ellie Williams"
ellie.ID = "24123456"

print()
print(ellie.name)
print(ellie.ID)

# Constructors
tommy = Member("Tommy Miller", 87654321)

print()
print(tommy.name)
print(tommy.ID)

# Methods
abby = Member("Abby Anderson", 24135791)

print()
abby.print()

# Inheritance
class Student(Member):
    position = "Student"
    
    def __init__(self, name, ID, course):
        super().__init__(name, ID)
        self.course = course
    
t u    def print(self):
        super().print()
        print(f"Position : {self.position}")
        print(f"Course   : {self.course}")


ellie = Student("Ellie Williams", 24123456, "Mathematics")

print("\n7.3 Inheritance\n---------------")
ellie.print()
print()
print(type(ellie))
print()
print(ellie.position)