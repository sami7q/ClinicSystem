# app/api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.db import init_db

# 📦 Import Routers
from app.api.routers.patients import router as patients_router
from app.api.routers.doctors import router as doctors_router
from app.api.routers.appointments import router as appointments_router
from app.api.routers.invoices import router as invoices_router
from app.api.routers.users import router as users_router
# لاحقاً:
# from app.api.routers.users import router as users_router

# 🚀 إعداد التطبيق
app = FastAPI(
    title="ClinicSystem API",
    version="0.3.0",
    description="A backend API for managing clinic data including patients, doctors, appointments, invoices, and users.",
)

# 🌍 السماح لواجهة Flutter أثناء التطوير
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
    "http://localhost",
    "http://127.0.0.1",
    # لاحقًا أضف نطاق تطبيق الإنتاج
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧩 ربط الراوترات
app.include_router(patients_router)
app.include_router(doctors_router)
app.include_router(appointments_router)
app.include_router(invoices_router)
app.include_router(users_router)
# app.include_router(users_router)

# ⚙️ عند تشغيل السيرفر — تهيئة قاعدة البيانات تلقائيًا
@app.on_event("startup")
def on_startup():
    print("🚀 Initializing database...")
    init_db()

# 🔍 Health Check
@app.get("/", tags=["Health"])
def health():
    return {
        "status": "ok",
        "service": "ClinicSystem API",
        "version": "0.3.0",
    }
