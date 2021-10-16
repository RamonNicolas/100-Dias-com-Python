from fastapi import FastAPI 
from a_fazer import router as a_fazer_router


app = FastAPI()

@app.get('/')
def hello_world ():
    """
    Root View, returns jsn {"hello": "world"}
    """
    return {"hello": "world"} 


app.include_router(a_fazer_router, prefix='/a-fazer', tags= ['todo'])