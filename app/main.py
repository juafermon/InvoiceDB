#Punto de entrada de la app
from fastapi import FastAPI, Depends, HTTPException
#from sqlalchemy.orm import Session
#from typing import List

app = FastAPI()

@app.get("/documents")
def read_root():
    return {"Diccionario": "Prueba API"}

#from . import models, schemas, database

# Crear las tablas en la BD automáticamente al iniciar
#models.Base.metadata.create_all(bind=database.engine)

#app = FastAPI(title="API Facturación")

# ------ RUTAS DE PRODUCTOS -------

#@app.post("/")
#def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    # creacion del modelo de BD con los datos del esquema
    #db_product = models.Product(**product.dict())
    #db.add(db_product)
    #db.commit()
    #db.refresh(db_product)
    #return db_product

#@app.get("/")
#def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    #products = db.query(models.Product).offset(skip).limit(limit).all()
    #return products