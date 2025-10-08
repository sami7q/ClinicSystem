# core/services/appointments_service.py
from datetime import datetime
from app.core.db import SessionLocal
from app.core.models import Appointment, Patient, Doctor

def create_appointment(patient_id, doctor_id, date, reason=None):
    """إضافة موعد جديد"""
    db = SessionLocal()
    try:
        # تحقق أن المريض والطبيب موجودان فعلاً
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

        if not patient:
            print("❌ Patient not found.")
            return
        if not doctor:
            print("❌ Doctor not found.")
            return

        appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            reason=reason,
            status="scheduled"
        )

        db.add(appointment)
        db.commit()
        db.refresh(appointment)
        print(f"✅ Appointment created for {patient.name} with {doctor.name} on {date}.")
        return appointment
    except Exception as e:
        db.rollback()
        print(f"❌ Error creating appointment: {e}")
    finally:
        db.close()


def list_appointments():
    """عرض كل المواعيد"""
    db = SessionLocal()
    try:
        return db.query(Appointment).all()
    finally:
        db.close()


def update_appointment_status(appointment_id, new_status):
    """تحديث حالة الموعد (scheduled/done/cancelled)"""
    db = SessionLocal()
    try:
        appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
        if not appointment:
            print("❌ Appointment not found.")
            return

        appointment.status = new_status
        db.commit()
        print(f"🔄 Appointment {appointment.id} status updated to '{new_status}'.")
    finally:
        db.close()


def delete_appointment(appointment_id):
    """حذف موعد"""
    db = SessionLocal()
    try:
        appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
        if appointment:
            db.delete(appointment)
            db.commit()
            print(f"🗑️ Appointment {appointment.id} deleted.")
        else:
            print("❌ Appointment not found.")
    finally:
        db.close()
