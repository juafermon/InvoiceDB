from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from .database import Base

class Products(Base):
    __tablename__ = "PRODUCTS"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True) # Código de barras o ID interno
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    cost_price = Column(String, default="0.0") # valor del producto para la empresa
    sale_price = Column(String, default="0.0") # Valor del producto para el cliente
    stock = Column(Integer, default=0)
    tax_rate = Column(String, default="16.0") # Ejemplo: 16% de IVA
    is_active = Column(Boolean, default=True)

class Client(Base):
    __tablename__ = "CLIENTS"

    id = Column(Integer, primary_key=True, index=True)
    tax_id = Column(Integer, unique=True, index=True) # DNI, RUT, RFC
    name = Column(String)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    #created_at = Column(DateTime(timezone=True), server_default=func.now())

class Business_Info(Base):
    __tablename__ = "BUSINESS_INFO"

    id = Column(Integer, primary_key=True, index=True)
    tax_name = Column(String)
    tax_id = Column(String, unique=True, index=True) # RUT, RFC
    address = Column(String)
    logo_url = Column(String, nullable=True)
    currency = Column(String, nullable=True)

class Users(Base):
    __tablename__ = "USERS"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("BUSINESS_INFO.id"))
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

class Invoices(Base):
    __tablename__ = "INVOICES"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True)
    client_id = Column(Integer, ForeignKey("CLIENTS.id"))
    user_id = Column(Integer, ForeignKey("USERS.id"))
    created_at = Column(String)
    subtotal = Column(String)
    discount_total = Column(String)
    tax_total = Column(String)
    total_amount = Column(String)
    status = Column(String)

class Invoice_Items(Base):
    __tablename__ = "INVOICE_ITEMS"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("INVOICES.ID"))
    product_id = Column(Integer, ForeignKey("PRODUCTS.id"))
    quantity = Column(Integer)
    unit_price = Column(String)
    discount_amount = Column(String)
    tax_amount =  Column(String)

class Accounting_Transactions(Base):
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    category = Column(String)
    amount = Column(String)
    description = Column(String)
    related_invoice_id = Column(Integer, ForeignKey("INVOICES.ID"))
    created_at = Column(String)