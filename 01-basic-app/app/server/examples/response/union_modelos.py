from typing import Union, List, Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int




items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

# Todo se define con el type que contenga el modelo y lo que tiene la respuesta 
# si el obj de respuesta tiene type car entonces carItem seria enviado de lo contrario... etc...
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem]) #enviara alguno de los dos modelos dependiendo de la informacion que se le otorge al response
async def read_item(item_id: str):
    return items[item_id]




class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=List[Item]) # para responder una lista
async def read_items():
    return items


@app.get("/keyword-weights/", response_model=Dict[str, str])
async def read_keyword_weights():
    return {"ok": False, "msg": 'Ocurrio un error'} # El falso lo convertira a string en la salida