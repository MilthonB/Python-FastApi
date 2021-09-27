from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


# Como el Query el Path tambien tiene que ser importado desde fastapi para poder usarlo
# Path(..., title) los tres punto lo vuelve un parametro obligatorio, pero no importa si tiene un None ya que para ingresar a esa ruta necesesita si o si el item_id
# También se pueden declarar más metadatos así como en el query 

@app.get("/items/{item_id}")
async def read_items(
    q: str,
    item_id: int = Path(..., title="The ID of the item to get"),
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
