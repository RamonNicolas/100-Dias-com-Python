class ISS(object):
    def calcula(self, orcamento):

        return orcamento.valor * 0.1

class ICMS(object):
    def calcula(self, orcamento):

        return orcamento.valor * 0.25

class Ipreville(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.55