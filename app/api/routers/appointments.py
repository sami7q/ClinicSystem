# app/api/routers/appointments.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.core.services.appointments_service import (
    create_appointment,
    list_appointments,
    update_appointment_status,
    delete_appointment,
)
from app.api.schemas import AppointmentCreate, AppointmentOut

# 📅 تعريف الراوتر
router = APIRouter(prefix="/appointments", tags=["Appointments"])

# ➕ إنشاء موعد جديد
@router.post("/", response_model=AppointmentOut, status_code=status.HTTP_201_CREATED)
def add_appointment(appointment: AppointmentCreate):
    created = create_appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        date=appointment.date,
        reason=appointment.reason,
    )
    if not created:
        raise HTTPException(status_code=400, detail="Failed to create appointment")
    return created

# 📋 عرض جميع المواعيد
@router.get("/", response_model=List[AppointmentOut])
def get_all_appointments():
    return list_appointments()

# 🔄 تحديث حالة الموعد
@router.put("/{appointment_id}")
def update_status(appointment_id: int, status_value: str):
    updated = update_appointment_status(appointment_id, new_status=status_value)
    if not updated:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": f"Status updated to {status_value}"}

# ❌ حذف الموعد
@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_appointment(appointment_id: int):
    deleted = delete_appointment(appointment_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted"}
