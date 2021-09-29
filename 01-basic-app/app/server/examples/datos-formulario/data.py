from fastapi import FastAPI, Form

app = FastAPI()


# No usado por mi ni verificado
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}