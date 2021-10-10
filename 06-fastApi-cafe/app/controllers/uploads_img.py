

import cloudinary
import uuid
from fastapi import File, UploadFile
from dotenv import dotenv_values
from cloudinary.uploader import upload, destroy
from bson import ObjectId

from db.config import db

config = dotenv_values()

cloud_name = config.get('CLOUD_NAME')
api_key = config.get('API_KEY') 
api_secret = config.get('API_SECRET') 

cloudinary.config(
    cloud_name = cloud_name, 
    api_key = api_key, 
    api_secret = api_secret,
    secure = True 
)

class Img(object): 
    
    def __init__(self):
        self.coleccion_usuario = db.coleccion_usuarios
        self.coleccion_producto = db.coleccion_productos

    def get_img(self, id:str):
        return {
            'img':'Se envío la img'
        }
    
    def update_img(self, coleccion: str, id: str):
        return {
            'img':'Se actualizó la img'
        }

    def subir_img(self, coleccion: str, id: str, file: UploadFile, public_id: str ):
       
        return upload(
            file.file,
            public_id = public_id,
            folder = f"{coleccion}/{id}/", 
            tags=id
        )
        
    
       
    def post_img(self, coleccion: str, id: str, file: UploadFile):
        
        if coleccion == 'usuario':
            usuario = self.coleccion_usuario.find_one({'_id':ObjectId(id)})
            
            if usuario['img']:
                destroy(usuario['img'].split('/')[-1])
                            
            obj=self.subir_img(coleccion, id, file, public_id='img-perfil')
            nombre = obj['secure_url']
    
            self.coleccion_usuario.find_one_and_update({'_id':ObjectId(id)}, {'$set':{'img':nombre}})
            
        elif coleccion == 'producto':
            
            producto = self.coleccion_producto.find_one({'_id':ObjectId(id)})
            
            if producto['img']:
                destroy(producto['img'].split('/')[-1]) 
                            
            obj=self.subir_img(coleccion, id, file,public_id='img-producto')
            nombre = obj['secure_url']
    
            self.coleccion_producto.find_one_and_update({'_id':ObjectId(id)}, {'$set':{'img':nombre}})
            
            

        return {
            'img':'Se creó una img'
        }
        
    