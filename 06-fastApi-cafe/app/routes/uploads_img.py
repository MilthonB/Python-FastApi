from fastapi import APIRouter
from fastapi.param_functions import Path
from controllers.uploads_img import Img

router = APIRouter(
    prefix='/img',
    tags=['Imagenes']
)

img = Img()

#get 
@router.get('/get/')
async def imagen_get():
    return img.get_img()

#update 
@router.put('/put/{coleccion}/{id_usuario}')
async def imagen_update(coleccion:str = Path(...), id_usuario:int = Path(...)):
    return img.update_img()

#post
@router.post('/post/{id_usuario}')
async def imagen_post(id_usuario:int = Path(...)):
    return img.post_img()