#Pydantic e YAML

import yaml
from pydantic import BaseModel, field_validator, model_validator

class InvalidProdRelease(Exception):
    #Gerado quando uma versão inválida é detectada
    pass

class UserDetails(BaseModel):
    name: str
    role: str

class ReleaseDetails(BaseModel):
    version: str
    deployed_to_production: bool

    @model_validator(mode="after")
    def check_for_valid_release(cls, values):
        for i in {"a", "b", "c"}:
            if i in values.version and values.deployed_to_production:
                raise InvalidProdRelease("Production release not allowed!")
        return values

class App(BaseModel):
    name: str
    version: float
    user_details: UserDetails
    release_details:ReleaseDetails

    @field_validator("name")
    def check_name(name):
        if not name.isalpha():
            return name
        raise ValueError("O nome está incorreto!")


with open("my_config.yaml") as file:
    contents = yaml.safe_load(file.read())

print(contents, "\n\n")
app = App(**contents["app"])
print(app.release_details)
