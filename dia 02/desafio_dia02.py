'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''


class bombaCombustivel():

    def __init__(self):
        self.valor_litro = self.valor_litro()
        self.alterarValor = self.alterarValor()
        self.valida_combustivel = self.valida_combustivel()
        self.quantidade_combustivel = self.quantidade_combustivel()
        self.select_abastecimento = self.select_abastecimento()


    def select_abastecimento(self):
        seleciona = int(input('Deseja abastecer definir a quantidade de combustivel se for por Valor digite [1] ou se for por Litro digite [2] ? '))
        if seleciona == 1:
            self.abastecerPorValor()
        elif seleciona == 2:
            self.abastecerPorLitro()
        else:
            print('Tipo digitado nao existe')



    def valor_litro(self):
        self.valorLitro = (float(input('Digite o valor do litro em : R$   ')))


    def valida_combustivel(self):
        self.tipoCombustivel = (input(
            'Digite o tipo do combustivel G (Gasolina) | D (Diesel) | E (Etanol):  ').lower())
        combustivel = self.tipoCombustivel
        for x in combustivel:
            if x == 'g' or x == 'd' or x == 'e':
                pass
            else:
                print('Digite um tipo de combustivel correto')


    def quantidade_combustivel(self):
        self.quantidadeCombustivel = int(
            input('Digite aqui a quantidade de combustivel disponivel na bomba: '))


    def abastecerPorValor(self):
        valida_combustivel = self.tipoCombustivel
        qnt_litro = self.quantidadeCombustivel
        self.abastecendoValor = (
            float(input('Digite quantos reais voce quer abastecer : R$   ')))
        print(
            f"Valor a ser abastecido em R${self.abastecendoValor}, valor do preco do litro R${self.valorLitro}, tipo do combustivel {valida_combustivel}")
        abastecendoValor = self.abastecendoValor / self.valorLitro
        if abastecendoValor > self.quantidadeCombustivel:
            print(f'O valor digitado e maior que a quantidade de combustivel disponivel, quantidade disponivel {self.quantidadeCombustivel}')
            exit()
        else:
            print(
            f"Isso gerou essa quantidade {abastecendoValor}Litro(s) em combustivel, restando um total de {qnt_litro - abastecendoValor} de combustivel na bomba")
            10

    def abastecerPorLitro(self):
        abastecimentoPorLitro = int(
            input('Digite aqui a quantidade de litros que quer abastecer: '))
        if abastecimentoPorLitro > self.quantidadeCombustivel:
            print(f'O valor digitado e maior que a quantidade de combustivel disponivel, quantidade disponivel {self.quantidadeCombustivel}')
            exit()
        else:
            valor = self.valorLitro
            qnt_litro = self.quantidadeCombustivel
            print(
                f"O valor do litro e {valor}, voce abasteceu {abastecimentoPorLitro}litros, isso custou R${valor*abastecimentoPorLitro} e restou {qnt_litro-abastecimentoPorLitro} de combustivel na bomba")

    def alterarValor(self):
        novo = int(input(
            f'Voce quer alterar o valor do litro ? \n digite [ 1 ] para alterar o valor \n e [ 2 ] para Nao alterar o valor \n o valor atual e R$ {self.valorLitro} \n '))
        if novo == 1:
            novo_valor = (float(input('Digite o valor do litro em R$   ')))
            self.valorLitro = novo_valor
            print(f"O valor do combustivel agora e R${self.valorLitro}")

        elif novo == 2:
            print(f'valor atual e R${self.valorLitro}\n')
            self.valorLitro=self.valorLitro
        else:
            exit()

posto = bombaCombustivel()
