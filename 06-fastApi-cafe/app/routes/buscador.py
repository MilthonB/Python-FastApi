
from fastapi import APIRouter, Path, Header, Depends
from controllers.buscador import Buscador
from helpers.dependencia_jwt import jwt_decode


router = APIRouter( tags=['Buscador'])

buscar = Buscador()

@router.get('/search/{coleccion}/{termino}', dependencies=[Depends(jwt_decode)])
async def buscado(x_token:str = Header(..., convert_underscores=False), coleccion:str = Path(...), termino:str = Path(...)):
    resp = await buscar.buscador(termino, coleccion)
    return resp