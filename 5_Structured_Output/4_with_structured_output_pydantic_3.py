from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student_1(BaseModel):

    name: str
    age: Optional[int] =  None
    email: Optional[EmailStr] = None
    cgpa: float =  Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")

new_student_1 = {"name": "Jon Snow", "age": 25, "email": "professor@gmail.com", "cgpa": 7}
student_1 = Student_1(**new_student_1)

student_dict = dict(student_1)
student_json = student_1.model_dump_json() 

print(student_1)
print(student_dict)
print(student_dict["name"])
print(student_json)
