

from fastapi import Depends, HTTPException
from bson import ObjectId

from db.config import db


lista_colecciones = ['productos','categorias']
def verify_coleccion(coleccion: str):
    print(coleccion)
    if coleccion not in lista_colecciones:
        raise HTTPException(status_code=400,detail={
            'ok':False,
            'msg':f'La coleccion ingresada no es valida. Colecciones válidas: {lista_colecciones}'
        })

def verify_mongoId( id:str ):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400,detail={
            'ok':False,
            'msg':f'El id no es válido: {id}'
        })

def verify_id_In_bd( id:str ):
    usuario = db.coleccion_usuarios.find_one({'_id': ObjectId(id)})

    if not usuario:
        raise HTTPException(status_code=400,detail={
            'ok':False,
            'msg':f'El id no esxiste: {id}'
        })
    elif usuario['estado'] == False:
        raise HTTPException(status_code=400,detail={
            'ok':False,
            'msg':f'El id esta inhabilitado: {id}'
        })
