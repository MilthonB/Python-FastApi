from typing import List, Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# Python tiene un tipo de datos especial para conjuntos de elementos únicos, el set. No alamcena valores duplicados
# Con esto, incluso si recibe una solicitud con datos duplicados, se convertirá en un conjunto de elementos únicos.


# Modelo que se utilizara como submodulo
class Image(BaseModel):
    # url: str
    url: HttpUrl
    name: str

# Se puede declarar "objetos" JSON profundamente anidados con nombres, tipos y validaciones de atributos específicos.
# Como image: Optional[Image] = None
class Item1(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # tags: list = [] # No se define el tipo de los elementos
    tags: Set[str] = set()
    image: Optional[Image] = None


class Item2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # Especificar los tipos de cada elemento agrefafo a la lista
    tags: List[str] = []


@app.put("/anidados/items/{item_id}")
async def update_item(item_id: int, item: Item1):
    results = {"item_id": item_id, "item": item}
    return results
