# tools/seed_admin.py
import sys
import os

# ✅ اجعل مجلد المشروع الرئيسي (ClinicSystem) مرئي داخل sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from core.db import init_db
from core.services.users_service import ensure_admin

if __name__ == "__main__":
    print("🚀 Initializing database...")
    init_db()

    admin = ensure_admin(username="admin", password="admin123")

    if admin:
        print(f"✅ Admin ready: {admin.username}")
    else:
        print("ℹ️ Admin already exists or could not be created.")
