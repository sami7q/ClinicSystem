# core/services/users_service.py
from sqlalchemy.exc import IntegrityError
from core.db import SessionLocal
from core.models import User
from core.security import hash_password, verify_password

def create_user(username: str, password: str, role: str = "admin"):
    """إنشاء مستخدم جديد مع تشفير كلمة المرور."""
    db = SessionLocal()
    try:
        user = User(username=username, password=hash_password(password), role=role)
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f"✅ User '{username}' created with role '{role}'.")
        return user
    except IntegrityError:
        db.rollback()
        print("❌ Username already exists.")
    except Exception as e:
        db.rollback()
        print(f"❌ Error creating user: {e}")
    finally:
        db.close()

def get_user_by_username(username: str):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.username == username).first()
    finally:
        db.close()

def authenticate(username: str, password: str):
    """يرجع المستخدم إذا كانت بيانات الدخول صحيحة، وإلا None."""
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and verify_password(password, user.password):
            print("✅ Authentication OK.")
            return user
        print("❌ Invalid username or password.")
        return None
    finally:
        db.close()

def ensure_admin(username: str = "admin", password: str = "admin123"):
    """إنشاء أدمن افتراضي إذا لم يكن موجود."""
    existing = get_user_by_username(username)
    if existing:
        print("ℹ️ Admin already exists.")
        return existing
    return create_user(username, password, role="admin")
