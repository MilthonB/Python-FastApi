from fastapi import Body

from models.producto import Productos_Base
from db.config import db


class Productos(object):
    
    def __init__(self):
        self.coleccion = db.coleccion_productos

    async def get_productos(self):
        ...
        
    async def get_producto(self, id: str):
        ...
        
    async def update_producto(self, id: str, body: Body):
        ...
        
    async def post_producto(self, body:Productos_Base ):
        ...
        
    async def delete_producto(self, id: str):
        ...
        