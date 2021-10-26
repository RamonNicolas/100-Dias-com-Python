valor = 1

match valor:
    case 1:
        print('O valor é 1')
    case 2: 
        print('O valor é 2')
    case _:
        print('Não é 1 nem 2 ')
        
lista = [1,2,3]
match lista:
    case [1,2,3]:
        print('Lista') 
    case [1,_,_]: # O primeiro item tem que ser 1 o resto não me importa, se tiver 3 valores e o 1 for 1
        print("1 é o primeiro")
    case [_,2,_]: # O segundo item tem que ser 2 o resto não me importa, se tiver 3 valores, não me importa o 1 nem o 3
        print("1 é o primeiro")

match lista:
    case [] | [_]:
        print('Um ou nenhum elemento')

    case [1,2]:
        print(lista = [1,2])

    case [1,*resto]: # Pega o primeiro se for 1 e depois toda a sequencia
        print(f'O primeiro é 1 e o {resto}')

