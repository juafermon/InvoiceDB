from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# --- ESQUEMAS PARA CLIENTES ---
class ClientBase(BaseModel):
    tax_id: int # En tu models.py lo pusiste como Integer
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    # En tu models.py comentaste created_at, si lo habilitas en la BD, descoméntalo aquí:
    # created_at: Optional[datetime] = None 

    class Config:
        from_attributes = True

# --- ESQUEMAS PARA PRODUCTOS ---
class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    # Cambiados a str para coincidir con tu models.py
    cost_price: str = "0.0"
    sale_price: str = "0.0"
    stock: int = 0
    tax_rate: str = "16.0"

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

# --- ESQUEMA PARA TOKEN (Necesario para el Login) ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None