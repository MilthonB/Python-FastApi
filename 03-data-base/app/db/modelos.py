

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#Importacion de Base para la creacion en la base de datos de nuestro modelos 
from .database import Base

#Primer modelo, USer
class User(Base):
    __tablename__ = "users" #Este __tablename__ le dira a sqlalchemy el nombre de la tabla en la base de datos 

    #Atributos de la tabla users
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    #Relaciones que tiene el usuario con los items 
    items = relationship("Item", back_populates="owner")



class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    #Relaciones que tiene el items con el usuario  
    owner = relationship("User", back_populates="items")
