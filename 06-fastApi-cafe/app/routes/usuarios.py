
from fastapi import APIRouter, Body
from typing import Optional, List
from fastapi.params import Param
from controllers.usuarios import Usuarios

router = APIRouter(
    prefix='/usuarios',
    tags=['Usuarios']
)

usuario = Usuarios()

"""
Dependencias:
    tiene que ser un id de mongo
    el id tiene que existir en la base de datos
    y el rol tiene que ser admin para poder hacert put post y delete
    contraseña tiene que tener un cierto rango 
    el correo tiene que ser un correo email válido
    jwt válido también en el delete
"""


@router.get('/get/')
async def usuarios_get():
    return usuario.get_usuarios()

@router.put('/put/{id_usuario}')
async def usuario_put( id_usuario:int = Param(...) ):
    ...

@router.post('/post/')
async def usuario_post(body= Body(...)):
    return body

@router.delete('/delete/{id_usuario}')
async def usuario_delete(id_usuario:int = Param(...) ):
    ...