from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):#modelo de entrada
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel): # modelo de salida, se omite la contraseña
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# Parámetros de codificación del modelo de respuesta
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},#valores predeterminados no se incluirán en la respuesta
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2}, #valores predeterminados
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},#Datos con los mismos valores que los predeterminados
}


# También puede utilizar los parámetros del decorador de operaciones de rutaresponse_model_include y response_model_exclude.
# @app.get("/exclude/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# @app.get("/exclude/items/{item_id}", response_model=Item, response_model_include={"name", "description"},)
# @app.get("/exclude/items/{item_id}", response_model=Item, response_model_exclude={"tax"})  
@app.get("/exclude/items/{item_id}", response_model=Item, response_model_exclude=["tax"]) # Es un set por default pero si mandas un [] fastapi lo convertira a set  
async def read_item(item_id: str):
    return items[item_id]