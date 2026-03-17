import sqlitecloud
from . import schemas

# --- OPERACIONES DE USUARIO (Para el Login) ---

def get_user_by_email(db, email: str):
    """Busca un usuario por email usando SQL puro"""
    query = "SELECT * FROM USERS WHERE email = ?"
    cursor = db.execute(query, (email,))
    # fetchone() devuelve un objeto Row que se comporta como diccionario
    return cursor.fetchone()

# --- OPERACIONES PARA PRODUCTOS ---

def get_products(db, skip: int = 0, limit: int = 100):
    """Lista productos con paginación"""
    query = "SELECT * FROM PRODUCTS LIMIT ? OFFSET ?"
    cursor = db.execute(query, (limit, skip))
    return cursor.fetchall()

def create_product(db, product: schemas.ProductCreate):
    """Inserta un producto y devuelve el registro creado"""
    query = """
        INSERT INTO PRODUCTS (sku, name, description, cost_price, sale_price, stock, tax_rate, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = (
        product.sku, 
        product.name, 
        product.description, 
        product.cost_price, 
        product.sale_price, 
        product.stock, 
        product.tax_rate, 
        1 if product.is_active else 0
    )
    
    cursor = db.execute(query, params)
    last_id = cursor.lastrowid # Obtenemos el ID generado en la nube
    
    # Recuperamos el producto recién creado para devolverlo al API
    cursor = db.execute("SELECT * FROM PRODUCTS WHERE id = ?", (last_id,))
    return cursor.fetchone()

# --- OPERACIONES PARA CLIENTES ---

def get_clients(db):
    """Obtiene todos los clientes"""
    query = "SELECT * FROM CLIENTS"
    cursor = db.execute(query)
    return cursor.fetchall()

def create_client(db, client: schemas.ClientCreate):
    """Registra un nuevo cliente"""
    query = """
        INSERT INTO CLIENTS (tax_id, name, email, phone, address)
        VALUES (?, ?, ?, ?, ?)
    """
    params = (client.tax_id, client.name, client.email, client.phone, client.address)
    
    cursor = db.execute(query, params)
    last_id = cursor.lastrowid
    
    cursor = db.execute("SELECT * FROM CLIENTS WHERE id = ?", (last_id,))
    return cursor.fetchone()