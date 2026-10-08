#Pydantic e YAML

import yaml
from pydantic import BaseModel, field_validator, model_validator

class UserDetails(BaseModel):
    name: str
    role: str

class ReleaseDetails(BaseModel):
    version: str
    deployed_to_production: bool

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

print(contents)
app = App(**contents["app"])
print("\n\n",app)
