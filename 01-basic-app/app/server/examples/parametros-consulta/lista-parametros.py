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