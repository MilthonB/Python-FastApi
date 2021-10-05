
from fastapi import APIRouter, Body, Path, Depends, Query
from typing import Optional, List


from controllers.productos import Productos
from models import producto as producto_model 

from helpers.dependencias.dependencias_generales import verify_mongoId 

router = APIRouter(
    prefix='/productos',
    tags=['Productos']
)

producto = Productos()


@router.get('/get/', response_model= List[producto_model.Productos_Out])
async def productos_get(limit:Optional[int] = Query(10), skip:Optional[int] = Query(0)):
    resp = await producto.get_productos(limit, skip)
    return resp

@router.get('/get/{id}',response_model= producto_model.Categorias_Out, dependencies=[Depends(verify_mongoId)])
async def producto_get(id:str = Path(...)):
    resp = await producto.get_producto(id) 
    return resp

@router.put('/put/{id}', response_model= producto_model.Productos_Out, dependencies=[Depends(verify_mongoId)])
async def producto_put( id:str = Path(...), body = Body(...) ):
    resp = await producto.update_producto(id, body) 
    return resp

@router.post('/post/', response_model=producto_model.Productos_Out)
async def producto_post(body: producto_model.Productos_Base = Body(..., embed=True)):
    resp = await producto.post_producto(body)
    return resp
    # return categoria.post_categoria(body)

@router.delete('/delete/{id}', response_model=producto_model.Productos_Out, dependencies=[Depends(verify_mongoId)])
async def producto_delete(id:str = Path(...) ):
    resp = await producto.delete_producto(id)
    return resp

