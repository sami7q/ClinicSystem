from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.db import Base  # ✅ التعديل الصحيح هنا


# 🧑‍💼 جدول المستخدمين (للدخول إلى النظام)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default="admin")  # admin / doctor / receptionist
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role})>"


# 🩺 جدول الأطباء
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    specialty = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    appointments = relationship("Appointment", back_populates="doctor")

    def __repr__(self):
        return f"<Doctor(name={self.name}, specialty={self.specialty})>"


# 👨‍🦰 جدول المرضى
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    gender = Column(String(10))
    phone = Column(String(20))
    address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):
        return f"<Patient(name={self.name}, age={self.age})>"


# 📅 جدول المواعيد
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    date = Column(DateTime, nullable=False)
    reason = Column(Text)
    status = Column(String(20), default="scheduled")  # scheduled / done / cancelled
    created_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    invoice = relationship("Invoice", back_populates="appointment", uselist=False)

    def __repr__(self):
        return f"<Appointment(date={self.date}, status={self.status})>"


# 💰 جدول الفواتير
class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    amount = Column(Float, nullable=False)
    payment_method = Column(String(50))  # cash / card / transfer
    issued_at = Column(DateTime, default=datetime.utcnow)

    appointment = relationship("Appointment", back_populates="invoice")

    def __repr__(self):
        return f"<Invoice(amount={self.amount}, method={self.payment_method})>"


# 🚀 عند تشغيل الملف مباشرة، تُنشأ الجداول في قاعدة البيانات
# 🚀 لتوليد الجداول، نفّذ python3 -m app.core.db وليس هذا الملف
if __name__ == "__main__":
    print("ℹ️  Run 'python3 -m app.core.db' to initialize the database.")
