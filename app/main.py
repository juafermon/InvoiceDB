from fastapi import FastAPI
from .database import engine, Base

# Crea las tablas automáticamente basado en nuestros modelos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Facturación API",
    description="Backend para App Web, Mobile y Desktop",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "Online", "message": "Servidor de Facturación funcionando"}