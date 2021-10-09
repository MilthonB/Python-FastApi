
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
    ...

def categoria_verify(body):
    ...
