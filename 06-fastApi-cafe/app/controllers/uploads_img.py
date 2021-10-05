

from fastapi.param_functions import File
import cloudinary




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