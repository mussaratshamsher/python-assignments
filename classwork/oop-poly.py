# variable belongs to methods, methods belong to objects
# Polymorphism
# i. overriding & polymorphism:
# polymorphisn is achieved by method overriding

class Animal:
    def eating(self, food:str) -> None:
        print(f"Animal is eating {food}")
class Bird(Animal):
    def eating(self, food:str) -> None:
        print(f"Bird is eating {food}.") 
bird: Bird = Bird()
bird.eating("seeds")  # Bird is eating seeds 

animal: Animal = Animal()
animal.eating("grass")
# runtime polymorphism: decides at runtime which method to run
animal: Animal = Bird() 
animal.eating("grass")

#  Overloading for methods
from typing import Union, overload

class Adder:
    @overload
    def add(self, x:int, y:int) -> int:
        ...
    @overload
    def add(self, x:float, y:float) -> float:
        ...   
    @overload
    def add(self, x:str, y:str) -> str:
        ...

    def add(x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(x, str) and isinstance(y, str):
            return x + y
        elif isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return x + y
        else:
            print("Error: Unsupported types for addition")
        
    # print("Int: ",add(1, 2))        # 3
    # print("Float: ",add(1.5, 2.5))  # 4.0
    # print("Str: ",add("Hello", " World"))  # Hello World
    # print("Str: ",add("Hello", 1))  # TypeError: Unsupported types for addition



