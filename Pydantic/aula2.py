#Pydantic - Basic Validators

from pydantic import BaseModel, field_validator

#Validade de campos -> field_validator

class Person(BaseModel):
    name: str
    age: int

    #Valida o campo name, que verifica se o nome contém apenas letras
    @field_validator("name")
    def check_name_is_alpha(n):
        if not n.isalpha():
            raise ValueError("Mensagem Personalizada que irá aparecer no console")
        return n

    @field_validator("age")
    def check_age_is_positive(n):
        if n < 1 or n > 100:
            raise ValueError(f"Idade errada!!!... {n}")
        return n

jhon = Person(name="Jhon", age=30)
print(jhon)