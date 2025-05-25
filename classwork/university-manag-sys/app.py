
# University Management System using oops

# Class for person to be use both in Admin & Student
class Person():
    def __init__(self,name:str, age:int, email:str, password:str ):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        print(f"Details:\nName: {self.name},\nAge: {self.age}, \nEmail: {self.email}, \nPassword: {self.password}")    
    def login(self):
        print("User login")

    def logout(self):
        print("User logout")

user = Person("Ali",20, "ali@gmail.com", "ABC123")
user.login()
# Class for admin
class Admin(Person):
    def __init__(self, name:str, age:int, email:str, password:str ):
      super().__init__(name,age, email, password)

    def login(self, admin_key):
        if admin_key != "1234":
           print("Invalid key") 
        else:
            print("Admin login")     
admin1 = Admin("Amar",30, "amar@gmail.com", "ABC123")
admin1.login("1234")    
# class for students
class Students(Person):
    def __init__(self, name, age, email, password, roll_num):
        super().__init__(name, age, email, password)
        self.roll_num = roll_num
        self.courses = []
    def register_for_course(self, course):
        self.courses.append(course)
        print(f"{self.name} registered for {course}")
# class Instructor
class Instructor(Person):
    def __init__(self, name, age, email, password, salary, courses):
        super().__init__(name, age,email, password)
        self.salary = salary
        self.courses = courses
    def assign_course(self, course):
        self.courses.append(course)
        print(f"Teacher{self.name} is assigned to {course}")
teacher1 = Instructor("Ali", 30, "ali@123", "ABC123", 50000, ["Math", "Science"])
teacher1.assign_course("English")        
# courses
class Course(Students):
    def __init__(self, course_id, course_name,  ):
        self.couse_id = course_id
        self.course_name = course_name

        

        

