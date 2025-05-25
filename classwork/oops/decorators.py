
# Decorators in Classes:
#  Property decorators: Python provides specific property decorators (@property, @setter, and @deleter) to manage attribute access in a controlled way.
# @property, @setter, & @deleter
#  @property decorator is used to define a method as a getter for a class attribute

# Class Decorator:
# class CountCalls:
#     def __init__(self, func):
#         self.func = func
#         self.call_count = 0
#     def __call__(self, *args, **kwargs):
#         self.call_count += 1
#         print(f"Decorator called {self.call_count} times")
#         return self.func(*args, **kwargs)

# @CountCalls
# def say_hello(name):
#     print(f"Hello, {name}!")        
# say_hello("Alice")
# say_hello("Bob")

# @property decoarator
# class Person:
#     def __init__(self, name):
#         self._name = name
#     @property
#     def name(self):
#         """Getter for name"""
#         return self._name 
# p = Person("Ali")
# print(p.name)

# Setter: (Change a Value with Validation)
# class Person:
#     def __init__(self, name):
#         self._name = name
#         @property
#         def name(self):
#            return self._name
#         @name.setter
#         def name(self, new_name):
#             if not isinstance(new_name, str):
#                 raise ValueError("Name must be a string!") 
#             self._name = new_name
# p = Person("Babloo")
# p.name = "Babloo Khan"  
# print(p.name) 

# Deleter: (Delete a Value)
# class Person:
#     def __init__(self, name):
#         self._name = name
#     @property
#     def name(self):
#         return self._name
#     @name.deleter
#     def name(self):
#         print("Deleting name...")
#         del self._name
# p = Person("Dolly")            
# print(p.name)
# del p.name

# def my_func(features):
#     def car():
#         print("Toyota")
#     features()

# @my_func
# def color():
#     print("Black")

# color()

# property -> Encapsulation (Getter And Setter)
# classmethod
# staticmethod
# abstractmethod