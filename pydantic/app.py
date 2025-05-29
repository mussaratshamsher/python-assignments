
# Pydantic: data validation and settings management using Python type annotations.

from pydantic import BaseModel,validator, EmailStr
import datetime
from enum import Enum

class Standard(Enum):
    primary = 5
    secondary = 8
    matriculation = 10

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr
    dob: datetime.date
    standard: Standard 
    @validator('age')
    def validate_age(cls, v):
        if v>= 18:
            raise ValueError('Age must be less than 18')
        return v
s1 = Student(
    name = "John Doe",
    age = 15,
    email = "JohnDoe@email.com",
    dob = datetime.date(2003, 5, 15),
    standard = Standard.secondary
)  

print(s1)
