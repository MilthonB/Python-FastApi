from fastapi import APIRouter, Depends

from dependencies import get_token_header


router = APIRouter(
    prefix='/users',
    dependencies= [Depends( get_token_header )],
    tags=['Users'],
)

#Rutas que manejan solo los usuarios

@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}