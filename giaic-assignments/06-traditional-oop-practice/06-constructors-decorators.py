# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and 
# another message when it is destroyed (destructor).

# Solution:

class Logger:
    def __init__(self):
        print(f"Logger is created.")

    def __del__(self):
        print(f"Logger is destroyed!")

logger = Logger()

del logger  # Explicitly calling the destructor
# In Python, the destructor is called when the object is deleted or goes out of scope.        


