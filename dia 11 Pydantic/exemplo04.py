from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime

class Myclass(BaseModel):
    """LE = Less equal, GT = greater than """
    #numero: int = Field(1, le=10, gt=0)
    """Se for uma lista, retorna uma lista, mas se tiver mais de 3 items você quebra em várias listas"""
    #lista: list[int] = Field([], max_items=3)
    """Foi necessário o ..., para que o valor seja requerido"""
    #valor_do_pedido: Decimal = Field(...,gt=1.0)

    criado_em: datetime = Field(default_factory=datetime.now)

print(Myclass())