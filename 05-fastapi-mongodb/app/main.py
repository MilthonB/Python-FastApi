
from typing import Optional, List
from bson.py3compat import b
from fastapi import FastAPI
from fastapi.param_functions import Body, Header, Query
from fastapi.params import Param
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
class PyObjectId(ObjectId):
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class DB(BaseModel): # Documento para pasar a la base de datos 
    nombre:str
    email: EmailStr
    activo: Optional[bool] = True 


class DB_out(DB): 
    id: Optional[PyObjectId] = Field(alias='_id')

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

@app.post('/post/{db_id}', response_model=DB_out)
async def insertar_data(q:int = Query(...), x_token: str = Header(...), body:DB = Body(..., embed=True)) -> List:
    collection = db.coleccion_alumnos #obtener la colleccion que se va a utilizar
    #insert document
    id = collection.insert_one(body.dict()).inserted_id #Insert en la coleccion y devuelve el id
    response = DB_out(_id = id, **body.dict())
    return response

@app.get('/get/{alumno_id}',response_model=DB_out)
async def obtener_data(alumno_id:str = Param(...)):
    alumnos = db.coleccion_alumnos.find_one({'_id': ObjectId(alumno_id)})
    return alumnos


@app.put('/put/{alumno_id}')
async def actualizar_data(alumno_id:str = Param(...)):
    
    ...

@app.delete('/delete/{alumno_id}', response_model=DB_out)
async def actualizar_data(alumno_id:str = Param(...)):
    antes_alumno = db.coleccion_alumnos.find_one({'_id':ObjectId(alumno_id)})
    print(type(antes_alumno))
    alumnos = db.coleccion_alumnos.delete_one({'_id':ObjectId(alumno_id)})
    return {
        **antes_alumno
    }
    