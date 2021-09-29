# from fastapi import FastAPI, HTTPException, Request
# from fastapi.responses import JSONResponse

from fastapi import FastAPI, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
) #Controladores predeterminado de FastAPI

# Puede agregar un controlador de excepciones personalizado con @app.exception_handler():
class UnicornException(Exception): #clase de expetiones de forma global
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

items = {"foo": "The Foo Wrestlers"}


# Al generar un HTTPException, puede pasar cualquier valor que se pueda convertir a JSON como parámetro detail, no solo str.
# Podrías pasar a dict, a list, etc.
# FastAPI los maneja automáticamente y los convierte a JSON.

@app.get("/details/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail={ 'ok': False, 'msg':'Ocurrio un error' }, headers={'x-toke':'No se proveyó un token válido'} )
    return {"item": items[item_id]}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detalles": exc.errors(), "request-body": exc.body}),
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/http/request/items/")
async def create_item(item: Item):
    return item


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc) #Reutilizando los métodos definidos de FASTAPI


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc) #Reutilizando los métodos definidos de FASTAPI


@app.get("/httpException/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}