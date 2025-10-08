# app/api/routers/invoices.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.core.services.invoices_service import (
    create_invoice,
    list_invoices,
    get_invoice_by_id,
    update_invoice,
    delete_invoice,
)
from app.api.schemas import InvoiceCreate, InvoiceOut

router = APIRouter(prefix="/invoices", tags=["Invoices"])

# ➕ إنشاء فاتورة جديدة
@router.post("/", response_model=InvoiceOut, status_code=status.HTTP_201_CREATED)
def add_invoice(invoice: InvoiceCreate):
    created = create_invoice(
        appointment_id=invoice.appointment_id,
        amount=invoice.amount,
        payment_method=invoice.payment_method,
    )
    if not created:
        raise HTTPException(status_code=400, detail="Failed to create invoice")
    return created

# 📋 عرض جميع الفواتير
@router.get("/", response_model=List[InvoiceOut])
def get_all_invoices():
    return list_invoices()

# 🔍 عرض فاتورة واحدة
@router.get("/{invoice_id}", response_model=InvoiceOut)
def get_invoice(invoice_id: int):
    invoice = get_invoice_by_id(invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

# ✏️ تحديث فاتورة
@router.put("/{invoice_id}")
def edit_invoice(invoice_id: int, data: InvoiceCreate):
    updated = update_invoice(invoice_id, **data.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice updated successfully"}

# ❌ حذف فاتورة
@router.delete("/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_invoice(invoice_id: int):
    deleted = delete_invoice(invoice_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice deleted"}
