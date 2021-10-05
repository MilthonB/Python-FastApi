
from fastapi import Body, HTTPException
from bson import ObjectId

from models.categoria import Categorias_Base
from db.config import db




class Categorias(object):
    
    def __init__(self):
        self.coleccion = db.coleccion_categorias
    
    async def get_categorias(self, limit:int, skip:int):

        categorias = [categoria for categoria in self.coleccion.find({}, limit=limit, skip=skip) if categoria['estado'] == True]
        return categorias
    
    
    async def get_categoria(self, id:str):

        categoria = self.coleccion.find_one({'_id': ObjectId(id)})
        if categoria['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg':'La categoria no existe'
            })
            
        return categoria
    
    
    async def update_categoria(self, id: str, body: Body):
        if type(body) is not dict:
            raise HTTPException(status_code=400, detail={
                'msg':'El cuerpo del body no es un objeto o diccinario'
            })
        
        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':body})
        categoria = self.coleccion.find_one({'_id': ObjectId(id)})
        return categoria
    
    
    async def post_categoria(self, body: Categorias_Base):

        id = self.coleccion.insert_one(body.dict()).inserted_id
        resp = self.coleccion.find_one({'_id':ObjectId(id)})

        return resp
    
    
    async def delete_categoria(self,id:str):
        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':{'estado':False}})
        categoria = self.coleccion.find_one({'_id': ObjectId(id)})

        return categoria