from fastapi import FastAPI

app = FastAPI()


@app.post("/estados/items/", status_code=200)
async def create_item(name: str):
    return {"name": name}