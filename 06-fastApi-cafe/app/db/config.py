from enum import unique
from pymongo import MongoClient
from functools import lru_cache
from dotenv import dotenv_values

mongodb = dotenv_values().get('MONGODB')

class Conexion(object):

    @lru_cache()
    def __init__(self):
        self.__uri = mongodb
        self.__client = MongoClient(self.__uri)
        self.__data_base = self.__client.Cafe_fastapi
        print('conectado db')

    @property
    def coleccion_usuarios(self):
        self.__data_base.usuarios.create_index('correo', unique=True)
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