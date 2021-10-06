from bson.objectid import ObjectId
from fastapi import Body, HTTPException
from passlib.hash import bcrypt

from models import usuario
from db.config import db


""" 
Dependencias:
    el id tiene que existir en la base de datos
    y el rol tiene que ser admin para poder hacert put post y delete = PENDIENTE
    contraseña tiene que tener un cierto rango => AGREGADO EN LOS MODELOS
    el correo tiene que ser un correo email válido => AGREGADO EN LOS MODELOS
    jwt válido también en el delete = PENDIENTE
"""


class Usuarios(object):

    def __init__(self):
        self.coleccion = db.coleccion_usuarios

    def post_usuario(self, body: usuario.Usuario_In ):
        
        body_dict = body.dict()
        password = body_dict['password']
        pass_hash = bcrypt.hash(password)
        body_dict.update({'password': pass_hash})

        id = self.coleccion.insert_one(body_dict).inserted_id
        resp = self.coleccion.find_one({'_id':ObjectId(id)})

        return resp
    
    def get_usuarios(self, limit:int, skip:int) :
        usuarios = [usuario for usuario in self.coleccion.find({}, limit=limit, skip=skip) if usuario['estado'] == True]
     
        return usuarios

    def get_usuario(self, id: str) :
        usuario = self.coleccion.find_one({'_id': ObjectId(id)})
        if usuario['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg':'El usuario no existe'
            })
        return usuario

    def update_usuario(self,id: str, body: Body):

        if type(body) is not dict:
            raise HTTPException(status_code=400, detail={
                'msg':'El cuerpo del body no es un objeto o diccinario'
            })
        
        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':body})
        usuario = self.coleccion.find_one({'_id': ObjectId(id)})
        return usuario

    def delete_usuario(self, id: str):

        # usuario = self.coleccion.find_one_and_delete({'_id': ObjectId(id)})
        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':{'estado':False}})
        usuario = self.coleccion.find_one({'_id': ObjectId(id)})

        return usuario


