# tools/seed_admin.py
import sys
import os

# ✅ اجعل مجلد المشروع الرئيسي (ClinicSystem) مرئي داخل sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app.core.services.users_service import ensure_admin

if __name__ == "__main__":
    print("🚀 Creating default admin user...")
    
    admin = ensure_admin(username="admin", password="admin123")

    if admin:
        print(f"✅ Admin ready: {admin.username}")
        print(f"🔐 Role: {admin.role}")
        print("\n📌 Use these credentials to login:")
        print("   Username: admin")
        print("   Password: admin123")
    else:
        print("ℹ️  Admin already exists or could not be created.")
