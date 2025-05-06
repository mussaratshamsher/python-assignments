#Encapsulation & Access modifiers in Python
# i. public: accessible from anywhere in the code
# ii. protected: accessible from the class and its subclasses (not enforced in Python, but by convention, we use a single underscore prefix)
# iii. private: accessible only within the class (enforced in Python, we use a double underscore prefix)

class Person:
    def __init__(self, name:str, age:int, phone:int):
        self.name: str = name
        self._age: int = age
        self.__phone: int = phone
        print(f"Ali's phone number is {self.__phone}") #can be accessed only within the class
        
person1: Person = Person("Ali", 25, 1234567890)
print(person1.name)  # Ali : public
print(person1._age)  # 25 :Protected
# print(person1.__phone)  # AttributeError: 'Person' object has no attribute '__phone' 

#ABSTRACTION:
# i. Abstract classes: classes that cannot be instantiated and are meant to be subclassed. They can have abstract methods (methods without implementation) and concrete methods (methods with implementation).
# ii. Abstract methods: methods that are declared but contain no implementation. They must be implemented in the subclasses.
# iii. Interfaces: a special type of abstract class that only contains abstract methods. In Python, we can use the `abc` module to create interfaces.
# iv. Abstract classes can have concrete methods, but interfaces cannot. Interfaces are used to define a contract that the implementing classes must follow.
# v. Abstract classes can have instance variables, while interfaces cannot. Interfaces only define method signatures without any implementation or state.
# vi. Abstract classes can have constructors, while interfaces cannot. Interfaces do not have any state or behavior, so they do not require a constructor.
# vii. Abstract classes can be used to provide a common base for related classes, while interfaces are used to define a common contract for unrelated classes.

from abc import ABC, abstractmethod

class Animal(ABC): #to make abstract class, in parent class pass ABC as parameter
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.living_things : bool = True
class Cat(Animal):
    def __init__(self):
        super().__init__()
        
cat: Cat = Cat()
print(cat.living_things)







