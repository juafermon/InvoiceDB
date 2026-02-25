from fastapi import FastAPI, HTTPException
import sqlitecloud
from pydantic import BaseModel

from app.dbSQlite import get_db_connection

app = FastAPI()

@app.get("/tablaUsuarios")
def leer_usuarios():
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Error al conectar con SQLiteCloud")
    
    try:
        cursor = conn.cursor()
        # Seleccionamos todos los registros de tu tabla
        cursor.execute("SELECT * FROM USER")
        result = cursor.fetchall()

        #print(result, "Registros obtenidos de la tabla USER")
        
        # Obtenemos los nombres de las columnas para devolver un JSON limpio
        columnas = [column[0] for column in cursor.description]
        usuarios = []
        
        for fila in result:
            usuarios.append(dict(zip(columnas, fila)))
        
        return {"usuarios": usuarios}
    
    except Exception as e:
        print(f"Error al leer datos: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        conn.close()

class UsuarioCreate(BaseModel):
    identification: int
    name: str
    last_name: str
    address: str
    

@app.post("/crearusuarios")
def crear_usuarios(usuario: UsuarioCreate):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Error al conectar con SQLiteCloud")
    try:
        cursor = conn.cursor()
        query = "INSERT INTO USER (identification, name, last_name, address) VALUES (?, ?, ?, ?)"
        values = (usuario.identification, usuario.name, usuario.last_name, usuario.address)
        
        cursor.execute(query, values)
        return {"Usuario": usuario}
    
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        conn.close()

#@app.post("/products/", response_model=schemas.Product)
#def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
#    # Lógica: Crear el modelo de BD con los datos del esquema
#    db_product = models.Product(**product.dict())
#    db.add(db_product)
#    db.commit()
#    db.refresh(db_product)
#    return db_product

#@app.get("/products/", response_model=List[schemas.Product])
#def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
#    products = db.query(models.Product).offset(skip).limit(limit).all()
#    return products