from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100): # dependencia 
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")

async def read_items(commons: dict = Depends(common_parameters)): #funciones que tiene deppendencias para su funcionamiento

    return commons


@app.get("/users/")

async def read_users(commons: dict = Depends(common_parameters)): #funciones que tiene deppendencias para su funcionamiento

    return commons
