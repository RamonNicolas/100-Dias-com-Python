from pydantic import BaseSettings,BaseModel, Field
from typing import Literal, Union

class TestConfig(BaseSettings):
    env: Literal['test']
    xpto: str = 'Meu ambiente de test'
    database_url: str = Field(env='database_url')

class ProdConfig(BaseSettings):
    env: Literal['prod']
    dog: str = 'Meu ambiente de prod'

class DevConfig(BaseSettings):
    env: Literal['dev']
    shark: str = 'Meu ambiente de dev'

class Config(BaseModel):
    """A partir do momento que o Literal foi setado, quando é passado o nome da váriavel setada no Literal é possível apenas chamar o valor setado"""
    config: Union[DevConfig,TestConfig,ProdConfig]

print(Config(config={'env': 'dev'}))
print(Config(config={'env': 'test'}))
print(Config(config={'env': 'prod'}))