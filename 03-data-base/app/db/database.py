from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Creacion de la base de datos 

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" #URL a la base de datos, Se generara un archivo con ese  nombre 
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#Generar el motor de la base de datos
# Se envia la base de datos que se encuentra en blanco que es la sql_app.db, puede tener cualquier nombre
# Otro parametro que recibe es el connect_arg se utiliza para usar multi hilos en la base de datos y decirle que tendrá varias lineas de conexción 
# Ya que sqlite se comunica por una sola linea  
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)  

#Se genera la linea o sesión para las comunicaciones que se requieren
#Es una clase por eso el nombre en mayuscula
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Se declara la base para crear cada uno de los modelos que se necesiten en la base de datos 
Base = declarative_base()