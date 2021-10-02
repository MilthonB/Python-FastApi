from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"Ejemplo": "Error"}}, # Se pede agregar un modelo de respuesta para todos este es un ejemplo que no hace nada 
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail={
            'ok': False,
            'msg': 'El item no se encontro',
            'item_id': item_id
        })
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}

@router.put("/{item_id}", tags=["custom"])
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail={
                'ok':False,
                'msg':'Sólo puedes actualizar el elemento plumbus',
                'item_id': item_id
            }
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
