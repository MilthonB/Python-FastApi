
import fastapi


from fastapi import FastAPI
from routes import usuarios,uploads_img
import uvicorn

app = FastAPI()


app.include_router(usuarios.router)
app.include_router(uploads_img.router)


# if __name__ == '__main__':
#     print('Hola mundo ')
#     uvicorn.run(app, port=4500, host='localhost')