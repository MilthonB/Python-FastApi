from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel,  Field

app = FastAPI()
    



# Pydantic schema_extra
# examplemodelo Pydantic usando Configy schema_extra

# Esa información adicional se agregará tal cual al esquema JSON de salida para ese modelo y se usará en los documentos de la API.
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:# esta información se muestra en los docs localhost:{port}/docs
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


#usando Field puede agregar o añadir example para cada campo 
# esto se mostrara en localhos docs
# los datos se muestra igual
class Item2(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


@app.put("/put/example/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results



@app.put("/schema/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results