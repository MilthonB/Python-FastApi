
from fastapi import APIRouter, Body, Path, UploadFile, File
from typing import Optional, List

from controllers.usuarios import Usuarios
from models import usuario as usuario_model




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

@router.get('/get/')
async def usuarios_get():
    return usuario.get_usuarios()

@router.put('/put/{id_usuario}')
async def usuario_put( id_usuario:int = Path(...), body = Body(...) ):
    return usuario.update_usuario(1, body)

@router.post('/post/')
async def usuario_post(body: usuario_model.Usuario_In = Body(..., embed=True)):
    return usuario.post_usuario(body)

@router.delete('/delete/{id_usuario}')
async def usuario_delete(id_usuario:int = Path(...) ):
    return usuario.delete_usuario(1)