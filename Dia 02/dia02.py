# Hoje vamos aprender Classes e funções
##

class Computador:
    # A classe deve ser dinâmica
    # __init__ é um construtor
    # Self serve para acessar as propriedades/e metodos de uma instancia
    def __init__(self, marca, memoria, gpu):
        # Definindo os parametros
        self.marca = marca
        self.memoria = memoria
        self.gpu = gpu

    # Ligar, Desligar , Exibir configurações
    # Criar metodos
    def ligar(self):
        print('estou ligando')

    def desligar(self):
        print('estou desligando')

    # todas as propriedades que são alocadas dentro do self, podem ser acessadas por outros metodos/que estão no escopo
    def exibir_info(self):
        print(self.marca, self.memoria, self.gpu)

# Instanciando a classe
#computador1 = Computador('Asus', '16gb', 'Nvidia')
# computador1.ligar()
# computador1.desligar()
# computador1.exibir_info()
#computador1 = Computador('Asus', '12gb', 'RTX')
# print(computador1.marca,computador1.memoria,computador1.gpu)


# Desafio
''' Criar uma class Carro e no minimo 3 propriedades do carro e no minimo 3 metodos'''


class Carro:
    #Propriedades
    def __init__(self, preco, combustivel, modelo, ano, lugares):
        self.preco = preco
        self.combustivel = combustivel
        self.modelo = modelo
        self.ano = ano
        self.lugares = lugares
        
    #Metodos
    def qnt_lugares(self):
        if self.lugares == 4:
            print(f"Esse carro {self.modelo} tem 4 lugares")
        if self.lugares > 4:
            print(f"Esse carro {self.modelo} é um SUV")
        else:
            print("É uma MOTO")

    def valor_carro(self):
        if self.preco > 35000 and self.preco < 85000:
            print(
                f"Esse carro {self.modelo} tem o valor de R${self.preco} esse carro está abaixo de R$85.000")
        else:
            print(f"Esse carro {self.modelo} tem o valor de R${self.preco}")

    def promocao(self):
        if self.preco <= 29000:
            print(
                f"Queima de Estoque esse carro {self.modelo} está em promo seu preço atual é de R${self.preco*1.00} está com 20% de desconto e seu valor é de R${self.preco*0.80}")
        if self.preco > 85000:
            sim = 'sim'
            nao = 'nao'
            avista = input(
                f"Você vai pagar o carro á vista ? digite {sim} ou {nao}, se for á vista o desconto é de 20 % \n ")
            if avista == 'sim':
                print(
                    f"Como o pagamento e avista, queima de Estoque esse carro {self.modelo} está em promo seu preço atual é de R${self.preco*1.00} está com 20% de desconto e seu valor é de R${self.preco*0.80}")
            else:
                print(
                    f"Modelo: {self.modelo} valor: R$ {self.preco*1.00}")

    def porta_malas(self):
        if self.modelo:
            self.lugares > 4
            print("Porta mala gigante")
        else:
            print("Porta Mala pequeno")

    def calota(self):
        print("calota")


jeep = Carro(95000, 'Diesel', 'Jeep Renegade', '2021', 7)

jeep.qnt_lugares()
jeep.promocao()


carro_budola = Carro(1500000,'Gasolina Premium', 'Audi R8', '2021',4)
fusca = Carro(25000, 'Gasolina', 'Fusca 1337', '1984', 5)
fusca.promocao()
fusca.porta_malas()
