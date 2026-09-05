#Pydantic - Class Validators

from pydantic import BaseModel, model_validator
from typing import Optional


class User(BaseModel):
    password: str
    confirm_password: str

    #after -> Valida o modelo após a criação do objeto
    #before -> Valida o modelo antes da criação do objeto
    @model_validator(mode="after")
    def password_check(self):
        if self.password != self.confirm_password:
            raise ValueError("Senhas não conferem!!!")
        else:
            print("Senhas conferem!!!")
        return self


# user = User(password="abc", confirm_password="abc")
# print(user)


class ItemShop(BaseModel):
    name: str
    needs_shipping: bool
    shipping_address: Optional[str] = ""

    @model_validator(mode="after")
    def item_check(self):
        print(vars(self))
        if self.needs_shipping and not self.shipping_address:
            raise ValueError(f"O item n tem endereço de entrega: {self.name}")
        return self
    

# item = ItemShop(name="Camiseta", needs_shipping=True, shipping_address="")


class File(BaseModel):
    pass

class ItemUpload(BaseModel):
    type_: str | File
    path: Optional[str] = None

    @model_validator(mode="after")
    def path_check(self):
        if isinstance(self.type_, File) and (self.path is None or not self.path):
            raise ValueError ("O item é do tipo File, mas não tem caminho de upload")
        return self


#x = ItemUpload(type_="File")
#x = ItemUpload(type_=File(), path="")