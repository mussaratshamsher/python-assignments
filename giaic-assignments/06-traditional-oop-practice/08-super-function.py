
# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Solution:

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with name: {self.name}")

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.subject ="Mathematics"
        print(f"{self.name} is a teacher of {self.subject}.")

person1 = Person("Ahmad")
teacher1 = Teacher("Ayan")

