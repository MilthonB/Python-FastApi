

from pymongo import MongoClient

from pymongo.collection import Collection 


class Conexion(object):

    def __init__(self):
        self.__uri = f'aquiva la uri de tu basde de mongo '
        self.__client = MongoClient(self.__uri)
        self.__data_base = self.__client.fastApi

    @property
    def coleccion_alumnos(self):
        return self.__data_base.alumnos

    @property
    def coleccion_semestre(self):
        return self.__data_base.semestre
    
    @property
    def coleccion_carrera(self):
        return self.__data_base.carrera