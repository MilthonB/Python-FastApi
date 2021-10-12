from fastapi import HTTPException, Body
from passlib.hash import bcrypt

from bson import ObjectId

from google.auth.transport import requests
from google.oauth2 import id_token


from models.auth import Auth_In
from models.usuario import Usuario_In
from db.config import db 
from helpers.dependencia_jwt import jwt_encode

class Auth(object):
    
    async def login( self, body: Auth_In,response ):

        correo, password = body.dict().values() 
        usuario = db.coleccion_usuarios.find_one({'correo': correo})

        if not usuario:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': 'Correo / Contraseña incorrectas' 
            })

        elif usuario['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': 'Correo inactivo'
            })

        elif usuario:
            
            validacion = bcrypt.verify(password, usuario['password'])
            
            if validacion:
                
                token = jwt_encode(str(usuario['_id']))
                response.set_cookie(key="token", value=token)
                usuario.update({'token': token})
                return usuario
            
            else:
                raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': 'Correo / Contraseña incorrectas'
            })
    
    
    async def google(self, token):
        
        request = requests.Request()
        
        coleccion_usuario = db.coleccion_usuarios
        
        try:    
            decoded_token = id_token.verify_token(str(token['id_token']),request)
            
            img = decoded_token['picture']
            correo = decoded_token['email']
            nombre = decoded_token['name']
            
        except ValueError as msg:
            print(msg)
            
        
        usuario = coleccion_usuario.find_one({'correo':correo}) 
        if usuario :
            return usuario
        
        informacion = {
            'img': img,
            'correo': correo,
            'nombre': nombre,
            'google': True,
            'password':'123456'
        }
        
       
        document_enviar = Usuario_In(**informacion)
        
        id = coleccion_usuario.insert_one(document_enviar.dict()).inserted_id

        usuario_nuevo = coleccion_usuario.find_one({'_id'   : ObjectId(id)})
        
        return usuario_nuevo


