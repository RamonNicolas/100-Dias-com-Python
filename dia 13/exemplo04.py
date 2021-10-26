def movimento(comando:str) -> str:
    match comando.split():
        case ['pular']:
            return 'Pulando'
        case ['mover']:
            return 'Pra onde?'
        case 'mover', 'direita' | 'esquerda' as direção:
            return f'Movendo lateralmente para f{direção}'
        case 'mover', 'cima'|'baixo' as direção:
            return f'Movendo horizontalmente para {direção}'

print(movimento('mover esquerda'))
print(movimento('mover'))
print(movimento('pular'))