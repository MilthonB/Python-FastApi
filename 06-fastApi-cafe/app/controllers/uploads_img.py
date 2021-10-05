

from sys import setswitchinterval
import cloudinary
from fastapi import File, UploadFile
from dotenv import dotenv_values

from cloudinary.uploader import upload

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

    def get_img(self, id:str):
        return {
            'img':'Se envío la img'
        }
    
    def update_img(self, coleccion: str, id: str):
        return {
            'img':'Se actualizó la img'
        }

    def post_img(self, coleccion: str, id: str, file: UploadFile):
        #Mandar la url de la foto almacenada en la file de la root
        # cloudinary.uploade.upload("/home/dotmb/Descargas/goku.png")
        # file.file = Al elemento temprario, es decir donde esta la img temporalmenta antes de su descarga o carga, en este caso carga
        
        #Crear folders ejemplo: productos/id/foto
        #Crear folders ejemplo: categorias/id/foto

        obj = {}
        if coleccion == 'productos':
            obj=self.subir_img(coleccion, id, file)
            # obj['secure_url'] guardar en el producto img str
        elif coleccion == 'categorias':
            obj=self.subir_img(coleccion, id, file)
            # obj['secure_url'] guardar en el producto img str

        return {
            'img':'Se creó una img'
        }
        
    
    def subir_img(self, coleccion: str, id: str, file: UploadFile ):
        return upload(
            file.file,
            public_id = file.filename,
            folder = f"{coleccion}/{id}/", 
            tags=id
        )