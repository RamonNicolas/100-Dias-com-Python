'''
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(10);           # 10 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
'''


class Carro:

    def __init__(self):
        self.tanque = self.tanque()
        self.consumo_combustivel = self.consumo_combustivel()
        self.obterGasolina = self.obterGasolina()
        self.quer_abastecer = self.quer_abastecer()



    def tanque(self):
        self.tanque_carro = int(
            input('Gostaria de abastecer digite[1] , se ja tiver combustivel digite [2] : '))
        if self.tanque_carro == 1:
            self.tanque_carro -= 1
            self.tanque_carro = self.adicionarGasolina()
            print(
                f'Carro abastecido pronto pra viagem tem um total de {self.add_gas} litros')
        elif self.tanque_carro == 2:
            self.tanque_carro = int(
                input('Digite a quantidade disponivel de combustivel em: '))
            print(f'Bora pra viagem, temos {self.tanque_carro} litros')
        else:
            print('Valor errado, tente novamente')
            self.tanque()
            

    def consumo_combustivel(self):
        self.insere_km = int(
            input('Digite a quantidade de KM para fazermos a media de KM por Litro: '))
        if self.tanque_carro:
            self.media = self.insere_km/self.tanque_carro
            print(f'Seu consummo medio foi de {self.media}km/lt')
        else:
            self.media = self.insere_km/self.add_gas
            print(f'Seu consummo medio foi de {self.media}km/lt')

    def quer_abastecer(self):
        self.x = int(input('Quer abastecer, abastecer digite[1] \n caso contrario digite [0] para continuar \n'))
        if self.x == 1:
            self.adicionarGasolina()
        if self.x == 0:
            pass

    def adicionarGasolina(self):
        if self.tanque_carro == 2:
            self.add_gas = int(
                input('Digite a quantidade de combustivel pra abastecer: '))
            self.tanque_carro = self.add_gas + self.tanque_carro
            print(
                f'Essa e a quantidade de combustivel {self.add_gas} litro(s) para viagem')
        a = int(
            input('Voce quer abastecer \n [1] para sim \n [2] para nao \n '))
        if a == 1:
            self.add_gas = int(
                input('Digite a quantidade de combustivel pra abastecer: '))
            self.tanque_carro = self.add_gas
            print(
                f'Essa e a quantidade de combustivel {self.add_gas} litro(s) para viagem')
        if a == 2:
            x = int(input('Ja tem combustivel ou quer sair do programa \n [0] para sair do programa \n [1] para adicionar o combustivel ja existente no tank'))
            if x == 0:
                exit()
            if x == 1:
                self.tanque()

    def obterGasolina(self):
        ja_abasteceu = int(input('Voce ja abasteceu ? \n  [0] Se ja tinha combustivel no tank \n [1] pra sim \n'))
        if ja_abasteceu == 0:
            self.percorrer = int(input(
                        f'Sabemos que a Media e {self.media}km/lt, com isso quantos KM vc quer percorrer: '))
            resultado_final = self.tanque_carro - (self.percorrer/self.media) 
            print(
                    f'Depois dessa distancia percorrida temos essa quantidade de combustivel {resultado_final} litro(s) no tanque')
        if ja_abasteceu == 1:
            self.percorrer = int(input(
                        f'Sabemos que a Media e {self.media}km/lt, com isso quantos KM vc quer percorrer: '))
            resultado_final = self.add_gas - (self.percorrer/self.media) 
            print(
                    f'Depois dessa distancia percorrida temos essa quantidade de combustivel {resultado_final} litro(s) no tanque')
        else:
            print('Saindo do programa')

carrola = Carro()

