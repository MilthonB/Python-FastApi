
from fastapi import APIRouter
from fastapi.params import Body
from controllers.auth import Auth

from models.auth import Auth_In
from models.usuario import Usuario_Out
router = APIRouter()

auth = Auth()

@router.post('/login', response_model= Usuario_Out)
async def login( body: Auth_In = Body(...) ):
    resp = await auth.login( body )
    return resp
