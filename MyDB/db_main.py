from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from contextlib import contextmanager

load_dotenv()

DB_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

#функция которая дает сессию к БД, чтобы закинуть ее в with блок. когда этот блок закончится где то выполняться,
# то сессия закроется. что то типа утилки (удобная вещь)
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()