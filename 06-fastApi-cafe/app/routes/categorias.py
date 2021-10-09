
from fastapi import APIRouter, Body, Path, Depends
from typing import Optional, List

from fastapi.param_functions import Query

from controllers.categorias import Categorias
from models import categoria as categoria_model

from helpers.dependencias.dependencias_generales import verify_mongoId 
from helpers.dependencias import db_dependencias as db_depns

router = APIRouter(
    prefix='/categorias',
    tags=['Categorias']
)

categoria = Categorias()

lista_dependencias = [
    Depends(verify_mongoId),
    Depends(db_depns.categoria_verify)
]

@router.get('/get/', response_model= List[categoria_model.Categorias_Out])
async def categorias_get(limit:Optional[int] = Query(10), skip:Optional[int] = Query(0)):
    resp = await categoria.get_categorias(limit, skip)
    return resp

@router.get('/get/{id}',response_model= categoria_model.Categorias_Out, dependencies=lista_dependencias)
async def categoria_get(id:str = Path(...)):
    resp = await categoria.get_categoria(id) 
    return resp

@router.put('/put/{id}', response_model= categoria_model.Categorias_Out, dependencies=lista_dependencias)
async def categoria_put( id:str = Path(...), body = Body(...) ):
    resp = await categoria.update_categoria(id, body) 
    return resp

@router.post('/post/', response_model=categoria_model.Categorias_Out)
async def categoria_post(body: categoria_model.Categorias_Base = Body(..., embed=True)):
    resp = await categoria.post_categoria(body)
    return resp
    # return categoria.post_categoria(body)

@router.delete('/delete/{id}', response_model=categoria_model.Categorias_Out, dependencies=lista_dependencias)
async def usuario_delete(id:str = Path(...) ):
    resp = await categoria.delete_categoria(id)
    return resp