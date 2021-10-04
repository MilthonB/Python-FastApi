from fastapi.param_functions import Body
from models import usuario


class Usuarios(object):

    def post_usuario(self, body: usuario.Usuario_In ):
        return{
            'msg':'Hola soy un método post'
        }
    
    def get_usuarios(self,) :
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


