from bson import ObjectId
from pydantic import BaseModel, EmailStr, SecretStr, Field
from typing import Optional
from helpers.pyobjectId import PyObjectId

class Categorias_Base(BaseModel):
    nombre: str
    estado: Optional[bool] = True
    usuario: PyObjectId 



class Categorias_Out(Categorias_Base):
    id: Optional[PyObjectId] = Field(alias='_id')

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


