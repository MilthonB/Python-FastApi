from typing import Optional, Set


from fastapi import FastAPI, status

from pydantic import BaseModel

app = FastAPI()


# https://fastapi.tiangolo.com/es/tutorial/path-operation-configuration/

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []



@app.post("/status/items/", response_model=Item, status_code=status.HTTP_201_CREATED)

async def create_item(item: Item):
    return item



@app.post("/i/items/", response_model=Item, tags=["items"])# tag sivern para dar el nombre de la operacion en la documentacion de la api
async def create_item(item: Item):
    return item


@app.get("/it/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/u/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


@app.post(
    "/items/",
    response_model=Item,
    summary="Create an itemess",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
) # más informacion a la documentacion de la api 
async def create_item(item: Item):
    return item

@app.post("/summary/items/", response_model=Item, summary="Create an item") # otra forma de  describir la funcion
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
