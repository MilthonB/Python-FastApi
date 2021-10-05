from pymongo import MongoClient
from functools import lru_cache
from dotenv import dotenv_values

mongodb = dotenv_values().get('MONGODB')

class Conexion(object):

    @lru_cache()
    def __init__(self):
        print('conectado', mongodb)
        self.__uri = mongodb
        self.__client = MongoClient(self.__uri)
        self.__data_base = self.__client.Cafe_fastapi

    @property
    def coleccion_usuarios(self):
        return self.__data_base.usuarios

    @property
    def coleccion_productos(self):
        return self.__data_base.productos
    
    @property
    def coleccion_categorias(self):
        return self.__data_base.categorias

    @property
    def coleccion_roles(self):
        return self.__data_base.roles

db = Conexion()