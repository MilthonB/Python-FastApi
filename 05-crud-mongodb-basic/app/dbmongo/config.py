

from pymongo import MongoClient

from pymongo.collection import Collection 


class Conexion(object):

    def __init__(self):
        self.__uri = f'mongodb+srv://fastApi:XUtKn6tvRlO1vyuj@clusterfastapi.ppox7.mongodb.net/test?authSource=admin&replicaSet=atlas-vvtkil-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
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