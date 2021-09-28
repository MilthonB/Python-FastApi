from typing import Optional

from fastapi import FastAPI, Path,Body
from pydantic import BaseModel

app = FastAPI()


# creacion del modelo de la peticion put item
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Mix Path, Queryy parámetros corporales


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results



class User(BaseModel):
    username: str
    full_name: Optional[str] = None

#multiples parametrso de body: Item y User
@app.put("/user/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

"""
Respuesta
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}"""

# Query y Path son para definir datos adicionales   

#Valores sigulares en el body
@app.put("/body/singular/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: int = Body(...) # valor singular en el body 
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


"""
Respuesta
{
    "item_id": 456,
    "item": {
        "name": "Basura",
        "description": "Basua organica",
        "price": 250.85,
        "tax": 560.54
    },
    "user": {
        "username": "Milthon",
        "full_name": "Milthon B"
    },
    "importance": 45
}

"""