from typing import Annotated
from pydantic import BaseModel, AfterValidator

"""
O Pydantic consegue ler metadados embutidos em tipos do Python via 
Annotated.

O AfterValidator intercepta o dado logo após a validação de tipo
padrão e executa sua lógica customizada (como barrar nomes muito 
curtos ou muito longos).

Se a validação falhar, o Pydantic interrompe o fluxo e gera um 
ValueError padronizado, mantendo a aplicação segura contra dados 
indesejados.
"""

def Check_name(name:str) -> str:
    if len(name) < 1 or len(name) >10:
        raise ValueError("O tamanho n está correto")
    return name

FirstName = Annotated[str, AfterValidator(Check_name)]

class Person(BaseModel):
    name: FirstName

a = Person(name="")
print(a)