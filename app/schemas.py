from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Esquema base para Clientes
class ClientBase(BaseModel):
    tax_id: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Esquema base para Productos
class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    cost_price: float
    sale_price: float
    stock: int
    tax_rate: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True