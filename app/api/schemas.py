# app/api/schemas.py
"""
📘 Schemas Layer — Pydantic Models for FastAPI
تُستخدم هذه الطبقة لتعريف هياكل البيانات (المدخلات والمخرجات)
الخاصة بالـ API لضمان تحقق الأنواع والأمان.
"""

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Literal

# ==============================
# ⚙️ الإعداد العام للنماذج
# ==============================
class ORMBase(BaseModel):
    """Base model configuration to allow SQLAlchemy ORM conversion."""
    class Config:
        from_attributes = True


# ==============================
# 👤 Users
# ==============================
class UserBase(ORMBase):
    username: str

class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=72)
    role: Literal["admin", "doctor", "receptionist"] = "admin"

class UserOut(UserBase):
    id: int
    role: str
    created_at: datetime


# ==============================
# 🩺 Doctors
# ==============================
class DoctorBase(ORMBase):
    name: str
    specialty: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class DoctorCreate(DoctorBase):
    pass

class DoctorOut(DoctorBase):
    id: int
    created_at: datetime


# ==============================
# 👥 Patients
# ==============================
class PatientBase(ORMBase):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class PatientOut(PatientBase):
    id: int
    created_at: datetime


# ==============================
# 📅 Appointments
# ==============================
class AppointmentBase(ORMBase):
    patient_id: int
    doctor_id: int
    date: datetime
    reason: Optional[str] = None
    status: Literal["scheduled", "done", "cancelled"] = "scheduled"

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentOut(AppointmentBase):
    id: int
    created_at: datetime


# ==============================
# 💰 Invoices
# ==============================
class InvoiceBase(ORMBase):
    appointment_id: int
    amount: float
    payment_method: Optional[str] = None  # cash / card / transfer

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceOut(InvoiceBase):
    id: int
    issued_at: datetime
