from fastapi import Body, HTTPException
from passlib.hash import bcrypt

from models.auth import Auth_In
from db.config import db 


class Auth(object):
    
    async def login( self, body: Auth_In ):

        correo = body.dict()['correo']
        password = body.dict()['password']
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

        elif usuario:
            validacion = bcrypt.verify(password, usuario['password'])
            print(validacion)
            if validacion:
                return usuario
            else:
                raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': 'Contraseña incorrecta'
            })
            

