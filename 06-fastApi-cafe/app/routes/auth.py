
from fastapi import APIRouter
from fastapi import Body, Response, Request
from pydantic.types import Json
from starlette.responses import JSONResponse
from controllers.auth import Auth
from localStoragePy import localStoragePy


from models.auth import Auth_In
from models.usuario import Usuario_Out

router = APIRouter( tags=['Login'] )

auth = Auth()

@router.post('/login', response_model= Usuario_Out)
async def login( response: Response, body: Auth_In = Body(...) ):
    resp = await auth.login(body,response)
    return resp


# @router.post("/cookie-and-object/")
# def create_cookie(response: Response):
#     print(response)
#     response.set_cookie (key="fakesession", value="fake-cookie-session-value")
#     return {"message": "Come to the dark side, we have cookies"}

# @router.post("/cookie/")
# def create_cookie(req: Request):
#     localStorage = localStoragePy('Api-cafe','storage-token')
#     localStorage.setItem('token','token')
#     print(localStorage.getItem('token'))

#     content = {"message": "Come to the dark side, we have cookies"}
#     response = JSONResponse(content=content)
#     # request = JSONR
#     a = req._cookies.get('TONTO')
#     print('Nda',a)
#     response.set_cookie(key="TONTO", value="fake-cookie-session-value")
#     return response

