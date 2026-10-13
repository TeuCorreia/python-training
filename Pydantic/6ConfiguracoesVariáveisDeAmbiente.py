#Pydantic com arquivos .env

#Tem que rodar pip install pydantic_settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    enviroment: str
    app_version: str

    class Config:
        env_file = ".env"

settings = Settings()
print(settings)