from pydantic import BaseModel, validator

class Pedidos(BaseModel):
    ids: list[int]

    """Antes do pydantic iniciar a função, a validação ocorre, no caso se é uma lista de inteiros"""
    @validator('ids', pre=True)
    def convert_ids(cls,v):
        return v.split(',')
    
    @validator('ids', each_item=True)
    def integ_ids(cls,v):
        if v < 0:
            raise ValueError('Erro')
    
        return v
        
print(Pedidos(ids='1,2,3,4'))