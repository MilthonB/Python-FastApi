from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from helpers.pyobjectId import PyObjectId


class Productos_Base(BaseModel):
    nombre: str
    categoria: PyObjectId
    estado: Optional[bool] = True
    usuario: PyObjectId
    precio: Optional[float] = 100.0
    disponible: Optional[bool] = True 


class Productos_Out(Productos_Base):
    id: Optional[PyObjectId] = Field(alias='_id')

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }