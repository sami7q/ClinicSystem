# 🏥 نظام إدارة العيادة الطبية - Clinic Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.s## 📦 المكتبات المطلوبة (req---

## 📚 شرح تفصيلي للملفات

### 🔥 الملفات الجديدة (FastAPI Layer)

### 🗂️ `app/api/main.py` ⭐ جديد!
**الوظيفة:** تطبيق FastAPI الرئيسي

**المكونات الرئيسية:**
- `app`: تطبيق FastAPI الرئيسي
- `CORSMiddleware`: تفعيل CORS للسماح بالطلبات من واجهات مختلفة
- `on_startup()`: تهيئة قاعدة البيانات عند بدء التشغيل
- `health()`: نقطة فحص صحة API

**المميزات:**
- ✅ CORS Support لـ React, Flutter, Vue, etc.
- ✅ تهيئة تلقائية لقاعدة البيانات
- ✅ ربط Routers تلقائياً
- ✅ توثيق تلقائي (Swagger UI)

**مثال التشغيل:**
```bash
uvicorn app.api.main:app --reload
```

---

### 🗂️ `app/api/schemas.py` ⭐ جديد!
**الوظيفة:** تعريف Pydantic Schemas للـ API

**الـ Schemas المتاحة:**

| Schema | الغرض | الحقول |
|--------|-------|--------|
| `UserCreate` | إنشاء مستخدم | username, password, role |
| `UserOut` | إخراج بيانات مستخدم | id, username, role, created_at |
| `DoctorCreate` | إنشاء طبيب | name, specialty, phone, email |
| `DoctorOut` | إخراج بيانات طبيب | id + جميع الحقول + created_at |
| `PatientCreate` | إنشاء مريض | name, age, gender, phone, address |
| `PatientOut` | إخراج بيانات مريض | id + جميع الحقول + created_at |
| `AppointmentCreate` | إنشاء موعد | patient_id, doctor_id, date, reason, status |
| `AppointmentOut` | إخراج بيانات موعد | id + جميع الحقول + created_at |
| `InvoiceCreate` | إنشاء فاتورة | appointment_id, amount, payment_method |
| `InvoiceOut` | إخراج بيانات فاتورة | id + جميع الحقول + issued_at |

**المميزات:**
- ✅ التحقق التلقائي من صحة البيانات
- ✅ تحويل تلقائي من/إلى SQLAlchemy Models
- ✅ توثيق تلقائي في Swagger
- ✅ دعم Optional Fields
- ✅ دعم Literal Types للقيم المحددة

---

### 🗂️ `app/api/deps.py` ⭐ جديد!
**الوظيفة:** Dependencies المشتركة للـ API

**الدوال:**
- `get_db()`: دالة Generator لإنشاء وإغلاق Database Session

**الاستخدام:**
```python
from fastapi import Depends
from app.api.deps import get_db
from sqlalchemy.orm import Session

@router.get("/")
def my_endpoint(db: Session = Depends(get_db)):
    # استخدام db هنا
    pass
```

**المميزات:**
- ✅ إدارة تلقائية لدورة حياة Session
- ✅ إغلاق تلقائي للـ Session بعد الطلب
- ✅ منع تسرب الذاكرة
- ✅ Thread-safe

---

### 🗂️ `app/api/routers/patients.py` ⭐ جديد!
**الوظيفة:** API Endpoints الخاصة بالمرضى

**الـ Endpoints المتاحة:**

| Method | Endpoint | الوصف | Response |
|--------|----------|-------|----------|
| POST | `/patients` | إنشاء مريض جديد | PatientOut (201) |
| GET | `/patients` | عرض جميع المرضى | List[PatientOut] |
| GET | `/patients/{id}` | عرض مريض محدد | PatientOut |
| PUT | `/patients/{id}` | تحديث مريض | PatientOut |
| DELETE | `/patients/{id}` | حذف مريض | 204 No Content |

**Query Parameters:**
- `q`: البحث في الأسماء
- `limit`: عدد النتائج (1-100، الافتراضي: 20)
- `offset`: تخطي عدد من النتائج (للـ Pagination)

**المميزات:**
- ✅ CRUD كامل للمرضى
- ✅ بحث بالاسم
- ✅ Pagination للنتائج الكبيرة
- ✅ معالجة أخطاء 404
- ✅ استجابات HTTP صحيحة

**مثال الاستخدام:**
```python
# GET /patients?q=أحمد&limit=10&offset=0
# Response: قائمة بـ 10 مرضى يحتوي اسمهم على "أحمد"
```

---

### 🗂️ `core/models.py`ents.txt)

المشروع يستخدم المكتبات التالية:

```
fastapi              # إطار عمل Web API الحديث
uvicorn[standard]    # ASGI Server عالي الأداء
PyJWT                # مصادقة JSON Web Tokens
python-multipart     # معالجة Form Data والملفات
SQLAlchemy           # ORM لإدارة قاعدة البيانات
passlib[bcrypt]      # تشفير كلمات المرور
```adge/License-Private-red)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)

**نظام شامل لإدارة العيادات الطبية بشكل احترافي ومنظم**

[المميزات](#-المميزات) • [التثبيت](#-التثبيت) • [الاستخدام](#-الاستخدام) • [الهيكل](#-هيكل-المشروع) • [المساهمة](#-المساهمة)

</div>

---

## 📋 نظرة عامة

نظام إدارة العيادة الطبية هو نظام متكامل مبني بلغة Python مع FastAPI لإدارة جميع عمليات العيادة بما في ذلك:
- 🌐 **RESTful API** كامل للتكامل مع أي واجهة (Web, Mobile, Desktop)
- 👥 إدارة المرضى والأطباء
- 📅 حجز وإدارة المواعيد
- 💰 إصدار الفواتير والمدفوعات
- 🔐 نظام المستخدمين والصلاحيات
- 📊 قاعدة بيانات محلية آمنة

---

## ✨ المميزات

### 🌐 **RESTful API (جديد!)**
- ✅ **FastAPI Framework** - أسرع وأحدث إطار عمل Python
- ✅ **Automatic Documentation** - توثيق تلقائي تفاعلي (Swagger UI)
- ✅ **CORS Support** - دعم CORS للتكامل مع واجهات مختلفة
- ✅ **Pydantic Schemas** - التحقق التلقائي من البيانات
- ✅ **RESTful Endpoints** - نقاط نهاية API احترافية
- ✅ **Async Support** - دعم العمليات غير المتزامنة
- ✅ **JWT Ready** - جاهز لإضافة المصادقة بـ JWT
- ✅ **Production Ready** - جاهز للإنتاج مع Uvicorn

### 🩺 **إدارة الأطباء**
- ✅ إضافة أطباء جدد مع تفاصيل كاملة (الاسم، التخصص، الهاتف، البريد)
- ✅ عرض قائمة جميع الأطباء
- ✅ تحديث بيانات الأطباء
- ✅ حذف الأطباء من النظام
- ✅ البحث عن طبيب معين

### 👥 **إدارة المرضى**
- ✅ تسجيل مرضى جدد (الاسم، العمر، الجنس، الهاتف، العنوان)
- ✅ عرض سجلات جميع المرضى عبر API
- ✅ تحديث معلومات المرضى عبر API
- ✅ حذف سجلات المرضى عبر API
- ✅ البحث والاستعلام عن المرضى مع Pagination
- ✅ API Endpoints: GET, POST, PUT, DELETE

### 📅 **إدارة المواعيد**
- ✅ حجز مواعيد للمرضى مع الأطباء
- ✅ تحديد تاريخ ووقت الموعد
- ✅ تسجيل سبب الزيارة
- ✅ تحديث حالة الموعد (محجوز / منتهي / ملغى)
- ✅ حذف المواعيد
- ✅ عرض جميع المواعيد

### 💰 **إدارة الفواتير**
- ✅ إصدار فواتير للمواعيد
- ✅ تحديد المبلغ وطريقة الدفع (نقدي / بطاقة / تحويل)
- ✅ منع تكرار الفواتير للموعد الواحد
- ✅ تحديث بيانات الفواتير
- ✅ حذف الفواتير
- ✅ عرض جميع الفواتير

### 🔐 **نظام الأمان**
- ✅ نظام المستخدمين مع صلاحيات متعددة
- ✅ أدوار المستخدمين (مدير / طبيب / موظف استقبال)
- ✅ تشفير كلمات المرور باستخدام Bcrypt
- ✅ نظام المصادقة (Authentication)
- ✅ دالة التحقق من كلمة المرور
- ✅ إنشاء حساب مدير افتراضي تلقائياً
- ✅ حماية من تكرار أسماء المستخدمين

### 📊 **قاعدة البيانات**
- ✅ قاعدة بيانات SQLite محلية
- ✅ استخدام SQLAlchemy ORM للأمان والمرونة
- ✅ علاقات بين الجداول (Foreign Keys)
- ✅ معالجة الأخطاء التلقائية

---

## 🛠️ التقنيات المستخدمة

| التقنية | الغرض | الإصدار |
|---------|-------|---------|
| **Python** | لغة البرمجة الأساسية | 3.12 |
| **FastAPI** | إطار عمل Web API الحديث | 0.100+ |
| **Uvicorn** | ASGI Server عالي الأداء | Latest |
| **Pydantic** | التحقق من البيانات والـ Schemas | Latest |
| **SQLAlchemy** | ORM لإدارة قاعدة البيانات | 2.x |
| **SQLite** | قاعدة البيانات | 3.x |
| **PyJWT** | مصادقة JWT | Latest |
| **Passlib** | تشفير كلمات المرور (Bcrypt) | Latest |
| **python-multipart** | معالجة Form Data | Latest |
| **Git** | نظام التحكم بالإصدارات | - |

---

## ⚡ البدء السريع (Quick Start)

```bash
# 1. استنساخ المشروع
git clone https://github.com/sami7q/ClinicSystem.git
cd ClinicSystem

# 2. إنشاء وتفعيل البيئة الافتراضية
python -m venv venv
venv\Scripts\activate  # Windows

# 3. تثبيت المكتبات
pip install -r requirements.txt

# 4. تهيئة النظام (قاعدة البيانات + مدير)
python tools/seed_admin.py

# 5. تشغيل API Server
uvicorn app.api.main:app --reload

# 6. افتح المتصفح
# API Documentation: http://127.0.0.1:8000/docs
# Alternative Docs: http://127.0.0.1:8000/redoc

# 7. بيانات الدخول الافتراضية
# Username: admin
# Password: admin123
```

**الآن النظام جاهز للاستخدام!** ✅

---

## 📦 التثبيت

### المتطلبات الأساسية
- Python 3.12 أو أحدث
- pip (مدير الحزم)
- Git

### خطوات التثبيت

```bash
# 1. استنساخ المشروع
git clone https://github.com/sami7q/ClinicSystem.git
cd ClinicSystem

# 2. إنشاء بيئة افتراضية
python -m venv venv

# 3. تفعيل البيئة الافتراضية
# على Windows:
venv\Scripts\activate
# على Linux/Mac:
source venv/bin/activate

# 4. تثبيت المكتبات المطلوبة
pip install -r requirements.txt

# 5. تهيئة قاعدة البيانات وإنشاء مدير النظام
python tools/seed_admin.py
```

---

## 🚀 الاستخدام

### تشغيل API Server

```bash
# تشغيل سيرفر التطوير مع Hot Reload
uvicorn app.api.main:app --reload

# أو تشغيل على منفذ محدد
uvicorn app.api.main:app --reload --port 8080

# تشغيل للإنتاج
uvicorn app.api.main:app --host 0.0.0.0 --port 8000
```

**🌐 الوصول للـ API:**
- API Health Check: http://127.0.0.1:8000/
- Swagger UI Documentation: http://127.0.0.1:8000/docs
- ReDoc Documentation: http://127.0.0.1:8000/redoc

---

### 📡 أمثلة API Endpoints

#### 🔹 إضافة مريض جديد (POST)
```bash
curl -X POST "http://127.0.0.1:8000/patients" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "أحمد محمد",
    "age": 35,
    "gender": "ذكر",
    "phone": "0501234567",
    "address": "الرياض، حي النخيل"
  }'
```

#### 🔹 عرض جميع المرضى (GET)
```bash
curl -X GET "http://127.0.0.1:8000/patients"
```

#### 🔹 البحث عن مرضى مع Pagination
```bash
curl -X GET "http://127.0.0.1:8000/patients?q=أحمد&limit=10&offset=0"
```

#### 🔹 عرض مريض محدد (GET)
```bash
curl -X GET "http://127.0.0.1:8000/patients/1"
```

#### 🔹 تحديث بيانات مريض (PUT)
```bash
curl -X PUT "http://127.0.0.1:8000/patients/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "أحمد محمد المحدث",
    "age": 36,
    "gender": "ذكر",
    "phone": "0501234567",
    "address": "جدة، حي الروضة"
  }'
```

#### 🔹 حذف مريض (DELETE)
```bash
curl -X DELETE "http://127.0.0.1:8000/patients/1"
```

---

### تهيئة قاعدة البيانات وإنشاء المدير

```bash
# تهيئة قاعدة البيانات وإنشاء حساب مدير افتراضي
python tools/seed_admin.py

# بيانات الدخول الافتراضية:
# Username: admin
# Password: admin123
```

### تسجيل الدخول والمصادقة

```python
from core.services.users_service import authenticate

# تسجيل دخول المستخدم
user = authenticate(username="admin", password="admin123")

if user:
    print(f"مرحباً {user.username}، دورك: {user.role}")
else:
    print("بيانات الدخول غير صحيحة")
```

### إنشاء مستخدم جديد

```python
from core.services.users_service import create_user

# إنشاء موظف استقبال
user = create_user(
    username="receptionist1",
    password="secure_password",
    role="receptionist"
)
```

---

### 💻 أمثلة استخدام Python Services (Legacy)

#### إضافة طبيب جديد

```python
from core.services.doctors_service import create_doctor

doctor = create_doctor(
    name="د. أحمد محمد",
    specialty="طب الأطفال",
    phone="0501234567",
    email="ahmad@clinic.com"
)
```

#### إضافة مريض جديد

```python
from core.services.patients_service import create_patient

patient = create_patient(
    name="محمد علي",
    age=35,
    gender="ذكر",
    phone="0509876543",
    address="الرياض، حي النخيل"
)
```

#### حجز موعد

```python
from datetime import datetime
from core.services.appointments_service import create_appointment

appointment = create_appointment(
    patient_id=1,
    doctor_id=1,
    date=datetime(2025, 10, 15, 10, 0),
    reason="فحص دوري"
)
```

#### إصدار فاتورة

```python
from core.services.invoices_service import create_invoice

invoice = create_invoice(
    appointment_id=1,
    amount=200.00,
    payment_method="cash"
)
```

---

## 📁 هيكل المشروع

```
ClinicSystem/
│
├── 📂 app/                          # التطبيق الرئيسي
│   ├── main.py                      # نقطة الدخول (قديم)
│   │
│   └── 📂 api/                      # ⭐ FastAPI Application (جديد!)
│       ├── __init__.py              # ملف التهيئة
│       ├── main.py                  # 🚀 FastAPI App الرئيسي
│       ├── deps.py                  # 🔧 Dependencies (Database Session)
│       ├── schemas.py               # 📋 Pydantic Schemas (جميع الـ Models)
│       │
│       └── 📂 routers/              # 🛣️ API Routers
│           ├── __init__.py          # ملف التهيئة
│           └── patients.py          # 👥 Patients API Endpoints
│
├── 📂 core/                         # المكونات الأساسية للنظام
│   ├── __init__.py                  # ملف التهيئة - يجعل المجلد Python Package
│   ├── db.py                        # ⚙️ إدارة قاعدة البيانات والاتصال
│   ├── models.py                    # 📊 تعريف الجداول والعلاقات (SQLAlchemy)
│   ├── security.py                  # 🔐 نظام الأمان والتشفير
│   ├── licensing.py                 # 📜 نظام الترخيص (قيد التطوير)
│   │
│   └── 📂 services/                 # خدمات الأعمال (Business Logic)
│       ├── __init__.py              # ملف التهيئة - يجعل المجلد Python Package
│       ├── users_service.py         # 👤 خدمات إدارة المستخدمين
│       ├── doctors_service.py       # 🩺 خدمات إدارة الأطباء
│       ├── patients_service.py      # 👥 خدمات إدارة المرضى
│       ├── appointments_service.py  # 📅 خدمات إدارة المواعيد
│       └── invoices_service.py      # 💰 خدمات إدارة الفواتير
│
├── 📂 data/                         # مجلد قاعدة البيانات
│   └── clinic.db                    # قاعدة البيانات SQLite
│
├── 📂 tools/                        # أدوات مساعدة
│   ├── __init__.py                  # ملف التهيئة - يجعل المجلد Python Package
│   └── seed_admin.py                # 🌱 إنشاء قاعدة البيانات والمدير الافتراضي
│
├── 📂 tests/                        # الاختبارات (قيد التطوير)
│
├── .gitignore                       # ملفات Git المستبعدة
├── requirements.txt                 # المكتبات المطلوبة
└── README.md                        # التوثيق (هذا الملف)
```

---

## � المكتبات المطلوبة (requirements.txt)

المشروع يستخدم المكتبات التالية:

```
PyQt5              # واجهة المستخدم الرسومية
SQLAlchemy         # ORM لإدارة قاعدة البيانات
passlib[bcrypt]    # تشفير كلمات المرور
fpdf2              # إنشاء ملفات PDF
python-dateutil    # معالجة التواريخ
```

**تثبيت جميع المكتبات:**
```bash
pip install -r requirements.txt
```

---

## �📚 شرح تفصيلي للملفات

### 🗂️ `core/db.py`
**الوظيفة:** إدارة الاتصال بقاعدة البيانات

**المكونات الرئيسية:**
- `engine`: محرك SQLAlchemy للاتصال بقاعدة البيانات
- `Base`: القاعدة الأساسية لجميع الـ Models
- `SessionLocal`: مصنع الجلسات (Sessions)
- `get_db()`: دالة لإنشاء جلسة قاعدة بيانات آمنة
- `init_db()`: تهيئة قاعدة البيانات وإنشاء الجداول

**الأداء:**
- ✅ إنشاء اتصال آمن بقاعدة البيانات
- ✅ إدارة دورة حياة الجلسات تلقائياً
- ✅ إنشاء جميع الجداول عند التشغيل الأول

---

### 🗂️ `core/models.py`
**الوظيفة:** تعريف جداول قاعدة البيانات والعلاقات بينها

**الجداول (Models):**

#### 1. 🧑‍💼 `User` - جدول المستخدمين
```python
- id: معرف فريد
- username: اسم المستخدم (فريد)
- password: كلمة المرور المشفرة
- role: دور المستخدم (admin/doctor/receptionist)
- created_at: تاريخ الإنشاء
```

#### 2. 🩺 `Doctor` - جدول الأطباء
```python
- id: معرف الطبيب
- name: اسم الطبيب
- specialty: التخصص
- phone: رقم الهاتف
- email: البريد الإلكتروني
- created_at: تاريخ التسجيل
- appointments: علاقة بجدول المواعيد
```

#### 3. 👥 `Patient` - جدول المرضى
```python
- id: معرف المريض
- name: اسم المريض
- age: العمر
- gender: الجنس
- phone: رقم الهاتف
- address: العنوان
- created_at: تاريخ التسجيل
- appointments: علاقة بجدول المواعيد
```

#### 4. 📅 `Appointment` - جدول المواعيد
```python
- id: معرف الموعد
- patient_id: معرف المريض (Foreign Key)
- doctor_id: معرف الطبيب (Foreign Key)
- date: تاريخ ووقت الموعد
- reason: سبب الزيارة
- status: حالة الموعد (scheduled/done/cancelled)
- created_at: تاريخ الحجز
- patient: علاقة بالمريض
- doctor: علاقة بالطبيب
- invoice: علاقة بالفاتورة
```

#### 5. 💰 `Invoice` - جدول الفواتير
```python
- id: معرف الفاتورة
- appointment_id: معرف الموعد (Foreign Key)
- amount: المبلغ
- payment_method: طريقة الدفع (cash/card/transfer)
- issued_at: تاريخ الإصدار
- appointment: علاقة بالموعد
```

**العلاقات:**
- ✅ علاقة واحد-لكثير بين Doctor و Appointments
- ✅ علاقة واحد-لكثير بين Patient و Appointments
- ✅ علاقة واحد-لواحد بين Appointment و Invoice

---

### 🗂️ `core/services/doctors_service.py`
**الوظيفة:** إدارة عمليات الأطباء (CRUD)

**الدوال المتاحة:**
| الدالة | الوصف | المعاملات |
|--------|-------|-----------|
| `create_doctor()` | إضافة طبيب جديد | name, specialty, phone, email |
| `get_all_doctors()` | عرض جميع الأطباء | - |
| `get_doctor_by_id()` | عرض طبيب معين | doctor_id |
| `update_doctor()` | تحديث بيانات طبيب | doctor_id, **kwargs |
| `delete_doctor()` | حذف طبيب | doctor_id |

**الأمان:**
- ✅ معالجة الأخطاء التلقائية
- ✅ Rollback عند حدوث أخطاء
- ✅ إغلاق الجلسات تلقائياً

---

### 🗂️ `core/services/patients_service.py`
**الوظيفة:** إدارة عمليات المرضى (CRUD)

**الدوال المتاحة:**
| الدالة | الوصف | المعاملات |
|--------|-------|-----------|
| `create_patient()` | إضافة مريض جديد | name, age, gender, phone, address |
| `get_all_patients()` | عرض جميع المرضى | - |
| `get_patient_by_id()` | عرض مريض معين | patient_id |
| `update_patient()` | تحديث بيانات مريض | patient_id, **kwargs |
| `delete_patient()` | حذف مريض | patient_id |

**المميزات:**
- ✅ تسجيل شامل للمعلومات الشخصية
- ✅ التحقق من وجود المريض قبل التحديث/الحذف
- ✅ رسائل توضيحية عند كل عملية

---

### 🗂️ `core/services/appointments_service.py`
**الوظيفة:** إدارة المواعيد بين المرضى والأطباء

**الدوال المتاحة:**
| الدالة | الوصف | المعاملات |
|--------|-------|-----------|
| `create_appointment()` | حجز موعد جديد | patient_id, doctor_id, date, reason |
| `list_appointments()` | عرض جميع المواعيد | - |
| `update_appointment_status()` | تحديث حالة الموعد | appointment_id, new_status |
| `delete_appointment()` | حذف موعد | appointment_id |

**التحقق التلقائي:**
- ✅ التحقق من وجود المريض قبل الحجز
- ✅ التحقق من وجود الطبيب قبل الحجز
- ✅ حالات الموعد: محجوز (scheduled) / منتهي (done) / ملغى (cancelled)

---

### 🗂️ `core/services/invoices_service.py`
**الوظيفة:** إدارة الفواتير والمدفوعات

**الدوال المتاحة:**
| الدالة | الوصف | المعاملات |
|--------|-------|-----------|
| `create_invoice()` | إنشاء فاتورة جديدة | appointment_id, amount, payment_method |
| `list_invoices()` | عرض جميع الفواتير | - |
| `get_invoice_by_id()` | عرض فاتورة معينة | invoice_id |
| `update_invoice()` | تحديث بيانات فاتورة | invoice_id, **kwargs |
| `delete_invoice()` | حذف فاتورة | invoice_id |

**الحماية:**
- ✅ منع إنشاء فاتورة مكررة لنفس الموعد
- ✅ التحقق من وجود الموعد قبل الإصدار
- ✅ دعم طرق دفع متعددة (نقدي، بطاقة، تحويل)

---

### 🗂️ `core/security.py`
**الوظيفة:** نظام التشفير والأمان

**المكونات الرئيسية:**
- `pwd_context`: سياق التشفير باستخدام Bcrypt
- `hash_password(password)`: تشفير كلمة المرور
- `verify_password(plain, hashed)`: التحقق من كلمة المرور

**الأداء:**
- ✅ تشفير قوي باستخدام Bcrypt (أحد أقوى خوارزميات التشفير)
- ✅ حماية من هجمات Rainbow Tables
- ✅ تحديد طول كلمة المرور (72 بايت كحد أقصى)
- ✅ آمن ضد هجمات Brute Force

**مثال الاستخدام:**
```python
from core.security import hash_password, verify_password

# تشفير كلمة المرور
hashed = hash_password("mypassword123")

# التحقق من كلمة المرور
is_valid = verify_password("mypassword123", hashed)
```

---

### 🗂️ `core/services/users_service.py`
**الوظيفة:** إدارة المستخدمين والمصادقة

**الدوال المتاحة:**
| الدالة | الوصف | المعاملات |
|--------|-------|-----------|
| `create_user()` | إنشاء مستخدم جديد | username, password, role |
| `get_user_by_username()` | البحث عن مستخدم | username |
| `authenticate()` | تسجيل الدخول والمصادقة | username, password |
| `ensure_admin()` | إنشاء مدير افتراضي | username, password |

**المميزات:**
- ✅ تشفير كلمات المرور تلقائياً
- ✅ منع تكرار أسماء المستخدمين
- ✅ معالجة الأخطاء والاستثناءات
- ✅ رسائل توضيحية لكل عملية
- ✅ نظام مصادقة آمن

**الأدوار المتاحة:**
- `admin`: مدير النظام (صلاحيات كاملة)
- `doctor`: طبيب (عرض المواعيد والبيانات)
- `receptionist`: موظف استقبال (إدارة المرضى والمواعيد)

---

### �️ `tools/seed_admin.py`
**الوظيفة:** تهيئة قاعدة البيانات وإنشاء مدير افتراضي

**المهام:**
1. ✅ تهيئة قاعدة البيانات وإنشاء جميع الجداول
2. ✅ إنشاء حساب مدير افتراضي (admin/admin123)
3. ✅ التحقق من عدم تكرار المدير

**طريقة التشغيل:**
```bash
python tools/seed_admin.py
```

**النتيجة:**
- ✅ قاعدة بيانات جاهزة مع جميع الجداول
- ✅ حساب مدير جاهز للاستخدام
- ✅ نظام جاهز للعمل مباشرة

---

### 🗂️ `core/security.py`
**الحالة:** ✅ مكتمل

**الوظائف المتاحة:**
- ✅ تشفير كلمات المرور (Password Hashing) باستخدام Bcrypt
- ✅ التحقق من كلمات المرور المشفرة
- ✅ حماية قوية ضد هجمات Brute Force
- 🔜 التحقق من الصلاحيات (Authorization)
- 🔜 إدارة الجلسات (Session Management)

---

### 🗂️ `core/licensing.py`
**الحالة:** 🔜 قيد التطوير

**الوظائف المخططة:**
- نظام ترخيص النظام
- التحقق من صلاحية الترخيص
- ربط مع معلومات الجهاز
- إدارة التراخيص المتعددة

---

### 🗂️ `app/main.py`
**الحالة:** 🔜 قيد التطوير

**الوظائف المخططة:**
- نقطة الدخول الرئيسية للتطبيق
- واجهة سطر الأوامر (CLI)
- أو واجهة رسومية (GUI)
- أو API REST

---

## 🏗️ معمارية النظام (Architecture)

### الطبقات (Layers)

```
┌─────────────────────────────────────────┐
│     Client Layer (Web/Mobile/API)      │
│  React, Flutter, Postman, curl, etc.   │
└─────────────────┬───────────────────────┘
                  │ HTTP/REST
┌─────────────────▼───────────────────────┐
│        API Layer (FastAPI)              │
│  • Routers (Endpoints)                  │
│  • Schemas (Pydantic Validation)        │
│  • Dependencies (DB Session)            │
│  • Middleware (CORS, etc.)              │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│    Business Logic Layer (Services)      │
│  • users_service.py                     │
│  • patients_service.py                  │
│  • doctors_service.py                   │
│  • appointments_service.py              │
│  • invoices_service.py                  │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│       Data Access Layer (ORM)           │
│  • SQLAlchemy Models                    │
│  • Relationships                        │
│  • Database Session Management          │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Database Layer (SQLite)         │
│  • clinic.db                            │
│  • Tables: users, doctors, patients,    │
│    appointments, invoices               │
└─────────────────────────────────────────┘
```

### تدفق الطلب (Request Flow)

```
1. Client → API Request (HTTP)
2. FastAPI Router → استقبال الطلب
3. Pydantic Schema → التحقق من البيانات
4. Dependency → إنشاء DB Session
5. Service Function → منطق الأعمال
6. SQLAlchemy ORM → الاستعلام من DB
7. Database → إرجاع البيانات
8. Service → معالجة البيانات
9. Pydantic Schema → تحويل للـ JSON
10. FastAPI → إرجاع Response (HTTP)
11. Client ← JSON Response
```

---

## 🔄 سير العمل (Workflow)

```mermaid
graph TD
    A[تسجيل دخول المستخدم] --> B{نوع المستخدم}
    B -->|مدير| C[إدارة الأطباء والمستخدمين]
    B -->|موظف استقبال| D[إدارة المرضى والمواعيد]
    B -->|طبيب| E[عرض المواعيد والفواتير]
    
    D --> F[تسجيل مريض جديد]
    F --> G[حجز موعد مع طبيب]
    G --> H[إتمام الموعد]
    H --> I[إصدار فاتورة]
    I --> J[تسجيل الدفع]
```

---

## 📊 قاعدة البيانات (Database Schema)

```
┌──────────────┐      ┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│     User     │      │   Doctor    │      │ Appointment  │      │   Patient   │
├──────────────┤      ├─────────────┤      ├──────────────┤      ├─────────────┤
│ id (PK)      │      │ id (PK)     │◄────┤ doctor_id FK │      │ id (PK)     │
│ username     │      │ name        │      │ patient_id FK├─────►│ name        │
│ password     │      │ specialty   │      │ date         │      │ age         │
│ role         │      │ phone       │      │ reason       │      │ gender      │
│ created_at   │      │ email       │      │ status       │      │ phone       │
└──────────────┘      │ created_at  │      │ created_at   │      │ address     │
                      └─────────────┘      └──────────────┘      │ created_at  │
                                                  │               └─────────────┘
                                                  │
                                                  ▼
                                           ┌──────────────┐
                                           │   Invoice    │
                                           ├──────────────┤
                                           │ id (PK)      │
                                           │appointment_id│
                                           │ amount       │
                                           │payment_method│
                                           │ issued_at    │
                                           └──────────────┘
```

---

## 🔒 الأمان والحماية

### التشفير
- ✅ **Bcrypt Hashing**: استخدام خوارزمية Bcrypt لتشفير كلمات المرور
- ✅ **Salt**: إضافة Salt عشوائي لكل كلمة مرور
- ✅ **Cost Factor**: معامل التكلفة يجعل التشفير مقاوم للهجمات

### حماية البيانات
- ✅ **SQL Injection Protection**: استخدام SQLAlchemy ORM يمنع هجمات SQL Injection
- ✅ **Password Length**: تحديد طول كلمة المرور (72 بايت كحد أقصى)
- ✅ **Unique Usernames**: منع تكرار أسماء المستخدمين
- ✅ **Error Handling**: معالجة شاملة للأخطاء والاستثناءات

### أفضل الممارسات
- ✅ **Session Management**: إغلاق جلسات قاعدة البيانات تلقائياً
- ✅ **Rollback on Error**: التراجع عن التغييرات عند حدوث أخطاء
- ✅ **Default Admin**: حساب مدير افتراضي للبدء السريع (يجب تغيير كلمة المرور)

### تحذيرات أمنية
⚠️ **مهم:** قم بتغيير كلمة المرور الافتراضية للمدير (admin123) فوراً بعد أول تسجيل دخول!

---

## 🧪 الاختبار

### اختبار API باستخدام Swagger UI

```bash
# 1. تشغيل السيرفر
uvicorn app.api.main:app --reload

# 2. افتح المتصفح
http://127.0.0.1:8000/docs

# 3. جرب الـ Endpoints مباشرة من الواجهة التفاعلية
```

### اختبار API باستخدام curl

```bash
# Health Check
curl http://127.0.0.1:8000/

# إضافة مريض
curl -X POST http://127.0.0.1:8000/patients \
  -H "Content-Type: application/json" \
  -d '{"name":"test","age":30}'

# عرض جميع المرضى
curl http://127.0.0.1:8000/patients

# بحث عن مرضى
curl "http://127.0.0.1:8000/patients?q=test&limit=5"
```

### اختبار وحدات الكود (Unit Tests)

```bash
# تشغيل الاختبارات (قيد التطوير)
python -m pytest tests/
```

---

## 🚀 خارطة الطريق (Roadmap)

### ✅ المكتمل
- [x] هيكل قاعدة البيانات
- [x] Models والعلاقات (SQLAlchemy)
- [x] نظام التشفير (Bcrypt)
- [x] نظام المصادقة (Authentication)
- [x] إدارة المستخدمين والصلاحيات
- [x] أداة إنشاء المدير الافتراضي
- [x] خدمات CRUD للأطباء
- [x] خدمات CRUD للمرضى
- [x] خدمات CRUD للمواعيد
- [x] خدمات CRUD للفواتير
- [x] خدمات CRUD للمستخدمين
- [x] ⭐ **FastAPI Framework**
- [x] ⭐ **RESTful API للمرضى**
- [x] ⭐ **Pydantic Schemas**
- [x] ⭐ **API Documentation (Swagger/ReDoc)**
- [x] ⭐ **CORS Middleware**
- [x] ⭐ **Pagination & Search**

### 🔄 قيد التطوير
- [ ] RESTful API للأطباء
- [ ] RESTful API للمواعيد
- [ ] RESTful API للفواتير
- [ ] نظام المصادقة JWT
- [ ] نظام الترخيص
- [ ] نظام التقارير (PDF)
- [ ] نظام الصلاحيات المتقدم

### 📋 المخطط
- [ ] واجهة ويب (React/Vue)
- [ ] تطبيق موبايل (Flutter/React Native)
- [ ] نظام النسخ الاحتياطي
- [ ] إشعارات SMS/Email
- [ ] لوحة تحكم إدارية
- [ ] نظام التقارير والإحصائيات المتقدمة
- [ ] دعم قواعد بيانات أخرى (PostgreSQL/MySQL)
- [ ] سجل العمليات (Audit Log)
- [ ] تصدير البيانات (Excel/CSV)
- [ ] WebSocket للإشعارات الفورية
- [ ] Docker Deployment

---

## 🤝 المساهمة

هذا مشروع خاص حالياً. للاستفسارات حول المساهمة، يرجى التواصل مع الفريق.

---

## 📄 الترخيص

© 2025 Clinic Management System. جميع الحقوق محفوظة.

هذا المشروع ملكية خاصة ولا يسمح باستخدامه أو توزيعه بدون إذن صريح.

---

## 📞 الدعم والتواصل

- **المطور:** sami7q
- **GitHub:** [github.com/sami7q/ClinicSystem](https://github.com/sami7q/ClinicSystem)
- **الحالة:** قيد التطوير النشط 🚀

---

## 🙏 شكر وتقدير

شكراً لاستخدامك نظام إدارة العيادة الطبية. نحن نعمل باستمرار على تحسين النظام وإضافة ميزات جديدة.

---

<div align="center">

**صُنع بـ ❤️ في المملكة العربية السعودية**

⭐ إذا أعجبك المشروع، لا تنسى النجمة على GitHub!

---

## 📝 سجل التحديثات (Changelog)

### 🚀 الإصدار الحالي (v0.3.0 - Major Update) - 2025-10-08

#### ✨ ميزات جديدة كبرى (Breaking Changes)
- 🎉 **إضافة FastAPI Framework** - تحول كامل إلى RESTful API
- 🎉 **Automatic API Documentation** - Swagger UI & ReDoc
- 🎉 **CORS Middleware** - دعم التكامل مع واجهات مختلفة
- 🎉 **Pydantic Schemas** - التحقق التلقائي من البيانات
- 🎉 **Patients API** - CRUD كامل للمرضى عبر API
- 🎉 **Pagination & Search** - بحث وترقيم احترافي
- 🎉 **API Health Check** - نقطة فحص صحة النظام

#### 📦 المكتبات الجديدة
- ✅ `fastapi` - إطار عمل Web API
- ✅ `uvicorn[standard]` - ASGI Server
- ✅ `PyJWT` - مصادقة JWT (جاهز للاستخدام)
- ✅ `python-multipart` - معالجة Form Data

#### 🗂️ ملفات جديدة
- ✅ `app/api/main.py` - تطبيق FastAPI الرئيسي
- ✅ `app/api/schemas.py` - جميع Pydantic Schemas
- ✅ `app/api/deps.py` - Dependencies المشتركة
- ✅ `app/api/routers/patients.py` - Patients API Router
- ✅ `app/api/__init__.py` & `app/api/routers/__init__.py`

#### 🔄 تحسينات
- ✅ تحديث `requirements.txt` بالكامل
- ✅ إعادة هيكلة المشروع لدعم API
- ✅ تحسين التوثيق في README

#### 📊 إحصائيات
- **عدد API Endpoints**: 5 (Patients)
- **عدد Pydantic Schemas**: 10
- **عدد المكتبات الجديدة**: 4
- **نسبة التغيير**: +300% في الوظائف

---

### الإصدار السابق (v0.2.0) - 2025-10-08
#### ✨ جديد
- ✅ إضافة نظام التشفير (Bcrypt) في `core/security.py`
- ✅ إضافة خدمات إدارة المستخدمين `core/services/users_service.py`
- ✅ إضافة أداة التهيئة `tools/seed_admin.py`
- ✅ إضافة ملفات `__init__.py` لجميع المجلدات
- ✅ تحديث `requirements.txt` بجميع المكتبات المطلوبة
- ✅ نظام المصادقة الكامل (Authentication)

#### 🔄 تحسينات
- ✅ تحديث `db.py` لدعم استيراد جميع Models بشكل صحيح
- ✅ إضافة نظام الأدوار (admin/doctor/receptionist)

### الإصدار الأول (v0.1.0)
- ✅ هيكل المشروع الأساسي
- ✅ Models وقاعدة البيانات
- ✅ خدمات CRUD الأساسية

</div>
