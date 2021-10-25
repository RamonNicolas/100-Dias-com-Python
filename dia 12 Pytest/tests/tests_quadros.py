
from app import  Coluna, Tarefa

def test_existe_um_quadro(quadro):
    quantidade_colunas = len(quadro.colunas)
    assert quantidade_colunas == 0 #assert

def test_quando_inserir_uma_coluna_deve_existir_uma_coluna(quadro):
    quadro.inserir_coluna(Coluna(nome='A fazer'))
    assert len(quadro.colunas) == 1

def test_quando_inserir_fazendo_deve_estar_no_quadro(quadro):
    quadro.inserir_coluna(Coluna(nome='Fazendo'))
    assert quadro.colunas[0].nome == 'Fazendo'

def test_quando_inserir_uma_tarefa_ela_deve_estar_na_primeira_coluna(quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 1

def test_quando_inserir_duas_tarefa_ela_deve_estar_na_primeira_coluna(quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Comer'))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 2

def test_quando_mover_cartao_coluna_next(quadro_com_colunas):
     tarefa = Tarefa ('Usar mascara!')
     quadro_com_colunas.inserir_tarefa(tarefa)
     quadro_com_colunas.mover(tarefa)
     assert tarefa not in quadro_com_colunas.colunas[0]

def test_quando_mover_cartao_coluna_remover_anterior(quadro_com_colunas):
     tarefa = Tarefa ('Usar mascara!')
     quadro_com_colunas.inserir_tarefa(tarefa)
     quadro_com_colunas.mover(tarefa)
     assert tarefa not in quadro_com_colunas.colunas[0]

from pytest import mark
@mark.exemplo

def test_exemplo(factory_boy_test):
    ...
#@mark.parametrize('quadro_parametrizado',[[1]],indirect=True)
#
#def test_passando_parametros(quadro_parametrizado):
#    ...
# Não é recomendado pela legibilidade