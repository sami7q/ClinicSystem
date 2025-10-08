# core/db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# المسار الكامل لملف قاعدة البيانات داخل مجلد data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "clinic.db")

# إنشاء المحرك (Engine)
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

# قاعدة النماذج
Base = declarative_base()

# جلسة للتعامل مع قاعدة البيانات
SessionLocal = sessionmaker(bind=engine)

def get_db():
    """تُرجع جلسة جديدة للتعامل مع قاعدة البيانات."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """تهيئة قاعدة البيانات وإنشاء الجداول إن لم تكن موجودة."""
    from core import models  # استيراد الجداول عند التهيئة فقط
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully at:", DB_PATH)

if __name__ == "__main__":
    init_db()

