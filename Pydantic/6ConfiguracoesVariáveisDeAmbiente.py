#Pydantic com arquivos .env

#Tem que rodar pip install pydantic_settings

"""
O Pydantic Settings busca os valores seguindo uma hierarquia
estrita de prioridade.

1 - Argumentos passados diretamente na instanciação (Maior prioridade)
2 - Variáveis de ambiente do sistema operacional (Ex: exportadas
no terminal via shell script).
3 - Arquivo .env

Por que utilizar:
Essa flexibilidade permite que você tenha valores padrão locais
seguros para desenvolvimento (.env), mas que possam ser facilmente
sobrescritos em ambientes de produção (como no Docker ou Kubernetes)
injetando variáveis de ambiente diretamente no container,
sem precisar alterar código.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    enviroment: str
    app_version: str

    class Config:
        env_file = ".env"

settings = Settings()
print(settings)