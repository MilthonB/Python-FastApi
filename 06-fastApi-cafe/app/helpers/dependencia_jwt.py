from jose import jwt, exceptions
from fastapi import Header, HTTPException
import time 

SECRET_KEY = "2489392ab42c85b49f7e0674c703f2c3699e2bee5691329347aba2d7ac697d16"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def jwt_encode(id:str):

    # Una hora de duracion para expirar tiene este token 
    data = {
        'id': id,
        'exp': int(time.time())+3600
    }

    try:
        token = jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
        return token
    except exceptions.ExpiredSignatureError: #agregar exception para cada caso que pueda generar el token
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': 'Toke a caducado'
        })
    except exceptions.JWTError:
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': 'Toke no coincide'
        })
        
        
def jwt_decode( x_token: str = Header(..., convert_underscores=False) ):
    
    try:
        token_verify = jwt.decode(x_token,SECRET_KEY,algorithms=['HS256'])
    except exceptions.JWTError:  #agregar exception para cada caso que pueda generar el token
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': 'Toke inválido'
        })