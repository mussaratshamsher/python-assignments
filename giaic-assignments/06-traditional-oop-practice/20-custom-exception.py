
# Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) 
# that raises this exception if age < 18. Handle it with try...except.

# Solution:

# Custom Exception Class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is less than 18")
    else:
        print("Age is valid.")

# Try-except block to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid number for age.")
