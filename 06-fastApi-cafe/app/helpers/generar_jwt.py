from jose import jwt


SECRET_KEY = "2489392ab42c85b49f7e0674c703f2c3699e2bee5691329347aba2d7ac697d16"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def jwt_encode(id:str):
    
    data = {
        'id': id,
        'exp': 30
    }

    try:
        token = jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
        return token        
    except :
        raise

def jwt_decode():
    toke = jwt.va