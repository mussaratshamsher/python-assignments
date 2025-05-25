
# Composition and Aggregation
# MRO: Method Resolution Order

# Composition: strong Relationship
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine() # Composition: car *has a* Engine
    def start(self):
        return f"Car starting: {self.engine.start()}"

# Aggregation: Weak Relationship
class Department:
    def __init__(self, name):
        self.name = name
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []  # Aggregation: university *has a* list of Departments           
    def add_departments(self, department):
        self.departments.append(department)

# MRO: Method Resolution Order: tells the order in which classes are searched when a method is called
# tells the class hierarchy. Python uses C3 linearization algorithm to determine the order.
# MRO is important for multiple inheritance to confusion .

print(Car.__mro__) # Car, object
print(University.__mro__) # University, object
print(Department.__mro__) # Department, object
class Student(University, Car):
    pass
class Teacher(Department):
    def greet(self):
        return "Hello, I am a teacher"
print(Student.__mro__) # Student, University, Car, object   
print(Teacher.__mro__) # Teacher, Department, object