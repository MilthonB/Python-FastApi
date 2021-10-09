
from fastapi import APIRouter, Body, Path, Depends, Header
from typing import Optional, List

from fastapi.param_functions import Query

from controllers.usuarios import Usuarios
from models import usuario as usuario_model
from helpers.dependencias.dependencias_generales import verify_mongoId, verify_id_In_bd
from helpers.dependencias.db_dependencias import rol_verify
from helpers.dependencia_jwt import jwt_decode
from helpers.dependencias import db_dependencias as db_depns

router = APIRouter(
    prefix='/usuarios',
    tags=['Usuarios']
)

usuario = Usuarios()

lista_depends = [
    Depends(verify_mongoId), 
    Depends(verify_id_In_bd),
    Depends(jwt_decode),
    Depends(db_depns.usuario_verify)
]

@router.get('/get/', response_model= List[usuario_model.Usuario_Out])
async def usuarios_get(limit:Optional[int] = Query(10), skip:Optional[int] = Query(0)):
    return usuario.get_usuarios(limit, skip)

@router.get('/get/{id}',response_model= usuario_model.Usuario_Out, dependencies=lista_depends)
async def usuario_get(id:str = Path(...)):
    return usuario.get_usuario(id)

@router.put('/put/{id}', response_model= usuario_model.Usuario_Out, dependencies=lista_depends)
async def usuario_put( id:str = Path(...), body:usuario_model.Usuario_update = Body(...) ):
    resp = await usuario.update_usuario(id, body) 
    return resp

@router.post('/post/', response_model=usuario_model.Usuario_Out)
async def usuario_post(body: usuario_model.Usuario_In = Body(..., embed=True)):
    return usuario.post_usuario(body)

lista_depends.append(Depends(rol_verify))
lista_depends.append(Depends(jwt_decode))
@router.delete('/delete/{id}', response_model=usuario_model.Usuario_Out, dependencies=lista_depends)
async def usuario_delete(id:str = Path(...), x_token: str = Header(..., convert_underscores=False) ):
    return usuario.delete_usuario(id)