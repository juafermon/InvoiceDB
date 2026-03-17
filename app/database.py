import sqlitecloud

CONNECTION_STRING = "sqlitecloud://cptkvgrsvz.g2.sqlite.cloud:8860/InvoiceDB?apikey=xBTeNIW9cMwwUGLJkkHHVZ5a0DBx6O5uiB6r6jgD66k"

def get_db():
    """Función para obtener la conexión (usada como dependencia en FastAPI)"""
    conn = None
    try:
        conn = sqlitecloud.connect(CONNECTION_STRING)
        # Esto permite acceder a las columnas por nombre como si fuera un diccionario
        conn.row_factory = sqlitecloud.Row 
        yield conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        raise e
    finally:
        if conn:
            conn.close()