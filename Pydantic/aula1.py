#Pydantic - Basics

from pydantic import BaseModel
from typing  import Optional, List

class User(BaseModel):
    name: str
    age: int
    passed_induction: bool
    #years_service: int = 0
    #years_service: Optional[int] = None
    years_service: int | float | str
    awards: List[str | int ]

user = User(name="Mateus", age=30, passed_induction=True, years_service=10, awards=["Employee of the Month", "Best Innovator", 5])
print(user)


"""
O Pydantic consegue converter valores setados como int para mas declarados como str, e vice-versa, desde que seja possível a conversão.
Por exemplo, se você definir um campo como int e passar uma string que representa um número, o Pydantic irá converter automaticamente para int.

O Pydantic também lê dicionários e listas, permitindo a criação de modelos complexos com facilidade.
Ex: user = {"name": "Mateus", "age": "30"}

O Optional é usado para indicar que um campo pode ser None, ou seja, não é obrigatório. 
Se você não fornecer um valor para esse campo, ele será definido como None por padrão.

"""