# core/services/patients_service.py
from app.core.db import SessionLocal
from app.core.models import Patient

def create_patient(name, age, gender=None, phone=None, address=None):
    """إضافة مريض جديد"""
    db = SessionLocal()
    try:
        patient = Patient(
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            address=address
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)
        print(f"✅ Patient '{name}' added successfully.")
        return patient
    except Exception as e:
        db.rollback()
        print(f"❌ Error adding patient: {e}")
    finally:
        db.close()


def get_all_patients():
    """عرض جميع المرضى"""
    db = SessionLocal()
    try:
        patients = db.query(Patient).all()
        return patients
    finally:
        db.close()


def get_patient_by_id(patient_id):
    """عرض مريض حسب ID"""
    db = SessionLocal()
    try:
        return db.query(Patient).filter(Patient.id == patient_id).first()
    finally:
        db.close()


def update_patient(patient_id, **kwargs):
    """تحديث بيانات مريض"""
    db = SessionLocal()
    try:
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if not patient:
            print("❌ Patient not found.")
            return None

        for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        db.commit()
        print(f"🔄 Patient '{patient.name}' updated.")
        return patient
    finally:
        db.close()


def delete_patient(patient_id):
    """حذف مريض"""
    db = SessionLocal()
    try:
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if patient:
            db.delete(patient)
            db.commit()
            print(f"🗑️ Patient '{patient.name}' deleted.")
        else:
            print("❌ Patient not found.")
    finally:
        db.close()
