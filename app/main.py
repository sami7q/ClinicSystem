# app/main.py
"""
نقطة الدخول الرئيسية لتطبيق ClinicSystem
يمكن تشغيل التطبيق بأحد الطرق التالية:

1. باستخدام uvicorn مباشرة:
   uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000

2. باستخدام هذا الملف:
   python -m app.main
"""

import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info" if settings.DEBUG else "warning",
    )
