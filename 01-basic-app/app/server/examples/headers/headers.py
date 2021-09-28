from typing import  Optional, List
from fastapi import FastAPI, Header


app = FastAPI()


# verificar el error aquí
# {
#     "User-Agent": "PostmanRuntime/7.28.4" Puedeser una variable reserbaba de
# }
# @app.get('/items/headers/') 
# async def read_items( user_agent: Optional[str] = Header(None) ):

#     return {"User-Agent": user_agent}


@app.get('/items/headers/')
async def read_items(x_token: Optional[List[str]] = Header(None)): # multiples headers con el mismo encabezado
# async def read_items( x_token: Optional[str] = Header(None) ):

    return {"X-oken": x_token}

# Si por alguna razón necesita deshabilitar la conversión automática de guiones bajos a guiones, configure el parámetro convert_underscoresde Headeren False:
