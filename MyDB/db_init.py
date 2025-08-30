from MyDB.db_main import Base, engine
from MyDB.db_models import User, Order, Product
from sqlalchemy import text

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized")

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Подключение успешно:", result.fetchone())
    except Exception as e:
        print("❌ Ошибка подключения к БД:", e)
