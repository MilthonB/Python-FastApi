from typing import Optional

from fastapi import Cookie, FastAPI

app = FastAPI()

# Luego declare los parámetros de la cookie usando la misma estructura que con Pathy Query.

@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}