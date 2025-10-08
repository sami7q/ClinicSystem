# core/services/invoices_service.py
from datetime import datetime
from app.core.db import SessionLocal
from app.core.models import Invoice, Appointment

def create_invoice(appointment_id, amount, payment_method):
    """إنشاء فاتورة جديدة لموعد"""
    db = SessionLocal()
    try:
        appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

        if not appointment:
            print("❌ Appointment not found.")
            return None

        # تحقق إذا كان للموعد فاتورة مسبقاً
        if appointment.invoice:
            print(f"⚠️ Invoice already exists for appointment {appointment_id}.")
            return appointment.invoice

        invoice = Invoice(
            appointment_id=appointment_id,
            amount=amount,
            payment_method=payment_method,
            issued_at=datetime.utcnow()
        )
        db.add(invoice)
        db.commit()
        db.refresh(invoice)

        print(f"✅ Invoice created for appointment {appointment_id} — amount: ${amount}")
        return invoice
    except Exception as e:
        db.rollback()
        print(f"❌ Error creating invoice: {e}")
    finally:
        db.close()


def list_invoices():
    """عرض جميع الفواتير"""
    db = SessionLocal()
    try:
        return db.query(Invoice).all()
    finally:
        db.close()


def get_invoice_by_id(invoice_id):
    """عرض فاتورة معينة"""
    db = SessionLocal()
    try:
        return db.query(Invoice).filter(Invoice.id == invoice_id).first()
    finally:
        db.close()


def delete_invoice(invoice_id):
    """حذف فاتورة"""
    db = SessionLocal()
    try:
        invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
        if invoice:
            db.delete(invoice)
            db.commit()
            print(f"🗑️ Invoice {invoice.id} deleted successfully.")
        else:
            print("❌ Invoice not found.")
    finally:
        db.close()


def update_invoice(invoice_id, **kwargs):
    """تحديث بيانات الفاتورة"""
    db = SessionLocal()
    try:
        invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
        if not invoice:
            print("❌ Invoice not found.")
            return None

        for key, value in kwargs.items():
            if hasattr(invoice, key):
                setattr(invoice, key, value)

        db.commit()
        print(f"🔄 Invoice {invoice.id} updated successfully.")
        return invoice
    finally:
        db.close()
