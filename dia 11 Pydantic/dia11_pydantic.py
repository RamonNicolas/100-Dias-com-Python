from pydantic import validate_arguments
from typing import Union
from pydantic.dataclasses import dataclass
from pydantic import StrictInt

@validate_arguments
def soma(x: int ,y: int) -> sum:
    return x+y

print(soma(2,2))


@dataclass
class Pessoa:
    nome: str
    idade: StrictInt

print(Pessoa(nome='ramon',idade=25))