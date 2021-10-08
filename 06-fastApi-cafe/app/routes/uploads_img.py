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



@router.get('/get/{id}')
async def imagen_get(id: str = Path(...)):
    return img.get_img(id)

#update 
@router.put('/put/{coleccion}/{id}', dependencies=lista_dependencias)
async def imagen_update(coleccion:str = Path(...), id:str = Path(...), file: UploadFile = File(...)):
    return img.update_img( coleccion, id )

#post 
lista_dependencias.append(Depends(depen.verify_type_img))
@router.post('/post/{coleccion}/{id}', dependencies=lista_dependencias)
async def imagen_post(id:str = Path(...), coleccion:str = Path(...), file: UploadFile = File(...)):
    return img.post_img( coleccion, id, file )


