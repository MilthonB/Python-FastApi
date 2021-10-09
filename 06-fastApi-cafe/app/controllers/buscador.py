

from fastapi import Body, HTTPException, Path
from bson import ObjectId

from models.categoria import Categorias_Base
from db.config import db


class Buscador(object):

    colecciones = [
        'usuarios',
        'categorias',
        'productos',
        'roles'
    ]    
    
    def __init__(self): # inicializar todas las colecciones porque se buscara en todas las colecciones
        self.coleccion_usuario = db.coleccion_usuarios
        self.coleccion_producto = db.coleccion_productos
        self.coleccion_categoria = db.coleccion_categorias
        self.coleccion_rol = db.coleccion_roles
    
    async def buscar_usuario(self, termino: str):...
    
    async def buscar_categoria(self, termino: str):...
    
    async def buscar_producto(self, termino: str): ...
    
    async def buscar_rol(self, termino: str): ...
    
    async def buscador(self, termino: str = Path(...), coleccion:str = Path(...)):
        
        if colecciones in coleccion:
            ... 
        