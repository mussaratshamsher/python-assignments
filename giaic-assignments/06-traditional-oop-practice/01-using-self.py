
# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Creating an instance of the Student class
student1 = Student("Alice", 85)

# Displaying the student details
student1.display()


        


