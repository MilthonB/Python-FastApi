
from typing import Optional, List
from fastapi import FastAPI
from fastapi.param_functions import Body, Header, Query
from pydantic import BaseModel, EmailStr
from bson import ObjectId
from pydantic.fields import Field

from dbmongo.config import Conexion



app = FastAPI(
    title='Api conexion a DB mongo atlas',
    description='Solo mostrar la conexion',
    # dependencies= [Depends(...)]
);

db = Conexion()

# Esto no se para que sirve aúns
# class PyObjectId(ObjectId):
    
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid objectid')
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type='string')




class DB(BaseModel): # Documento para pasar a la base de datos 
    id: int
    nombre:str
    email: EmailStr
    activo: Optional[bool] = True 

   



@app.post('/db/{db_id}', response_model=DB)
async def obtener_data(q:int = Query(...), x_token: str = Header(...), body:DB = Body(..., embed=True)) -> List:
    print('no hay error', body.dict())
   
    # if hasattr(body, 'id'):
    #     delattr(body, 'id')
   
    print(body)

    dictAux = {
        'nada':'nada'
    }

    collection = db.coleccion_alumnos# asi se crean colecciones
    # post = db.posts#coleccion
    #insert document
    id = collection.insert_one(dictAux).inserted_id #Insert en la coleccion y devuelve el id
    print(id) #Imprime el id
    # print (db.list_collection_names())
    return body #retorna el body recibivo

