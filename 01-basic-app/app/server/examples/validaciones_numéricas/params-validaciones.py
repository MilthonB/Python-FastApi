from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


# Como el Query el Path tambien tiene que ser importado desde fastapi para poder usarlo
# Path(..., title) los tres punto lo vuelve un parametro obligatorio, pero no importa si tiene un None ya que para ingresar a esa ruta necesesita si o si el item_id
# También se pueden declarar más metadatos así como en el query

#El asterisco indica que la unicamanera de asignar valor a los parametrso de la funcion read_items es mandado la llave y el valor ejemplo:
#obj = {'item_id':5,'q':'Holamnundo'}
# read_items(**obj)
@app.get("/items/validaciones/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str # esta es otra opción para que no muestre el error de q:str y enton hace que los valores
    # se llamen con la palabra clave kwargs  
    # q: str,
    # item_id: int = Path(..., title="The ID of the item to get"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

#mayor que o igual validaciones
#ge = greater than or equal
@app.get("/items/mayorque{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


#mayor que 
#Menor o igual 
@app.get("/items/mayor/menor{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

#Validadores a float
# gt: greater than
# lt: less than
@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Si la estructura de tu peticion se encuentra así python se quejara
# Tiene que tener un valor declarado antes del path el q
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(..., title="The ID of the item to get"),
#     q: str,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
