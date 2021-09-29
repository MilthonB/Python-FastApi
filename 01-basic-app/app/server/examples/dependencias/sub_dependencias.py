from typing import Optional

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()

# Aquí se genera un árbol de dependencias 
# la funcion del opereador tiene una dependencia con query_or_cookie_extractor
# y query_or_cookie_extractor tiene una dependencia con query_extractor

def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):

    return {"q_or_cookie": query_or_default}
