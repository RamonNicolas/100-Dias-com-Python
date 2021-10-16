from fastapi import APIRouter
from typing import Optional,List
from starlette.types import Send
from models import ModeloDoItem,ModeloDoItemResposta
from data import AFazer, OpcoesDeStatus

a_fazer = AFazer()
router = APIRouter()


@router.get('/', response_model=List[ModeloDoItemResposta])
def lista_a_fazer (status: Optional[OpcoesDeStatus] = None):
    """
    View que insere items na lista a fazer
    """
    if status is not None:
        return a_fazer.filter(status=status)
    return a_fazer.listar()


@router.post('/', response_model=ModeloDoItemResposta, status_code=201,)
def inserir_a_fazer (item_a_inserir: ModeloDoItem):
    """
    View que insere items na lista a fazer
    """
    return a_fazer.inserir(item_a_inserir.dict())

@router.get('/{id_do_item}', response_model=ModeloDoItemResposta)
def pegar_item_a_fazer (id_do_item: int):
    """
    View que mostra um item a partir do id
    """
    return a_fazer.pegar_item(id_do_item)