import time

from fastapi import FastAPI, Request

app = FastAPI()


#Apropiar funcionalidad del middelware
#Documentación bien explicada
# https://fastapi.tiangolo.com/es/tutorial/middleware/

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response
