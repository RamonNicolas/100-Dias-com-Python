dicionario = {'a':25, 'c': 5}
match dicionario:
    case {'a': 1, 'b': 2}:
        print('Match Literal')
    case {'a':_,'b': 2}:
        print('Match na chave b')
    case {'a': chave_a,'b': _}:
        print(f'Match na chave {chave_a}')
    case {'a':_,'b': _}:
        print('Nenhum Match')
    case {'error': _}:
        print('Deu ruim nos Matchs')

    case {'a': _} | {'c': _}:
        print('Deu ruim nos Matchs')
