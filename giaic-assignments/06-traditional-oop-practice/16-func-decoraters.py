

#  Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello().

# Solution:
# Decorator fucntion
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Applying decorator to function
@log_function_call
def say_hello():
    print("Hello, world!")

# Calling decorator fucntion     
say_hello()

