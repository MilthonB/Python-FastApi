from fastapi import Body, HTTPException

from models.auth import Auth_In
from db.config import db 


class Auth(object):
    
    async def login( body: Auth_In= Body(...)):
        correo = body.dict()['correo']
        usuario = db.coleccion_usuarios.find_one({'correo': correo})

        if not usuario:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': 'Correo no registrado'
            })

        elif usuario['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': 'Correo no inactivo'
            })

        return usuario
