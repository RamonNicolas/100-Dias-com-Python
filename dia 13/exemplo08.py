class Pessoa:

    __match_args__ = ('nome','idade','funcionario')

    def __init__(self, nome, idade, funcionario=False) -> None:            
        self.nome: nome
        self.idade: idade
        self.funcionario= funcionario

def valor_cinema(pessoas: Pessoa, valor: int) -> str:
    match pessoa:
        case Pessoa('Ramon'|'Jarbas'):
            return f'Vai estudar Python'
        case Pessoa(nome,idade=idade,funcionario=False) if idade >= 65 :
            return f'Você {nome.capitalize()} paga meia {valor/2}'
        case Pessoa(nome,idade=_,funcionario=True):
            return f'Você é um funcionário com nome {nome.capitalize()}, e aqui funcionários pagam {valor/5}'
        case Pessoa(nome,idade=_,):
            return f'Seja bem vindo ao nosso cinema, {nome.capitalize()}, o valor do ingresso é {valor}'





print(valor_cinema(Pessoa('Ramon',80), 20))
print(valor_cinema(Pessoa('José',35, True), 20))
print(valor_cinema(Pessoa('Uriel',15), 20))
print(valor_cinema(Pessoa('Jarbas',80), 20))
#Observe a diferença do exemplo07 para o 08