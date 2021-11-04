
# Desafio
''' Criar uma class Loja e no minimo 3 propriedades da Loja e no minimo 3 metodos'''

class Loja:
    def __init__(self,produto,id,vendedor,caixa,valor_produto):
        self.produto = produto
        self.id = id
        self.vendedor= vendedor
        self.caixa = caixa
        self.valor_produto = valor_produto

    def valor_produtos(self):
        lista_produtos=[]
        lista_produtos.append(self.produto)
        print(f'Lista de produtos{lista_produtos}')
    
    def nome_vendedor(self):
        nome_vendedor=[]
        nome_vendedor.append(self.vendedor)
        print(nome_vendedor)

    def lucro_caixa(self):
        lucro = self.caixa - self.valor_produto
        print(f"O lucro do caixa {lucro}")

loja_xand = Loja('mac',420,'Xanx',15000,50)
loja_xand.lucro_caixa()
loja_xand.nome_vendedor()   
loja_xand.valor_produtos()
