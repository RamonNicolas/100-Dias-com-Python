
def chato_das_cores(cor:int) -> int:    
    match cor:
        case r,g,b:
            return 'Cade o Alpha'
        case r,g,b,a if a == 255: # Uma validação a mais, denominada de Guards
            return 'Tudo transparente? Ta maluco'
        case r,g,b,a if r == 255:
            return 'Muito vermelho'
        case r,g,b,a if g == 255:
            return 'Tu é palmeirense ?'
        case r,g,b,a if b == 255:
            return 'Ta afim de ver o mar'
        case r,g,b,a:
            return 'Acertou mizeravi'

print(chato_das_cores(220,220,20,5))