from typing import List, Optional, Set,Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# Python tiene un tipo de datos especial para conjuntos de elementos únicos, el set. No alamcena valores duplicados
# Con esto, incluso si recibe una solicitud con datos duplicados, se convertirá en un conjunto de elementos únicos.


# Modelo que se utilizara como submodulo
# tipos exóticos de Pydantic HttUrl
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
    # image: Optional[Image] = None
    images: Optional[List[Image]] = None #Lista de imagenes


class Item2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # Especificar los tipos de cada elemento agrefafo a la lista
    tags: List[str] = []


# Modelos profundamente anidados
class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item1]

@app.post("/post/offers/")
async def create_offer(offer: Offer):
    return offer


class Image(BaseModel):
    url: HttpUrl
    name: str

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):# Tambien se puede declarar una anidacón desde los parametros 
    return images
# No podría obtener este tipo de soporte de editor si estuviera trabajando directamente con dictmodelos Pydantic en lugar de.
# los dictados entrantes se convierten automáticamente y su salida también se convierte automáticamente a JSON.


#En este caso, aceptaría cualquiera dictsiempre que tenga intclaves con floatvalores:
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]): # Si en la peticion se envia un str con el número entonces solo se parsea y se convierte a int 
    # si no mandas un número y en su lugar mandas una letra entonces marcara un erro de que el valor no es int
    print(weights)
    return weights

# Marca error
# {
#     "dsaf":1.25
# }

# Pasa y hace parsing al 1 string y lo vuele int
# {
#     "1":1.25
# }


@app.put("/anidados/items/{item_id}")
async def update_item(item_id: int, item: Item1):
    results = {"item_id": item_id, "item": item}
    return results


"""

{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}

"""
