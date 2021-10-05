

from pymongo import MongoClient

class Db_cafe(object):

    def __init__(self):
        self.__uri = f'Aqui va la uri de mongodb'
        self.__client = MongoClient(self.__uri)
        self.__data_base = self.__client.<nombre de tu base de datos> #sin las llavez
        # self.__data_base = self.__client.nombredelabasededatos #sin las llavez