from threading import local
from fastapi import Body, HTTPException
from passlib.hash import bcrypt
from localStoragePy import localStoragePy
from starlette.responses import JSONResponse

from models.auth import Auth_In
from db.config import db 
from helpers.generar_jwt import jwt_encode

localStorage = localStoragePy('Api-cafe','storage-token')

class Auth(object):
    
    async def login( self, body: Auth_In,response ):

        correo, password = body.dict().values() 
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
            
            if validacion:
                token = jwt_encode(str(usuario['_id']))
                response.set_cookie(key="token", value=token)

                return usuario
            else:
                raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': 'Contraseña incorrecta'
            })
            

