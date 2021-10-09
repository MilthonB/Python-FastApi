
#Verificar los roles 
from fastapi import HTTPException
from bson import ObjectId

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
        
def producto_verify(body):
    producto_id = body['producto']
    producto = db.coleccion_productos.find_one({'_id':ObjectId(producto_id)})
    
    if not producto:
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': f'El Producto no existe'
        })
    

def categoria_verify(body):
    categoria_id = body['categoria']
    categoria = db.coleccion_categorias.find_one({'_id':ObjectId(categoria_id)})
    
    if not categoria:
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': f'La Categoria no existe'
        })
    
    