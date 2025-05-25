# . Practical Coding Task 
# ➢ Scenario: 
# Build a system for a Zoo Management App that uses inheritance and polymorphism to manage 
# animals. 
# ❖ Your Requirements: 
# Create a Base Class: Animal 
# • Attributes: 
# o name, species 
# • Method: 
# o make_sound() – returns "Some generic sound" 
# Create 3 Child Classes: 
# 1. Dog – Overrides make_sound() → "Bark!" 
# 2. Cat – Overrides make_sound() → "Meow!" 
# 3. Lion – Overrides make_sound() → "Roar!" 
# Use super() to initialize base class in each child. 

#Solution:
class Animal:
    def __init__(self, name:str, species:str):
        self.name = name
        self.species = species
    def make_sound(self) -> str:
        return "Some  generic Sound"
    def info(self) -> str:
        return f"{self.name} is a {self.species}"
    
# Inheritance and Polymorphism
class Dog(Animal):
    def __init__(self, name:str, species:str):
        super().__init__(name, species)
    def make_sound(self):
        return "Dogs Bark!"
    def info(self) -> str:
        return super().info() + " and it is a loyal animal"
        
class Cat(Animal):
    def __init__(self, name:str, species:str):
        super().__init__(name, species)            
    def make_sound(self):
        return "Cat Meow!"
    def info(self) -> str:
        return super().info() + " and it is a pet animal"
    
class Lion(Animal):
    def __init__(self, name:str, species:str):
        super().__init__(name, species)
    def make_sound(self):
        return "Lion Roar!"
    def info(self) -> str:
        return super().info() + " and it is a wild animal"
# Create instances of each animal
print("Animal Management System")
print("=====================================")  
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")
lion = Lion("Simba", "Lion")
# Print the information of each animal
print("Animal Information:")
print(dog.info())
print(cat.info())
print(lion.info())
# Print the sounds made by each animal
print(f"{dog.name} the {dog.species} says: {dog.make_sound()}")
print(f"{cat.name} the {cat.species} says: {cat.make_sound()}")
print(f"{lion.name} the {lion.species} says: {lion.make_sound()}")


