from pydantic import BaseModel

class Auth_In(BaseModel):
    correo:str
    password: str