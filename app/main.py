from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import timedelta
from typing import List

# Importaciones locales
from .database import get_db
from .core import security
from . import crud, schemas

app = FastAPI(
    title="Sistema de Facturación API",
    description="Backend con conexión directa a SQLite Cloud",
    version="1.1.0"
)

# Configuración de CORS para Flutter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# --- DEPENDENCIAS DE SEGURIDAD ---

def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # Buscamos al usuario con SQL puro a través del CRUD
    user = crud.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user

# --- RUTAS DE AUTENTICACIÓN ---

@app.post("/login", tags=["Autenticación"], response_model=schemas.Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db = Depends(get_db)
):
    # Buscamos al usuario en la tabla USERS
    user = crud.get_user_by_email(db, email=form_data.username)
    
    # Verificamos contraseña (user ahora es un diccionario/Row)
    if not user or not security.verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user["email"], "role": user["role"]},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --- RUTAS DE PRODUCTOS ---

@app.get("/products/", response_model=List[schemas.Product], tags=["Productos"])
def read_products(skip: int = 0, limit: int = 100, db = Depends(get_db)):
    """Lista productos directamente desde SQLite Cloud"""
    return crud.get_products(db, skip=skip, limit=limit)

@app.post("/products/", response_model=schemas.Product, tags=["Productos"])
def create_product(
    product: schemas.ProductCreate, 
    db = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Crea un producto validando que el usuario sea admin"""
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos de administrador")
    return crud.create_product(db, product)

# --- RUTAS DE CLIENTES ---

@app.get("/clients/", response_model=List[schemas.Client], tags=["Clientes"])
def read_clients(db = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.get_clients(db)

# --- ENDPOINT DE SALUD ---
@app.get("/", tags=["General"])
def health_check():
    return {"status": "online", "database": "SQLite Cloud Direct Connection"}