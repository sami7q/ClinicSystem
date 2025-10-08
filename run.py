#!/usr/bin/env python
"""
🚀 ClinicSystem - Quick Start Script
====================================
هذا السكريبت لتشغيل تطبيق ClinicSystem بسرعة

الاستخدام:
    python run.py

أو للتطوير مع إعادة التحميل التلقائي:
    python run.py --reload
"""

import sys
import subprocess

def main():
    reload_flag = "--reload" if "--reload" in sys.argv else ""
    
    print("=" * 60)
    print("🏥 ClinicSystem API Server")
    print("=" * 60)
    print("🚀 Starting server...")
    print("📡 URL: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    print("🔧 ReDoc: http://localhost:8000/redoc")
    print("=" * 60)
    
    cmd = ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
    
    if reload_flag:
        cmd.append("--reload")
        print("🔄 Auto-reload: ENABLED")
    else:
        print("🔄 Auto-reload: DISABLED")
    
    print("=" * 60)
    print()
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped gracefully.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
