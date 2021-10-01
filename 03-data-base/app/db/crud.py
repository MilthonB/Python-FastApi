from sqlalchemy.orm import Session
from db import modelos, schema

def get_user(db: Session, user_id: int): # Obtener un usuario  por el id, recibe la seccion de la base ded atos y el usuario de tipo int
    return db.query(modelos.User).filter(modelos.User.id == user_id).first()
    #utiliza la sesion de la base de datos para hacer un query a User y filtra por el id y toma el primer elemento

def get_user_by_email(db: Session, email: str):#Obtener un usuario por el email
    return db.query(modelos.User).filter(modelos.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):#Obtener los usuarios
    return db.query(modelos.User).offset(skip).limit(limit).all() # retorna una grupo de objetos 

def create_user(db: Session, user: schema.UserCreate): #Crear uusuario
    fake_hashed_password = user.password + "notreallyhashed" 
    db_user = modelos.User(email=user.email, hashed_password=fake_hashed_password) # Se genera el modelo de tabla User a la basde de datos
    db.add(db_user)  #Se cargan los datos del modelo creado
    db.commit() # Se cambian los datos de la tabla 
    db.refresh(db_user) # se aplican y se generan los cambios
    return db_user # retorna el usuario creado

def get_items(db: Session, skip: int = 0, limit: int = 100): #Obtener los items 
    return db.query(modelos.Item).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: schema.ItemCreate, user_id: int): #Crear item
    db_item = modelos.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
