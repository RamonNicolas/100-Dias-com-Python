from pytest import fixture


@fixture
def tarefas():
    return[
    ('Estudar', 'Feito'),
    ('Dormir', 'Feito'),
    ('Comer', 'A fazer')
    ]
print(tarefas)
