# https://fastapi.tiangolo.com/es/tutorial/security/first-steps/
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") #Es una url relativa ./token http://localhost:8080/token


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
