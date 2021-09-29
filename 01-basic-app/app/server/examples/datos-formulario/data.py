from fastapi import FastAPI, Form

app = FastAPI()

# https://fastapi.tiangolo.com/es/tutorial/request-forms/


# No usado por mi ni verificado
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}