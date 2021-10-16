#Design Pattern Strategy

from impostos import ICMS, ISS, Ipreville


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':

    from orcamento import Orcamento

    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)
    #Duck Tipping, não importa qual instancia eu passe como parametro pra imposto, contando que tenha o metodo calcula
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, Ipreville())
