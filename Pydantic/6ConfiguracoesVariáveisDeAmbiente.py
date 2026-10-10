#Pydantic com arquivos .env

#Tem que rodar para que as variaveis existam no ambiente: source export_vars.sh
#Tem que rodar pip install pydantic_settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME = str
    ENVIROMENT = str
    APP_VERSION = str

settings = Settings()
print(settings)