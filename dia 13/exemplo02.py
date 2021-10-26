#valor = 1
#
#match valor:
#    case 1 | 2 :
#        print(f'É {valor}')
#

lista = [1,'2',3]

match lista:
    case [] | [_]:
        print('Um ou nenhum elemento')

    case [1|'2', _,_] | [_, 1|2, _]: # Funciona com qualquer seja INT, STR,FLOAT ou que preferir
        print('Inicia com 1 ou 2')
    
#cor = (255,255,255)
cor1 = (255,255,255,255)
match cor1:
    # Nomenclatura para as variáveis
    case [r,g,b]:
        print(f'{r=},{g=},{b=}') #cor
    case r,g,b,a:
        print(f'{r=},{g=},{b=},{a=}') #cor1