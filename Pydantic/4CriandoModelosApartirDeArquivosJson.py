import json
from pydantic import BaseModel

#Class que representa uma pessoa
#Os nomes devem ser iguais aos nomes das chaves do arquivo json
class Person(BaseModel):
    name: str
    age: int
    location: str

    @classmethod
    def make_person_from_json(cls, file_path: str) -> "Person":
        with open(file_path) as file:
            return cls(**json.loads(file.read()))


person = Person.make_person_from_json("person.json")
print(person)     