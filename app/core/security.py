# core/security.py
from passlib.context import CryptContext

# 🔒 تهيئة سياق التشفير
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """تشفير كلمة المرور"""
    # تأكد ألا تتجاوز 72 بايت
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """التحقق من كلمة المرور"""
    return pwd_context.verify(plain_password, hashed_password)
