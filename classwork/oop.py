
# OOP: Object Oriented Programming

# class Student():
#     def __init__(self):   # init: constructor #magic function
#         #self = {} # self is the instance of the class
#         self.name = "Jhon"
#         self.roll_num = roll
#         self.age = 20
# s1 = Student() 
# print(s1.name) # Jhon

class Student():
    def __init__(self, roll:str):   # init: constructor #magic function
        #self = {} # self is the instance of the class
        self.name = "Jhon"
        self.roll_num = roll
        self.age = 20
s1 = Student(roll="123") 
print(s1.name) # Jhon
s2 = Student(roll="122")
print(s2.roll_num) # 122

class Teacher():
    def __init__(self, name:str, age:int, salary:int):
        self.name =name
        self.age = age
        self.salary = salary
teacher1 = Teacher(name="Ali", age=30, salary=20000)
teacher2= Teacher(name="Sara", age=25, salary=25000) 
print(teacher1.name) 
print(teacher2.salary)      
        

        
