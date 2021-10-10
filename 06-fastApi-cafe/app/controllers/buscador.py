
import re
from fastapi import Body, HTTPException, Path
from bson import ObjectId

from models.categoria import Categorias_Base
from db.config import db


class Buscador(object):

    def __init__(self):  # inicializar todas las colecciones porque se buscara en todas las colecciones
        self.coleccion_usuario = db.coleccion_usuarios
        self.coleccion_producto = db.coleccion_productos
        self.coleccion_categoria = db.coleccion_categorias
        self.coleccion_rol = db.coleccion_roles
        self.colecciones = [
            'usuarios',
            'categorias',
            'productos',
            'roles'
        ]

    async def buscar_usuario(self, termino: str):
        # se puede buscar por
        
        # id
        if ObjectId.is_valid(termino):
            usuario = self.coleccion_usuario.find_one({'_id': termino})
            return usuario
        
        # nombre
        # Busqueda insensible
        regex_termino = re.compile(termino, re.I)
        usuario = self.coleccion_usuario.find_one({
            '$or':[{'nombre': { '$regex': regex_termino}}, {'correo': { '$regex': regex_termino}}],
            '$and':[{'estado':True}]
        })
        
        if usuario == None:
            return {
                'ok': False,
                'msg': 'No se encotro el usuario'
            }
        
        return usuario 
        
        # correo
        
    async def buscar_categoria(self, termino: str): 
        # se puede buscar por 
        # id 
        # nombre
        ... 

    async def buscar_producto(self, termino: str):
        # se puede buscar por 
        # id 
        # nombre
        ...

    async def buscar_rol(self, termino: str): 
        #  se puede buscar por 
        # id
        # nombre 
        ...

    async def buscador(self, termino: str = Path(...), coleccion: str = Path(...)):

        if coleccion not in self.colecciones:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'Coleccion incorrecta, tiene que se de tipo: {self.colecciones}'
            })

        if coleccion == 'usuarios':
            return await self.buscar_usuario(termino)
        elif coleccion == 'categorias':
            return await self.buscar_categoria(termino)
        elif coleccion == 'productos':
            return await self.buscar_producto(termino)
        elif coleccion == 'roles':
            return await self.buscar_rol(termino)
