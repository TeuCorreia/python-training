#Pydantic Fields
"""
Fields adicionam informações e validações de regras extras para
o seu model Fields que as dicas de digitação regulares não conseguem
expressar
"""

#r'^\d{5}$' <- É uma sequência de caracteres que define
#um padrão de busca em textos 

from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(...,min_length=5, max_length=10)
    age : int = Field(default=10, ge=1, le=100)
    zipcode: str = Field(..., pattern=r'^\d{5}$')

person = Person(name="Ian Smith", age=11, zipcode="12345")
print(person)