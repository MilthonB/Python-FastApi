
# import uvicorn

from fastapi import FastAPI
from routes import usuarios,uploads_img, categorias,productos, auth
from db.config import db

app = FastAPI()



app.include_router(usuarios.router)
app.include_router(categorias.router)
app.include_router(productos.router)
app.include_router(auth.router)
app.include_router(uploads_img.router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080, reload=False) 