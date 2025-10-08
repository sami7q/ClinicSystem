# app/api/routers/patients.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.api.schemas import PatientCreate, PatientOut
from app.api.deps import get_db
from core.models import Patient

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("", response_model=PatientOut, status_code=201)
def create_patient_api(payload: PatientCreate, db: Session = Depends(get_db)):
    patient = Patient(**payload.model_dump())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@router.get("", response_model=List[PatientOut])
def list_patients_api(
    db: Session = Depends(get_db),
    q: str | None = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    query = db.query(Patient)
    if q:
        like = f"%{q}%"
        query = query.filter(Patient.name.ilike(like))
    items = query.order_by(Patient.id.desc()).limit(limit).offset(offset).all()
    return items

@router.get("/{patient_id}", response_model=PatientOut)
def get_patient_api(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put("/{patient_id}", response_model=PatientOut)
def update_patient_api(patient_id: int, payload: PatientCreate, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    for k, v in payload.model_dump().items():
        setattr(patient, k, v)
    db.commit()
    db.refresh(patient)
    return patient

@router.delete("/{patient_id}", status_code=204)
def delete_patient_api(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return
