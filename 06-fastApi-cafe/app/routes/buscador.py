
from fastapi import APIRouter, Path


router = APIRouter()


@router.get('/search/{coleccion}/{termino}')
async def buscado(coleccion:str = Path(...), termino:str = Path(...)):
    ... 