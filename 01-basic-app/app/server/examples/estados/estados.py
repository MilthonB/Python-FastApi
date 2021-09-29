from fastapi import FastAPI, status

app = FastAPI()


# @app.post("/estados/items/", status_code=200)
@app.post("/estados/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}