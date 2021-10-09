
from fastapi import APIRouter, Body, Path, Depends, Query, Header
from typing import Optional, List


from controllers.productos import Productos
from models import producto as producto_model 

from helpers.dependencias.dependencias_generales import verify_mongoId
from helpers.dependencia_jwt import jwt_decode
from helpers.dependencias import db_dependencias as db_deps

router = APIRouter(
    prefix='/productos',
    tags=['Productos']
)

producto = Productos()

lista_depends=[
    Depends(verify_mongoId),
    Depends(jwt_decode),
    Depends(db_deps.producto_verify)
]

@router.get('/get/', response_model= List[producto_model.Productos_Out])
async def productos_get(limit:Optional[int] = Query(10), skip:Optional[int] = Query(0)):
    resp = await producto.get_productos(limit, skip)
    return resp

@router.get('/get/{id}',response_model= producto_model.Productos_Out, dependencies=lista_depends)
async def producto_get(id:str = Path(...), x_token:str = Header(..., convert_underscores=False )):
    resp = await producto.get_producto(id) 
    return resp

@router.put('/put/{id}', response_model= producto_model.Productos_Out, dependencies=lista_depends)
async def producto_put( id:str = Path(...), body = Body(...), x_token:str = Header(...,  convert_underscores=False) ):
    resp = await producto.update_producto(id, body) 
    return resp


@router.delete('/delete/{id}', response_model=producto_model.Productos_Out, dependencies=lista_depends)
async def producto_delete(id:str = Path(...) , x_token:str = Header(...,  convert_underscores=False)):
    resp = await producto.delete_producto(id)
    return resp


@router.post('/post/', response_model=producto_model.Productos_Out, dependencies=[Depends(jwt_decode), Depends(db_deps.categoria_verify), Depends(db_deps.usuario_verify)])
async def producto_post(body: producto_model.Productos_Base = Body(..., embed=True)):
    resp = await producto.post_producto(body)
    return resp
