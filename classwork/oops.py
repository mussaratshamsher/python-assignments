

# Object Oriented Programming (OOP) in Python
# * class
#    *method
#    *Attribute
    #  *class variable
    #  *constructor : def __init__(self) #self: is additional parameter which is used to refer the instance of the class

# class syntax => class ClassName:(): pass

class Teacher():
    counter: int = 0
    helpline_number:str = "1234567890"

    def __init__(self,teacher_id: int, teacher_name: str) -> None:
        self.name:str = teacher_name
        self.teacher_id:int = teacher_id
        self.organization_name: str = "ABC School"
        Teacher.counter += 1

    def speaker(self, words: str) -> None:
        print(f"{self.name} is speaking {words}")        

    def teaching(self,subject:str) -> None:
        print(f"{self.name} is teaching {subject}")

    def details(self) -> None:
        information:str =f"Teacher nameis{self.name}.Our helpline number is{Teacher.helpline_number}"

obj1 : Teacher = Teacher(2, "John") 
obj2 : Teacher = Teacher(3, "Doe")
print(obj1.name)
# Inheritance: 
class Student(Teacher):
    pass
std1: Student = Student(1, "Ali")
print(std1.name)
print(std1.teacher_id)
print(std1.helpline_number)
print(std1.organization_name)
# 


   