from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

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

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail={ 'ok': False, 'msg':'Ocurrio un error' }, headers={'x-toke':'No se proveyó un token válido'} )
    return {"item": items[item_id]}
