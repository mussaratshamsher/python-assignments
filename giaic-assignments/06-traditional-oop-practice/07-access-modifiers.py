
# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variable

# Solution:
class Employee:
   def __init__(self, name, _salary, __ssn):
      self.name = name # Public variable
      self._salary = _salary # Protected variable
      self.__ssn = __ssn
      print(f"Employee name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")

Employee1 = Employee("Ali", 50000, "123-45-6789")

  

