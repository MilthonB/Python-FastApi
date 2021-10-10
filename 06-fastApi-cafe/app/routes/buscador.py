
from fastapi import APIRouter, Path
from controllers.buscador import Buscador

router = APIRouter( tags=['Buscador'])

buscar = Buscador()

@router.get('/search/{coleccion}/{termino}')
async def buscado(coleccion:str = Path(...), termino:str = Path(...)):
    resp = await buscar.buscador(termino, coleccion)
    return resp