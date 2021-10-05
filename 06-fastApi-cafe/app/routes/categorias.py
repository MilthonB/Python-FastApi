
from fastapi import APIRouter, Body, Path, Depends
from typing import Optional, List

from fastapi.param_functions import Query

from controllers.categorias import Categorias
from models import categoria as categoria_model

from helpers.dependencias.dependencias_generales import verify_mongoId 

router = APIRouter(
    prefix='/categorias',
    tags=['Categorias']
)

categoria = Categorias()


@router.get('/get/', response_model= List[categoria_model.Categorias_Out])
async def categorias_get(limit:Optional[int] = Query(10), skip:Optional[int] = Query(0)):
    return categoria.get_categorias(limit, skip)

@router.get('/get/{id}',response_model= categoria_model.Categorias_Out, dependencies=[Depends(verify_mongoId)])
async def usuario_get(id:str = Path(...)):
    return categoria.get_categoria(id)

@router.put('/put/{id}', response_model= categoria_model.Categorias_Out, dependencies=[Depends(verify_mongoId)])
async def categoria_put( id:str = Path(...), body = Body(...) ):
    return categoria.update_categoria(id, body)

@router.post('/post/', response_model=categoria_model.Categorias_Out)
async def usuario_post(body: categoria_model.Categorias_Base = Body(..., embed=True)):
    return categoria.post_categoria(body)

@router.delete('/delete/{id}', response_model=categoria_model.Categorias_Out, dependencies=[Depends(verify_mongoId)])
async def usuario_delete(id:str = Path(...) ):
    return categoria.delete_categoria(id)