from typing import List, Optional

from fastapi import FastAPI, Query

app = FastAPI()



# Consultar lista de parámetros / valores múltiples
# puede declararlo Optional[List[str]] para recibir una lista de valores, o dicho de otra manera, para recibir múltiples valores.
# todos los querys que tenga en el path la letra q sera obtenidos como un arreglo, por ejemplo:
# http://localhost:8000/items/?q=foo&q=bar

"""Resultado:
    {
  "q": [
    "foo",
    "bar"
  ]
}
Si no se envia nada sera null
"""
@app.get("/items/")

async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

# Consultar lista de parámetros / valores múltiples con valores predeterminados
@app.get("/items/default")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items

"""
Respuesta
{
    "q": [
        "foo",
        "bar"
    ]
}
"""


# Tambien se puede definir simplemente list y sera tomado como lista
@app.get("/items/list")
async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items

#Agregar más metadatos
# Esta información solo se podra visualizar en OpenApi en el http://127.0.0.1:{port}/docs# revisar documentación 
@app.get("/items/metadatos")
async def read_items(
    q: Optional[str] = Query(None, title="MOSTRAR INFORMACIÓN", description="Query string for the items to search in the database that have a good match",min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Parámetros de alias
# Dentro de un query param los identificadores como item-query no son reconocidos por python por la separación del guion lo que python podría leer es sería item_query
# con un guion bajo, eso si lo podría entender python 
# Pero si aún así tienes una valor que no puede leer python como ese, entonces es donde entra el alias de la función Query()
#ejemplo: http://127.0.0.1:8000/items/?item-query=foobaritems

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Desactivación de parámetros
# Esto marcara como obsolote la query
# Pero solo sera visualizado en OpenApi
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
