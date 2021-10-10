from enum import unique
from bson import ObjectId
from pydantic import BaseModel, EmailStr, SecretStr, Field
from typing import Optional
from helpers.pyobjectId import PyObjectId

class Usuarios_Base(BaseModel):
    nombre: str
    correo: EmailStr
    rol: Optional[str] = 'USER_ROLE'
    img: Optional[str] = None
    estado: Optional[bool] = True
    google: Optional[bool] = False

    

class Usuario_In(Usuarios_Base):
    password: str = Field(..., min_length=6)
    # password: SecretStr = Field(..., min_length=6)

class Usuario_Out(Usuarios_Base):
    id: Optional[PyObjectId] = Field(alias='_id')
    token: Optional[str] = 'Sin token'

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Usuario_update(BaseModel):
    nombre: str
    img: str