from typing import Optional

from fastapi import FastAPI, Body
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

    # esta información se muestra en los docs localhost:{port}/docs
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


# usando Field puede agregar o añadir example para cada campo
# esto se mostrara en localhos docs
# los datos se muestra igual
# Al usar cualquiera de:
#
# Path()
# Query()
# Header()
# Cookie()
# Body()
# Form()
# File()
# también puede declarar un dato example
class Item2(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


@app.put("/put/example/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


#Body con múltiples examples
# Anidados unos con otros 
#  Esto se omuestra en la OpenAPI
@app.put("/put/body/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
        # example={
        #     "name": "Foo",
        #     "description": "A very nice Item",
        #     "price": 35.4,
        #     "tax": 3.2,
        # },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/schema/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
