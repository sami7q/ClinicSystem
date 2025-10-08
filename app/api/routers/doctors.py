# app/api/routers/doctors.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from core.services.doctors_service import (
    create_doctor,
    get_all_doctors,
    get_doctor_by_id,
    update_doctor,
    delete_doctor,
)
from app.api.schemas import DoctorCreate, DoctorOut

# ✅ هذا السطر هو المهم (هو ما يبحث عنه Uvicorn)
router = APIRouter(prefix="/doctors", tags=["Doctors"])

# 🩺 إضافة طبيب جديد
@router.post("/", response_model=DoctorOut, status_code=status.HTTP_201_CREATED)
def add_doctor(doctor_data: DoctorCreate):
    doctor = create_doctor(
        name=doctor_data.name,
        specialty=doctor_data.specialty,
        phone=doctor_data.phone,
        email=doctor_data.email,
    )
    if not doctor:
        raise HTTPException(status_code=400, detail="Failed to create doctor")
    return doctor

# 📋 عرض جميع الأطباء
@router.get("/", response_model=List[DoctorOut])
def list_doctors():
    return get_all_doctors()

# 🔍 عرض طبيب محدد
@router.get("/{doctor_id}", response_model=DoctorOut)
def get_doctor(doctor_id: int):
    doctor = get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

# 🛠️ تحديث بيانات الطبيب
@router.put("/{doctor_id}", response_model=DoctorOut)
def modify_doctor(doctor_id: int, doctor_data: DoctorCreate):
    updated = update_doctor(
        doctor_id,
        name=doctor_data.name,
        specialty=doctor_data.specialty,
        phone=doctor_data.phone,
        email=doctor_data.email,
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found or not updated")
    return updated

# ❌ حذف الطبيب
@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_doctor(doctor_id: int):
    deleted = delete_doctor(doctor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor deleted successfully"}
