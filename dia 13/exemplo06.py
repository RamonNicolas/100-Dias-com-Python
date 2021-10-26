from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    funcionario: bool = False

def valor_cinema(pessoa: Pessoa, valor: int) -> str:
    match pessoa:
        case Pessoa('Ramon'):
            return f'Vai estudar Python'
        case Pessoa(nome,idade,False) if idade >= 65 :
            return f'Você {nome.capitalize()} paga meia {valor/2}'
        case Pessoa(nome,_,True):
            return f'Você é um funcionário com nome {nome.capitalize()}, e aqui funcionários pagam {valor/5}'

print(valor_cinema(Pessoa('Ramon',80), 20))
print(valor_cinema(Pessoa('José',35, True), 20))
