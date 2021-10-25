from pydantic import BaseModel, validator

class Cadastro(BaseModel):
    email: str
    senha_1: str
    senha_2: str
    """Validator é um decorador e é necessário passar o campo que precisa de validação"""

    @validator('email')
    def email_deve_ter_arroba(cls, v):
        """cls é instancia da classe não do objeto"""
        """v e o valor passado no load"""
        if '@' not in v:
            raise ValueError ('Não tem @ no email')
        return v

    @validator('senha_1','senha_2')
    def senha_tem_10_chars(cls,v):
        if len(v)>=10:
            return v
        else:
            raise ValueError('Senha não tem 10 caracteres')

    @validator('senha_2')
    def valida_senha(cls,v, values):
        if v == values['senha_1']:
            return v
        else:
            raise ValueError('Senhas diferentes')

Cadastro(**{'email': 'arapodkaspokd123@gmail.com', 'senha_1': 'testeteste1','senha_2': 'testeteste1'}).json()
print(Cadastro)