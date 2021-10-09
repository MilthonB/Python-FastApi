
#Verificar los roles 
from fastapi import HTTPException, Body, Path
from bson import ObjectId
from typing import Optional

from db.config import db




def rol_verify(id: str):
    
    usuario = db.coleccion_usuarios.find_one({'_id': ObjectId(id)})
    rol_usuario = usuario['rol']
    
    roles = [rol['rol'] for rol in db.coleccion_roles.find({}) ]
    
    if rol_usuario not in roles:
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': f'Rol no permitido, necesitas ser un {roles}'
        })
    elif rol_usuario != 'ADMIN_ROLE':
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': f'Rol no permitido, necesitas ser ADIMN'
        })
        
def categoria_verify( id: Optional[str] = None, body = Body(None, embed=True)): # Valores opcionales 
    
    
    if body:
        id_categoria = body['categoria']
        categoria = db.coleccion_categorias.find_one({'_id':ObjectId(id_categoria)})
        if not categoria or categoria['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'La categoia no existe'
            })
    
    if id:
        categoria = db.coleccion_categorias.find_one({'_id':ObjectId(id)})
        if not categoria or categoria['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'La categoia no existe'
            })
    
    

def usuario_verify(id:Optional[str] = None, body = Body(None, embed=True)):
    # Verificar usuarios si existe el usuario entonces pudes continuar 
    if body:
        id_usuario = body['usuario']
        
        usuario = db.coleccion_usuarios.find_one({'_id':ObjectId(id_usuario)})

        if not usuario or usuario['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'El usuario no existe'
            })
    
    if id:
        usuario = db.coleccion_usuarios.find_one({'_id':ObjectId(id)})

        if not usuario or usuario['estado'] == False:
            raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'El usuario no existe'
            })
        

def producto_verify(id:str = Path(...)):
    
    producto = db.coleccion_productos.find_one({'_id': ObjectId(id)})
    
    if not producto or producto['estado'] == False or producto['disponible'] == False:
         raise HTTPException(status_code=400, detail={
                'ok': False,
                'msg': f'El Producto no existe'
            })
    
    