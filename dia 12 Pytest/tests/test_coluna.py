from app import Coluna
from pytest import fixture

def teste_coluna_deve_ter_um_nome():
    assert Coluna('Fazendo').nome == 'Fazendo'