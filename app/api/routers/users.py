# app/api/routers/users.py
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from core.services.users_service import (
    create_user,
    get_user_by_username,
    authenticate,
)
from core.auth import create_access_token, verify_token, require_role
from app.api.schemas import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["Users"])


# 🧩 إنشاء مستخدم جديد (فقط المدير admin)
@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def add_user(user: UserCreate, current_user=Depends(require_role("admin"))):
    """
    إنشاء مستخدم جديد — يمكن فقط للمدير (admin) تنفيذ هذه العملية.
    """
    new_user = create_user(
        username=user.username,
        password=user.password,
        role=user.role,
    )
    if not new_user:
        raise HTTPException(status_code=400, detail="Failed to create user")
    return new_user


# 🔍 عرض مستخدم معين (يتطلب فقط توكن صالح)
@router.get("/{username}", response_model=UserOut)
def get_user(username: str, current_user=Depends(verify_token)):
    """
    عرض بيانات مستخدم محدد — متاح لأي مستخدم مسجل دخول.
    """
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 🔑 تسجيل الدخول (JWT + متوافق مع Swagger)
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    تسجيل الدخول باستخدام username + password.
    يعيد JWT Token صالح لمدة 24 ساعة.
    """
    user = authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": user.username})
    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.role,
        "username": user.username
    }
