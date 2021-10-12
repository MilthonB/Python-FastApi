from bson.objectid import ObjectId
from fastapi import Body, HTTPException
from passlib.hash import bcrypt
import pymongo

from models import usuario
from db.config import db


class Usuarios(object):

    def __init__(self):
        self.coleccion = db.coleccion_usuarios

    def post_usuario(self, body: usuario.Usuario_In ):
        body_dict = body.dict()
        
        try:
            password = body_dict['password']
            pass_hash = bcrypt.hash(password)
            body_dict.update({'password': pass_hash})

            id = self.coleccion.insert_one(body_dict).inserted_id
            resp = self.coleccion.find_one({'_id':ObjectId(id)})

            return resp

        except pymongo.errors.DuplicateKeyError:
            correo = body_dict['correo']
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'El correo: { correo } ya esta registrado'
            })

       
    
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

    async def update_usuario(self,id: str, body: usuario.Usuario_update):

        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':body.dict()})
        usuario = self.coleccion.find_one({'_id': ObjectId(id)})
        return usuario

    def delete_usuario(self, id: str):

        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':{'estado':False}})
        usuario = self.coleccion.find_one({'_id': ObjectId(id)})

        return usuario


