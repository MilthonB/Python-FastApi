
import fastapi


from fastapi import FastAPI
from routes import usuarios

app = FastAPI()


app.include_router(usuarios.router)

