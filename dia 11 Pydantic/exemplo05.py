from pydantic import BaseSettings, Field, PostgresDsn

#class MinhaConfig1(BaseSettings):
#    """com o ENV pega o os valores da variáveis de ambiente"""
#    mongo_url: str = Field(..., env='mongo_url')
#    postgres: str = Field(..., env='postgres_url')

#print(MinhaConfig1()) 

class TestConfig(BaseSettings):
    """com o ENV pega o os valores da variáveis de ambiente"""
    #mongo_url: str
    """Valida URL do Postgres"""
    postgres: PostgresDsn 

    class Config:
        env_prefix = 'test_'
#Exemplo certo
print(TestConfig(postgres='postgres://user:pass@localhost:5432')) 
#Exemplo com erro
#print(TestConfig(postgres='postgres//user:pass@localhost:5432')) 