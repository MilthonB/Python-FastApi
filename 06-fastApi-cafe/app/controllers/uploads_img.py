

from fastapi.param_functions import File
from dotenv import dotenv_values
import cloudinary


config = dotenv_values(".env")

print(config.get('CLOUDINARY_URL'),'dotenv')


class Img(object):

    def get_img(self, id:str):
        return {
            'img':'Se envío la img'
        }
    
    def update_img(self, coleccion: str, id: str):
        return {
            'img':'Se actualizó la img'
        }

    def post_img(self, coleccion: str, id: str, file: File):
        #Mandar la url de la foto almacenada en la file de la root
        return {
            'img':'Se creó una img'
        }