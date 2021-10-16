from pydantic import BaseModel
from typing import Optional
from data import OpcoesDeStatus


class ModeloDoItem(BaseModel):

    titulo: str
    descricao: Optional[str]
    status: Optional[OpcoesDeStatus]

class ModeloDoItemResposta(ModeloDoItem):
    id: int