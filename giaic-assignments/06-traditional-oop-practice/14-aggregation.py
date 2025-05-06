
# Assignment:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# Solution:

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def __str__(self):
        return f"Employee Name: {self.name}, Position: {self.position}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(employee)

# Creating Employee objects independently
employee1 = Employee("Ali", "Software Engineer")
employee2 = Employee("Saf", "Data Scientist")

# Creating Department object and adding Employee objects to it
department = Department("Tech")
department.add_employee(employee1)
department.add_employee(employee2)

# Displaying employees in the department
department.show_employees()

