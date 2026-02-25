#Conexion a base de datos
#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
import sqlitecloud

# Tu URI de conexión (Asegúrate de que los datos sean correctos)
# NOTA: En producción, usa variables de entorno para esto.
CONNECTION_STRING = "sqlitecloud://cptkvgrsvz.g2.sqlite.cloud:8860/InvoiceDB?apikey=xBTeNIW9cMwwUGLJkkHHVZ5a0DBx6O5uiB6r6jgD66k"

def get_db_connection():
    try:
        # Conectamos a la base de datos
        conn = sqlitecloud.connect(CONNECTION_STRING)    
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None


# URL DE LA BASE DE DATOS
# Para producción/Postgres: "postgresql://user:password@localhost/dbname"
#SQLALCHEMY_DATABASE_URL = "https://cptkvgrsvz.g2.sqlite.cloud:443?apikey=xBTeNIW9cMwwUGLJkkHHVZ5a0DBx6O5uiB6r6jgD66k"

# connect_args es necesario solo para SQLite
#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = declarative_base()

# Dependencia para obtener la sesión de BD en cada petición
#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()