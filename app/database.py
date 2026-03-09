from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tu cadena de conexión desde el dashboard de SQLite Cloud
SQLITE_CLOUD_URL = "sqlitecloud://cptkvgrsvz.g2.sqlite.cloud:8860/InvoiceDB?apikey=xBTeNIW9cMwwUGLJkkHHVZ5a0DBx6O5uiB6r6jgD66k"

engine = create_engine(SQLITE_CLOUD_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import sqlitecloud

# Tu URI de conexión (Asegúrate de que los datos sean correctos)
# NOTA: En producción, usa variables de entorno para esto.
#CONNECTION_STRING = "sqlitecloud://cptkvgrsvz.g2.sqlite.cloud:8860/InvoiceDB?apikey=xBTeNIW9cMwwUGLJkkHHVZ5a0DBx6O5uiB6r6jgD66k"

#def get_db_connection():
#    try:
#        # Conectamos a la base de datos
#        conn = sqlitecloud.connect(CONNECTION_STRING)    
#        return conn
#    except Exception as e:
#        print(f"Error de conexión: {e}")
#        return None