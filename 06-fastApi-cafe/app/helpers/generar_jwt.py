from jose import jwt
import time 

SECRET_KEY = "2489392ab42c85b49f7e0674c703f2c3699e2bee5691329347aba2d7ac697d16"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def jwt_encode(id:str):

    # Una hora de duracion para expirar tiene este token 
    data = {
        'id': id,
        'exp': int(time)+3600
    }

    try:
        token = jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
        return token        
    except : #agregar exception para cada caso que pueda generar el token
        raise

def jwt_decode():
    pass