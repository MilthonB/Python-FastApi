from pydantic import BaseModel, EmailStr, SecretStr, FilePath, Field
from typing import Optional

class Usuarios_Base(BaseModel):
    nombre: str
    correo: EmailStr
    img: str
    rol: str
    estado: Optional[bool] = True
    google: Optional[bool] = False

class Usuario_In(Usuarios_Base):
    password: SecretStr = Field(..., min_length=6)

class Usuario_Out(Usuarios_Base):
    ...