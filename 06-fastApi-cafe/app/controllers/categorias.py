
from fastapi.param_functions import Body
from bson import ObjectId

from models.categoria import Categorias_Base
from db.config import db




class Categorias(object):
    
    def __init__(self):
        self.coleccion = db.coleccion_categorias
    
    async def get_categorias(self):
        ...
    
    
    async def get_categoria(self):
        ...
    
    
    async def update_categoria(self):
        ...
    
    
    async def post_categoria(self, id:str, body: Categorias_Base):

        id = self.coleccion.insert_one(body.dict()).inserted_id
        resp = self.coleccion.find_one({'_id':ObjectId(id)})

        return resp
    
    
    async def delete_categoria(self):
        ...