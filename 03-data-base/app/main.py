

#Importaciones para el funcionamiento 
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal, engine
from db import crud, modelos, schema


modelos.Base.metadata.create_all(bind=engine) # Se crean las tablas de la base de datos que se encuentran en los modelos

app = FastAPI() # Se incio la app de fast api


# Dependency
def get_db(): # Se obtiene en incio del secion con el operador yield
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schema.User) #Operacion (petición) a usuarios create  post y la respuesta es un Schema.Usuer
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)): # Se espera un user de UserCreate Schema y una sesion de bd que se obtiene de get_db
    db_user = crud.get_user_by_email(db, email=user.email)  #Verificas si ese correo o email ya existe 
    if db_user: # Si existe mandas un exception code status 400
        raise HTTPException(status_code=400, detail={
            'ok': False,
            'msg': 'El correo ya fue registrado'
        })
    return crud.create_user(db=db, user=user) # Si todo pasa, se crea el usuario y devuelve el usuario creado


@app.get("/users/", response_model=List[schema.User]) #Opereación get, response Lista de User
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)): # tiene un dependecia co la sesion de la base de datos
    users = crud.get_users(db, skip=skip, limit=limit) # Retorna un objeto con todos los valores
    return users # retorna el objeto como una lista 

#Igual que los demás
@app.get("/users/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail={
            'ok':False,
            'msg':'El usuario no se encontro',
            'id': user_id
        })
    return db_user


@app.post("/users/{user_id}/items/", response_model=schema.Item)
def create_item_for_user(user_id: int, item: schema.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
