from typing import List,Optional,Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item1(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # tags: list = [] # No se define el tipo de los elementos
    tags: Set[str] = set()


class Item2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = [] #Especificar los tipos de cada elemento agrefafo a la lista


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results