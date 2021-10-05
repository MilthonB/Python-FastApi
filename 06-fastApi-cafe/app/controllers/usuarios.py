from bson.objectid import ObjectId
from fastapi.param_functions import Body
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
    
        id = self.coleccion.insert_one(body.dict()).inserted_id
        resp = self.coleccion.find_one({'_id':ObjectId(id)})

        return resp
    
    def get_usuarios(self, limit:int, skip:int) :
        usuarios = [x for x in self.coleccion.find({}, limit=limit, skip=skip)]
        return usuarios

    def get_usuario(self, id: str) :
        usuario = self.coleccion.find_one({'_id': ObjectId(id)})
        return usuario

    def update_usuario(self,id: str, body: Body):
        
        return{
            'msg':'Hola soy un método update'
        }

    def delete_usuario(self,id: str):
        return{
            'msg':'Hola soy un método delete'
        }


