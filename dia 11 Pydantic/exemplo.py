from pydantic import BaseModel


class Pessoa(BaseModel):
    nome: str
    idade: int
    sobrenome: str


class Pessoas(BaseModel):
    pessoas: list[Pessoa]


class Festa(BaseModel):
    maiores: Pessoas

"""
exemplo
d = {'maiores': 
    {'pessoas': [
        {'nome': 'Ramon', 'idade': '20'},
        {'nome': 'Nicolas', 'idade': '21'}    
    ]
    }
}
"""
