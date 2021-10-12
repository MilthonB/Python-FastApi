

import cloudinary
import uuid
from fastapi import File, UploadFile, HTTPException
from dotenv import dotenv_values
from cloudinary.uploader import upload, destroy
from bson import ObjectId

from db.config import db

config = dotenv_values()

cloud_name = config.get('CLOUD_NAME')
api_key = config.get('API_KEY')
api_secret = config.get('API_SECRET')

cloudinary.config(
    cloud_name=cloud_name,
    api_key=api_key,
    api_secret=api_secret,
    secure=True
)


class Img(object):

    def __init__(self):
        self.coleccion_usuario = db.coleccion_usuarios
        self.coleccion_producto = db.coleccion_productos

    def verificar_coleccion(self, coleccion: str, id: str):
        if coleccion == 'usuario':
            usuario = self.coleccion_usuario.find_one({'_id': ObjectId(id)})

            if not usuario:
                raise HTTPException(status_code=400, detail={
                    'ok': False,
                    'img': 'Id no válido'
                })
            return usuario

        elif coleccion == 'producto':
            producto = self.coleccion_producto.find_one({'_id': ObjectId(id)})

            if not producto:
                raise HTTPException(status_code=400, detail={
                    'ok': False,
                    'img': 'Id no válido'
                })

            return producto

        else:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'La colección: {coleccion} no exite, debe de pertenecer a: [usuario, producto]'
            })
            
    def update_post_img(self,coleccion, id, file):
        coleccion_verificada = self.verificar_coleccion(coleccion, id)

        if coleccion_verificada['img']:
             destroy(coleccion_verificada['img'].split('/')[-1])


        obj = self.subir_img(coleccion, id, file, public_id='img-coleccion')
        nombre = obj['secure_url']
        
        if coleccion == 'usuario':
            self.coleccion_usuario.find_one_and_update(
                {'_id': ObjectId(id)}, {'$set': {'img': nombre}})
        elif coleccion == 'producto':
            self.coleccion_producto.find_one_and_update(
                {'_id': ObjectId(id)}, {'$set': {'img': nombre}})

    def subir_img(self, coleccion: str, id: str, file: UploadFile, public_id: str):

        return upload(
            file.file,
            public_id=public_id,
            folder=f"{coleccion}/{id}/",
            tags=id
        )



    def get_img(self, coleccion: str, id: str):

        coleccion = self.verificar_coleccion(coleccion, id)
        return {
                '_id': str(coleccion['_id']),
                'img': coleccion['img']
            }

    def update_img(self, coleccion: str, id: str, file: UploadFile):

        self.update_post_img(coleccion, id, file)
        return {
            'img': 'se actualizó la img'
        }

    
    def post_img(self, coleccion: str, id: str, file: UploadFile):

        self.update_post_img(coleccion, id, file)
       
        return {
            'ok': True,
            'msg': 'Se creó una img'
        }
