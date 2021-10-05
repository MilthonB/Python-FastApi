
from fastapi import APIRouter, Body, Path, Depends
from typing import Optional, List

from controllers.usuarios import Usuarios
from models import usuario as usuario_model
from helpers.dependencias.dependencias_generales import verify_mongoId 




router = APIRouter(
    prefix='/usuarios',
    tags=['Usuarios']
)

usuario = Usuarios()

""" 
Dependencias:
    tiene que ser un id de mongo => LISTO DEPENDENCIA CREADA 
    el id tiene que existir en la base de datos
    y el rol tiene que ser admin para poder hacert put post y delete
    contraseña tiene que tener un cierto rango 
    el correo tiene que ser un correo email válido
    jwt válido también en el delete
"""
#Señalar cuando no esta el path element dentro del path principal

@router.get('/get/', response_model= usuario_model.Usuario_Out)
async def usuarios_get():
    return usuario.get_usuarios()

@router.get('/get/{id}',response_model= usuario_model.Usuario_Out, dependencies=[Depends(verify_mongoId)])
async def usuario_get(id:str = Path(...)):
    return usuario.get_usuario(id)

@router.put('/put/{id}', dependencies=[Depends(verify_mongoId)])
async def usuario_put( id:str = Path(...), body = Body(...) ):
    return usuario.update_usuario(id, body)

@router.post('/post/', response_model=usuario_model.Usuario_Out)
async def usuario_post(body: usuario_model.Usuario_In = Body(..., embed=True)):
    return usuario.post_usuario(body)

@router.delete('/delete/{id}', dependencies=[Depends(verify_mongoId)])
async def usuario_delete(id:str = Path(...) ):
    return usuario.delete_usuario(1)