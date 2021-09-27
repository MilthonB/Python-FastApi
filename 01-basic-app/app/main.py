from fastapi import FastAPI, Query
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

class Item_Body(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


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

# Parámetros de query requeridos
# Aquí el parámetro de query needy es un parámetro de query requerido, del tipo str.
# Por supuesto que también puedes definir algunos parámetros como requeridos, con un valor por defecto y otros completamente opcionales:
@app.get("/items/needy/{item_id}")
async def read_user_item(  item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy}
    return item # Este es mi respons


#Request body
#En su editor, dentro de su función, obtendrá sugerencias de tipo y finalización en todas partes (esto no sucedería si recibiera un dict en lugar de un modelo Pydantic):
#Request body + path parameters
#FastAPI reconocerá que los parámetros de la función que coinciden con los parámetros de la ruta deben tomarse de la ruta, y que los parámetros de la 
#función que se declaran como modelos Pydantic deben tomarse del cuerpo de la solicitud.

@app.put("/body/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}    

# Request body + path + query parameters
@app.put("/params/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

#Request body
#En su editor, dentro de su función, obtendrá sugerencias de tipo y finalización en todas partes (esto no sucedería si recibiera un dict en lugar de un modelo Pydantic):
@app.post("/post/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/")
async def read_items(skip:int=0,limit:int=10):#parametros por defecto en
    print(fake_items_db[skip: skip + limit])
    return{
        "msg": "ok",
        "fake_items_db":fake_items_db[skip: skip +limit]
    }


# Parámetros de consulta y validaciones de cadenas
#importar de fastApi el módulo Query
# estableciendo el parámetro max_lengthen 50, min_length=3, regex
#^: comienza con los siguientes caracteres, no tiene caracteres antes.
#fixedquery: tiene el valor exacto fixedquery.
#$: termina ahí, no tiene más caracteres después fixedquery.
#De la misma manera que puede pasar Nonecomo el primer argumento que se utilizará como valor predeterminado, puede pasar otros valores.

@app.get("/params/query/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
# async def read_items(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


from fastapi import FastAPI, Query

app = FastAPI()

# Operador ellipsis
#Se puede utilizar de algunas otras maneras, pero en este caso lo que hace es hacer obligatorio el query, Query (...,min_length=3)
# Esto le permitirá a FastAPI saber que este parámetro es obligatorio.
@app.get("/ellipsis/query/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results




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
