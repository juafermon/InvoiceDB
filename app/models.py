#Tablas de la BD con SQLAlchemy 
from sqalchemy import Boolean, Column, Float, Integer, String
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)  # En producción real usa DECIMAL para dinero
    stock = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)