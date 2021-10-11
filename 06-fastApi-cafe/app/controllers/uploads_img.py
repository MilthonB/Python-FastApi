

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


#Código repetido optimizar 

class Img(object):

    def __init__(self):
        self.coleccion_usuario = db.coleccion_usuarios
        self.coleccion_producto = db.coleccion_productos

    def get_img(self, coleccion: str, id: str):

        if coleccion == 'usuario':
            usuario = self.coleccion_usuario.find_one({'_id': ObjectId(id)})

            if not usuario['img'] or not usuario:
                raise HTTPException(status_code=400, detail={
                    'ok': False,
                    'img': 'Imagen no encotrada'
                })

            return {
                '_id': str(usuario['_id']),
                'img': usuario['img']
            }

        elif coleccion == 'producto':
            producto = self.coleccion_producto.find_one({'_id': ObjectId(id)})

            if not producto['img'] or not producto:
                raise HTTPException(status_code=400, detail={
                    'ok': False,
                    'img': 'Imagen no encotrada'
                })

            return {
                'img': 'Se actualizó la imagen'
            }

        else:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'La colección: {coleccion} no exite, debe de pertenecer a: [usuario, producto]'
            })

        return {
            'img': 'Se envío la img'
        }

    def update_img(self, coleccion: str, id: str, file: UploadFile):

        if coleccion == 'usuario':
            usuario = self.coleccion_usuario.find_one({'_id': ObjectId(id)})

            if not usuario['img'] or not usuario:
                raise HTTPException(status_code=400, detail={
                    'ok': False,
                    'img': 'Imagen no encotrada'
                })

            obj = self.subir_img(coleccion, id, file, public_id='img-perfil')
            nombre = obj['secure_url']
            self.coleccion_usuario.find_one_and_update(
                {'_id': ObjectId(id)}, {'$set': {'img': nombre}})

            return {
                'img': 'se actualizó la img'
            }

        elif coleccion == 'producto':
            producto = self.coleccion_producto.find_one({'_id': ObjectId(id)})

            if not producto['img'] or not producto:
                raise HTTPException(status_code=400, detail={
                    'ok': False,
                    'img': 'Imagen no encotrada'
                })

            obj = self.subir_img(coleccion, id, file, public_id='img-producto')
            nombre = obj['secure_url']
            
            self.coleccion_producto.find_one_and_update(
                {'_id': ObjectId(id)}, {'$set': {'img': nombre}})

            return {
                'img': 'se actualizó la img'
            }

        else:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'La colección: {coleccion} no exite, debe de pertenecer a: [usuario, producto]'
            })

    def subir_img(self, coleccion: str, id: str, file: UploadFile, public_id: str):

        return upload(
            file.file,
            public_id=public_id,
            folder=f"{coleccion}/{id}/",
            tags=id
        )

    def post_img(self, coleccion: str, id: str, file: UploadFile):

        if coleccion == 'usuario':
            usuario = self.coleccion_usuario.find_one({'_id': ObjectId(id)})

            if usuario['img']:
                destroy(usuario['img'].split('/')[-1])

            obj = self.subir_img(coleccion, id, file, public_id='img-perfil')
            nombre = obj['secure_url']

            self.coleccion_usuario.find_one_and_update(
                {'_id': ObjectId(id)}, {'$set': {'img': nombre}})

        elif coleccion == 'producto':

            producto = self.coleccion_producto.find_one({'_id': ObjectId(id)})

            if producto['img']:
                destroy(producto['img'].split('/')[-1])

            obj = self.subir_img(coleccion, id, file, public_id='img-producto')
            nombre = obj['secure_url']

            self.coleccion_producto.find_one_and_update(
                {'_id': ObjectId(id)}, {'$set': {'img': nombre}})
        else:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'La colección: {coleccion} no exite, debe de pertenecer a: [usuario, producto]'
            })
        return {
            'ok': False,
            'msg': 'Se creó una img'
        }
