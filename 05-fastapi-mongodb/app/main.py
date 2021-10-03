
from typing import Optional, List
from fastapi import FastAPI
from fastapi.param_functions import Body, Header, Query
from pydantic import BaseModel, EmailStr
from bson import ObjectId

from dbmongo.config import client



app = FastAPI(
    title='Api conexion a DB mongo atlas',
    description='Solo mostrar la conexion',
    # dependencies= [Depends(...)]
);

class DB(BaseModel):
    id:str
    nombre:str
    email: EmailStr
    activo: Optional[bool] = True 


print(client)


@app.post('/db/{db_id}', response_model=DB)
async def obtener_data(q:int = Query(...), x_token: str = Header(...), body:DB = Body(..., embed=True)) -> List:
    print('no hay error', body.dict())
    db = client.test_database
    # coleccion = db['test-collection']
    # print(coleccion)
    post = db.posts
    id = post.insert_one(body.dict()).inserted_id
    print(id)
    return body

