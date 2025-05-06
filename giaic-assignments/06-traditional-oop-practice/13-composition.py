

# 13. Composition
# Assignment:
# Create a class Engine and a class Car.
# Use composition by passing an Engine object to the Car class during initialization.
#  Access a method of the Engine class via the Car class.

# Solution:

class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"The {self.type} engine has started.")

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start(self):
        print(f"The {self.model} car is starting...")
        self.engine.start()

# Creating an Engine object
engine1 = Engine("Petrol")

# Creating a Car object with the Engine object
car1 = Car("Toyota", engine1)

# Starting the car, which in turn starts the engine
car1.start()
