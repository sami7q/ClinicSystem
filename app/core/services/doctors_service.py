# core/services/doctors_service.py
from app.core.db import SessionLocal
from app.core.models import Doctor

def create_doctor(name, specialty=None, phone=None, email=None):
    """إضافة طبيب جديد"""
    db = SessionLocal()
    try:
        doctor = Doctor(
            name=name,
            specialty=specialty,
            phone=phone,
            email=email
        )
        db.add(doctor)
        db.commit()
        db.refresh(doctor)
        print(f"✅ Doctor '{name}' added successfully.")
        return doctor
    except Exception as e:
        db.rollback()
        print(f"❌ Error adding doctor: {e}")
    finally:
        db.close()

def get_all_doctors():
    """عرض جميع الأطباء"""
    db = SessionLocal()
    try:
        return db.query(Doctor).all()
    finally:
        db.close()

def get_doctor_by_id(doctor_id):
    """عرض طبيب حسب ID"""
    db = SessionLocal()
    try:
        return db.query(Doctor).filter(Doctor.id == doctor_id).first()
    finally:
        db.close()

def update_doctor(doctor_id, **kwargs):
    """تحديث بيانات طبيب"""
    db = SessionLocal()
    try:
        doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
        if not doctor:
            print("❌ Doctor not found.")
            return None
        for k, v in kwargs.items():
            if hasattr(doctor, k):
                setattr(doctor, k, v)
        db.commit()
        print(f"🔄 Doctor '{doctor.name}' updated.")
        return doctor
    finally:
        db.close()

def delete_doctor(doctor_id):
    """حذف طبيب"""
    db = SessionLocal()
    try:
        doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
        if doctor:
            db.delete(doctor)
            db.commit()
            print(f"🗑️ Doctor '{doctor.name}' deleted.")
        else:
            print("❌ Doctor not found.")
    finally:
        db.close()
