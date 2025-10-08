# app/core/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# إنشاء المحرك باستخدام DATABASE_URL من .env (PostgreSQL)
engine = create_engine(settings.DATABASE_URL, echo=False)

# تعريف Base لجميع الموديلات
Base = declarative_base()

# إنشاء SessionLocal
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    """تُرجع جلسة جديدة للتعامل مع قاعدة البيانات."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ضروري حتى Alembic يرى الموديلات
from app.core import models  # noqa: F401
