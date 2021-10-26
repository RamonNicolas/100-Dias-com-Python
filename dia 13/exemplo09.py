class Pessoa:

    __match_args__ = ('nome','idade','funcionario')

    def __init__(self, nome, idade, funcionario=False) -> None:            
        self.nome: nome
        self.idade: idade
        self.funcionario= funcionario

    def __repr__(self) -> str:
        return self.nome

def valor_cinema(pessoas:list[Pessoa]) -> str:
    match pessoas:
        case [
            Pessoa('Jarbas') as jarbas, 
            Pessoa('Eduardo', idade) as eduardo
            ]:
            return jarbas.idade, eduardo, idade

        case [Pessoa('Jarbas')  | Pessoa('Eduardo') as pessoa ]:
            return pessoa
        #case [Pessoa('Jarbas' | 'Eduardo') as pessoa ]: # Tambem funciona
        #    return pessoa

print(valor_cinema([Pessoa('Jarbas',18,True), Pessoa('Eduardo',19,True)]))
print(valor_cinema([Pessoa('Jarbas',18,True)]))
#Observe a diferença do exemplo07 para o 08