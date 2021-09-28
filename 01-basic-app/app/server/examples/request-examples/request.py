from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

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


@app.put("/schema/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results