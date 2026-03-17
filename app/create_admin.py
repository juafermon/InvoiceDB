from app.database import SessionLocal
from app.models import Users, Business_Info
from app.core import security

def create_initial_data():
    db = SessionLocal()
    try:
        # 1. Primero creamos una información de negocio base
        # (necesaria por la llave foránea en Users)
        business = db.query(Business_Info).first()
        if not business:
            business = Business_Info(
                tax_name="Mi Empresa Pro",
                tax_id="123456789-0",
                address="Calle Falsa 123",
                currency="COP"
            )
            db.add(business)
            db.commit()
            db.refresh(business)
            print("✅ Empresa de prueba creada.")

        # 2. Verificamos si el usuario ya existe
        admin_email = "admin@correo.com"
        user_exists = db.query(Users).filter(Users.email == admin_email).first()

        if not user_exists:
            # Encriptamos la contraseña "admin123"
            hashed_pw = security.get_password_hash("admin123")
            
            new_user = Users(
                business_id=business.id,
                username="admin",
                email=admin_email,
                password_hash=hashed_pw,
                role="admin",
                is_active=True
            )
            db.add(new_user)
            db.commit()
            print(f"🚀 Usuario creado con éxito.")
            print(f"📧 Email: {admin_email}")
            print(f"🔑 Password: admin123")
        else:
            print("ℹ️ El usuario administrador ya existe.")

    except Exception as e:
        print(f"❌ Error al crear el usuario: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_initial_data()