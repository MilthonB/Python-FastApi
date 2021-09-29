from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


# se ejecutaran los verify pero si las funciones tiene  algo que retornar 
# entonces no de podrán observar en la funcion de la operacion con el método get
@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)]) 
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
