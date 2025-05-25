#  Practical Coding Task: 
# ➢ Scenario: 
# You're building a simple calculator class. This calculator can add, subtract, multiply, and divide two 
# numbers. You’ll use separate methods for each operation, and then a method to display all results 
# together. 
# ▪ Task Requirements: 
# 1. Create a class named Calculator. 
# 2. Use _ _init_ _() to take two numbers: num1 and num2. 
# 3. Add the following methods: 
# o add() 
# o subtract() 
# o multiply() 
# o divide() (add check: division by zero) 
 
# 4. Add a method show_all() that: 
# o Calls all the above methods 
# o Prints results in this format: 
# 5. Create one object with numbers of your choice (e.g., 10 and 2), and call show_all(). 

# Solution:

class Calculator:
    def __init__(self, num1:float, num2:float):
        self.num1 = num1
        self.num2 = num2

    def add(self):
            return self.num1 + self.num2
    def subtract(self):
            return self.num1 - self.num2
    def multiply(self):
            return self.num1 * self.num2
    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return self.num1 /self.num2
    def show_all(self):
                print(f"Addition: {self.add()}")
                print(f"Subtraction: {self.subtract()}")
                print(f"Multiplication: {self.multiply()}")
                print(f"Division: {self.divide()}")
# # Create an object of the Calculator class
# calc = Calculator(10, 2)
# # Call the show_all method to display results
# calc.show_all()

# CLI-based user input
def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        calc = Calculator(num1, num2)
        print("\nResults:")
        calc.show_all()
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
# main()

print(Calculator.__doc__)
print(Calculator.__name__)
print(Calculator.__module__)
print(Calculator.mro())
