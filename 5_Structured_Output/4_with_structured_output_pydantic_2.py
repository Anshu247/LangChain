from pydantic import BaseModel, EmailStr
from typing import Optional

class Student_1(BaseModel):

    name: str
    age: Optional[int] =  None
    email: Optional[EmailStr] = None

new_student_1 = {"name": "Jon Snow", "age": 25, "email": "professor@gmail.com"}
new_student_2 = {"name": "Eleven", "age": "24"} # Coerce, if age is in string format, the PyDantic is smart enough to understand this is a number and converts this into a integer

student_1 = Student_1(**new_student_1)
student_2 = Student_1(**new_student_2)

print(student_1)
print(student_2)