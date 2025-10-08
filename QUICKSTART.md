# 🚀 دليل التشغيل السريع - ClinicSystem

## ⚡ البدء السريع

### 1️⃣ تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### 2️⃣ إعداد PostgreSQL
```sql
-- افتح PostgreSQL وقم بتنفيذ:
CREATE DATABASE clinicsystem;
CREATE USER clinicsys WITH PASSWORD 'SAme115599';
GRANT ALL PRIVILEGES ON DATABASE clinicsystem TO clinicsys;
```

### 3️⃣ إنشاء الجداول
```bash
alembic upgrade head
```

### 4️⃣ إنشاء المستخدم الإداري
```bash
python tools/seed_admin.py
```

### 5️⃣ تشغيل السيرفر
```bash
python run.py --reload
```

---

## 🔗 الروابط المهمة

- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/

---

## 🔑 بيانات الدخول الافتراضية

```
Username: admin
Password: admin123
```

---

## 📝 ملاحظات

- تأكد من تشغيل PostgreSQL قبل البدء
- يمكنك تعديل `.env` لتغيير الإعدادات
- للمزيد من المعلومات، راجع `FIXES_REPORT.md`
