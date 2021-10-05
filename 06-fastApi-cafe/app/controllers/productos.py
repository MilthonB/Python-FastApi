from fastapi import Body, HTTPException
from bson import ObjectId

from models.producto import Productos_Base
from db.config import db


class Productos(object):
    
    def __init__(self):
        self.coleccion = db.coleccion_productos

    async def get_productos(self, limit, skip):
        productos = [producto for producto in self.coleccion.find({}, limit=limit, skip=skip) if( producto['estado'] == True and producto['disponible'] == True)]
        return productos
        
    async def get_producto(self, id: str):
        producto = self.coleccion.find_one({'_id': ObjectId(id)})
        if producto['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg':'El producto no existe'
            })
        elif producto['disponible'] == False:
            raise HTTPException(status_code=200, detail={
                'ok': False,
                'msg':'El producto no esta disponible'
            })
            
        return producto
    
        
    async def update_producto(self, id: str, body: Body):
        if type(body) is not dict:
                raise HTTPException(status_code=400, detail={
                'msg':'El cuerpo del body no es un objeto o diccinario'
            })
        
        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':body})
        producto = self.coleccion.find_one({'_id': ObjectId(id)})
        return producto
        
    async def post_producto(self, body:Productos_Base ):
        id = self.coleccion.insert_one(body.dict()).inserted_id
        resp = self.coleccion.find_one({'_id':ObjectId(id)})

        return resp
        
    async def delete_producto(self, id: str):
        self.coleccion.find_one_and_update({'_id': ObjectId(id)}, {'$set':{'estado':False}})
        producto = self.coleccion.find_one({'_id': ObjectId(id)})

        return producto
        