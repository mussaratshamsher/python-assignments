

# # Object Oriented Programming (OOP) in Python
# # * class
# #    *method
# #    *Attribute
#     #  *class variable
#     #  *constructor : def __init__(self) #self: is additional parameter which is used to refer the instance of the class

# # class syntax => class ClassName:(): pass

# class Teacher():
#     counter: int = 0
#     helpline_number:str = "1234567890"

#     def __init__(self,teacher_id: int, teacher_name: str) -> None:
#         self.name:str = teacher_name
#         self.teacher_id:int = teacher_id
#         self.organization_name: str = "ABC School"
#         Teacher.counter += 1

#     def speaker(self, words: str) -> None:
#         print(f"{self.name} is speaking {words}")        

#     def teaching(self,subject:str) -> None:
#         print(f"{self.name} is teaching {subject}")

#     def details(self) -> None:
#         information:str =f"Teacher nameis{self.name}.Our helpline number is{Teacher.helpline_number}"

# obj1 : Teacher = Teacher(2, "John") 
# obj2 : Teacher = Teacher(3, "Doe")
# print(obj1.name)
# # Inheritance: 
# class Student(Teacher):
#     pass
# std1: Student = Student(1, "Ali")
# print(std1.name)
# print(std1.teacher_id)
# print(std1.helpline_number)
# print(std1.organization_name)

# # OOP: Object Oriented Programming

# # class Student():
# #     def __init__(self):   # init: constructor #magic function
# #         #self = {} # self is the instance of the class
# #         self.name = "Jhon"
# #         self.roll_num = roll
# #         self.age = 20
# # s1 = Student() 
# # print(s1.name) # Jhon

# class Student():
#     def __init__(self, roll:str):   # init: constructor #magic function
#         #self = {} # self is the instance of the class
#         self.name = "Jhon"
#         self.roll_num = roll
#         self.age = 20
# s1 = Student(roll="123") 
# print(s1.name) # Jhon
# s2 = Student(roll="122")
# print(s2.roll_num) # 122

# class Teacher():
#     def __init__(self, name:str, age:int, salary:int):
#         self.name =name
#         self.age = age
#         self.salary = salary
# teacher1 = Teacher(name="Ali", age=30, salary=20000)
# teacher2= Teacher(name="Sara", age=25, salary=25000) 
# print(teacher1.name) 
# print(teacher2.salary)      
class MyClass:
    def __init__(self, name):
        self.name = name
    def instance_method(self):
        print("This is an instance method")        
    @classmethod
    def class_method(cls):
        print("This is a class method")
    @staticmethod
    def static_method():
        print("This is a static method")    

# obj = MyClass("Ali")
# obj.instance_method()  # This is an instance method
# print(obj.name)  # Ali

# obj.class_method()  # This is a class method
# MyClass.class_method()  # This is a class method

# obj.static_method()  # This is a static method
# MyClass.static_method()  # This is a static method

# print(MyClass)
# print(MyClass.__name__)
# print(MyClass.__module__)
# print(MyClass.__dict__)
print(MyClass.__bases__)
print(MyClass.__class__)
print(MyClass.__doc__)
print(MyClass.__dir__)
print(MyClass.__init__)
print(MyClass.__new__)
print(MyClass.__str__)  
print(MyClass.__repr__)
print(MyClass.__sizeof__)
print(MyClass.__subclasshook__)
print(MyClass.__weakref__)  


        



   