#Validacion de datos con Pydantic
import pydantic
from typing import Optional

# Base común (para evitar repetir código)
class ProductBase(pydantic.BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

# Esquema para CREAR (Lo que recibimos de Flutter)
class ProductCreate(ProductBase):
    #pendiente de agregar codigo
    pass

# Esquema para LEER (Lo que devolvemos a Flutter)
# Incluye el ID que genera la base de datos
class Product(ProductBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True # Permite leer desde el modelo de SQLAlchemy