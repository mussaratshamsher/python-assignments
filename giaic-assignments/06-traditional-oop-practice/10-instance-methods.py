
# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() 
# that prints a message including the dog's name.

# Solution:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} {self.breed}.")

dog1 = Dog("Buddy", "Godlden Retriver")
dog2 = Dog("Max", "Bulldog")
dog1.bark()  # Output: Buddy says Woof! I am a Godlen Retriver.
dog2.bark()  # Output: Max says Woof! I am a Bulldog.            
