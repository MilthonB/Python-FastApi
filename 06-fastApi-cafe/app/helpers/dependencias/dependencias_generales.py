

from fastapi import Depends, HTTPException
from bson import ObjectId


lista_colecciones = ['productos','categorias']
def verify_coleccion(coleccion: str):
    print(coleccion)
    if coleccion not in lista_colecciones:
        raise HTTPException(status_code=400,detail={
            'ok':False,
            'msg':f'La coleccion ingresada no es valida. Colecciones válidas:${lista_colecciones}'
        })

def verify_mongoId( id_usuario:str ):
    if not ObjectId.is_valid(id_usuario):
        raise HTTPException(status_code=400,detail={
            'ok':False,
            'msg':f'El id no es válido: ${lista_colecciones}'
        })