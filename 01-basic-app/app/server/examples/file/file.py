import shutil
from typing import List

from fastapi import FastAPI, File, UploadFile
from starlette.responses import HTMLResponse

app = FastAPI()



@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)): # UploadFile tiene la ventaja que puede manejar archivos grandess

    #Operacion para guardar una imagen subida
    with open('../../img/imagen-prueba.png','wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.file}



@app.post("/uploadfile/list")
async def create_upload_file(files: List[UploadFile] = File(...)): # guardar mutiples imgaenes

    #Operacion para guardar una imagen subida
    for file in files:
        print(file.filename)
        with open(f'../../img/{file.filename}','wb') as buffer:
            shutil.copyfileobj(file.file, buffer)

    return {"filename": files}



# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)