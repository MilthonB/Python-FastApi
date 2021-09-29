from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


# Modelo base
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


# Herencia del modelo base
class UserIn(UserBase):
    password: str


# Herencia del modelo base
class UserOut(UserBase):
    pass


# Herencia del modelo base
class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    # Los modelos Pydantic tienen un .dict()método que devuelve un dictcon los datos del modelo.    
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved