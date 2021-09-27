from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()  # Objeto creado de fastapi que se ejecuta en uvicorn


# A+prender a manejar los estados de las respuesta de peticiones
# Mandar informacion por heades, querys, paramas,

# Se puede separar como modelos de peticiones Http
class Item(BaseModel):  # iterface de peticion de un put  elementos que debe de contener el put para pasar
    name: str
    price: float
    is_offer: Optional[bool] = None

class Ejemplo(BaseModel):  # iterface de peticion de un put  elementos que debe de contener el put para pasar
    uid: int
    nombre: str
    edad: int
    pais: str

@app.get("/{id}")
def read_rootes(id:int, req: Ejemplo):
    return {
        "msg": "rootes",
        "id": id,
        "req":req
        }

@app.get("/")
def read_root():
    return {"msg": "root"}




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}
