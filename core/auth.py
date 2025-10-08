# core/auth.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from core.services.users_service import get_user_by_username

# إعدادات JWT
SECRET_KEY = "super-secret-key"  # 🔒 لاحقًا نستخدم env file
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

# تعريف نظام المصادقة
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# 🔑 إنشاء التوكن
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 🧾 التحقق من التوكن وإرجاع المستخدم الحالي
def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user

# ⚙️ نظام الصلاحيات حسب الدور (Roles)
def require_role(*allowed_roles):
    """
    يسمح فقط بالأدوار المحددة، مثال:
    current_user=Depends(require_role("admin", "doctor"))
    """
    def role_checker(current_user=Depends(verify_token)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied for role '{current_user.role}'",
            )
        return current_user
    return role_checker
