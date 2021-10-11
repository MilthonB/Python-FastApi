
# import uvicorn

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request


from routes import usuarios,uploads_img, categorias,productos, auth, buscador
from db.config import db

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(usuarios.router)
app.include_router(categorias.router)
app.include_router(productos.router)
app.include_router(auth.router)
app.include_router(uploads_img.router)
app.include_router(buscador.router)

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request':request})

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080, reload=False) 