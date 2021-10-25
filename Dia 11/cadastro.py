from pydantic import BaseModel,EmailStr


class Cadastro(BaseModel):
    nome: str
    idade: int
    sobrenome: str
    """Precisa install o , pip install email-validator"""
    email: EmailStr 
    senha: str
    ativo: bool = True