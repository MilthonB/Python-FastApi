

from fastapi.param_functions import File


class Img(object):

    def get_img(self, id_usuario:int):
        return {
            'img':'Se envío la img'
        }
    
    def update_img(self, coleccion: str, id_usuario: str):
        return {
            'img':'Se actualizó la img'
        }

    def post_img(self, coleccion: str, id_usuario: str, file: File):
        #Mandar la url de la foto almacenada en la file de la root
        return {
            'img':'Se creó una img'
        }