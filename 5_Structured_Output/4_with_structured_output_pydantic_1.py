from pydantic import BaseModel

class Student_1(BaseModel):

    name: str

new_student_1 = {"name": "Jon Snow"}
student_1 = Student_1(**new_student_1)

# new_student_2 = {"name": 10} # this does not work becasue we defined name should be string not integer so that it gives error, PyDantic gives data validation
# student_2 = Student_1(**new_student_2)

print(f"Student 1 Name: {student_1}")
# print(f"Student 2 Name: {student_2}")

print(f"Type: {type(student_1)}")

class Student_2(BaseModel):

    name: str = "Eleven" # setting default value, if value is not present then this by default value prints

new_student_3 = {}
student_3 = Student_2(**new_student_3)

print(f"Student 3 Name: {student_3}")