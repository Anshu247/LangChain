from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

first_person: Person = {"name": "Professor", "age": 22}

# This will also work if you put {age: "25"} in str like this because TypeDict does not have data validation
second_person: Person = {"name": "Jon Snow", "age": "25"}

print(f"First Person: {first_person}")
print(f"Second Person: {second_person}")