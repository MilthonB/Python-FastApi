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

    def post_usuario(self, body: usuario.Usuario_In ):
        return{
            'msg':'Hola soy un método post'
        }
    
    def get_usuarios(self,) :
        return{
            'msg':'Hola soy un método get'
        }

    def get_usuario(self,) :
        return{
            'msg':'Hola soy un método get'
        }
    def update_usuario(self,id_usuario: int, body: Body):
        return{
            'msg':'Hola soy un método update'
        }

    def delete_usuario(self,id_usuario: int):
        return{
            'msg':'Hola soy un método delete'
        }


