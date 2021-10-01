from typing import List, Optional

from pydantic import BaseModel

# https://fastapi.tiangolo.com/es/tutorial/sql-databases/

# Creación de los modelos 

#Modelo item base, los demas heredaran de ItemBase y a su vez este hereda de BaseModel de Pydantic para generar el modelo 
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

# Este config y los demas le dicen al model de pydantic que lea los data incluso aunque no sea un dict, ya que sera un ORM model
# Y si antes para acceder a los valores tenia se hacer un item = data['id']
# Ahora sera item = data.id
    class Config: 
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True