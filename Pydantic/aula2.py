#Pydantic - Basic Validators

from pydantic import BaseModel, field_validator

#Validade de campos simples -> field_validator

class Person(BaseModel):
    f_name: str
    f_second_name: str
    age: int

    #Valida o campo name, que verifica se o nome contém apenas letras
    @field_validator("f_name", "f_second_name")
    def check_name_is_alpha(n):
        if not n.isalpha():
            raise ValueError(f"{n} não é um nome válido!")
        return n.title()

    @field_validator("age")
    def check_age_is_positive(n):
        if n < 1 or n > 100:
            raise ValueError(f"Idade errada!!!... {n}")
        return n

jhon = Person(f_name="jhon", f_second_name="doe", age=30)
print(jhon)