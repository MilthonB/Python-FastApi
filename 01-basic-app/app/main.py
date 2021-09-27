from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI()  # Objeto creado de fastapi que se ejecuta en uvicorn


# A+prender a manejar los estados de las respuesta de peticiones
# Mandar informacion por heades, querys, paramas,

# Se puede separar como modelos de peticiones Http
class Item(BaseModel):  # iterface de peticion de un put  elementos que debe de contener el put para pasar
    name: str
    price: float
    is_offer: Optional[bool] = None


# iterface de peticion de un put  elementos que debe de contener el put para pasar
class Ejemplo(BaseModel):
    uid: int
    nombre: str
    edad: int
    pais: str


class ModelName(str, Enum):  # Enum class modelo nombre, los parametros que entren tendra que pertencer o estar en la clase si no es así entonces mandara un error
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{
    "item_name": "Foo"
},
    {
        "item_name": "Bar"
},
    {
    "item_name": "Baz"
}]

#También puedes declarar tipos bool y serán convertidos:
#http://127.0.0.1:8000/items/foo?short=1
#http://127.0.0.1:8000/items/params?short=True
#http://127.0.0.1:8000/items/params?short=true
#http://127.0.0.1:8000/items/params?short=on
#http://127.0.0.1:8000/items/params?short=yes
# o cualquier otra variación (mayúsculas, primera letra en mayúscula, etc.) tu función verá el parámetro short con un valor bool de True. Si no, lo verá como False.


@app.get("/items/params/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items/")
async def read_items(skip:int=0,limit:int=10):#parametros por defecto en
    print(fake_items_db[skip: skip + limit])
    return{
        "msg": "ok",
        "fake_items_db":fake_items_db[skip: skip +limit]
    }

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):#parametros opcionales
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/users/me")
def read_root():
    return {"msg": "root"}


@app.get("/users/{id}")
def read_rootes(id: int, req: Ejemplo):
    return {
        "msg": "rootes",
        "id": id,
        "req": req
    }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.price, "item_id": item_id}
