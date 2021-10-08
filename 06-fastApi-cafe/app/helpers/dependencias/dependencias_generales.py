from fastapi import Depends, HTTPException
from bson import ObjectId
from fastapi import UploadFile, File

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

def verify_type_img( file: UploadFile = File(...)):
    tipo_extencion = file.filename.split('.')[-1];
    #obtener la extencion del archivo png, jpeg, jpg
    extenciones_validas = ['png', 'jpeg', 'jpg']
    
    if tipo_extencion not in extenciones_validas:
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': 'Archivo de imagen no válida'
        })
    