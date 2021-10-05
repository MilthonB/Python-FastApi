from fastapi import APIRouter, UploadFile, File, Path
from fastapi.param_functions import Depends
from controllers.uploads_img import Img
from helpers.dependencias import dependencias_generales as depen

router = APIRouter(
    prefix='/img',
    tags=['Imagenes']
)

img = Img()

lista_dependencias = [
    Depends(depen.verify_mongoId),
    Depends(depen.verify_coleccion),
]



@router.get('/get/{id_usuario}')
async def imagen_get(id_usuario: int = Path(...)):
    return img.get_img(id_usuario)

#update 
@router.put('/put/{coleccion}/{id_usuario}', dependencies=lista_dependencias)
async def imagen_update(coleccion:str = Path(...), id_usuario:str = Path(...), file: UploadFile = File(...)):
    return img.update_img( coleccion, id_usuario )

#post 
@router.post('/post/{coleccion}/{id_usuario}', dependencies=lista_dependencias)
async def imagen_post(id_usuario:str = Path(...), coleccion:str = Path(...), file: UploadFile = File(...)):
    return img.post_img( coleccion, id_usuario, file )


