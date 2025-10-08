from logging.config import fileConfig
import os
import sys
from sqlalchemy import engine_from_config, pool
from alembic import context

# ========= إعداد المسارات =========
# المسار الأساسي لمجلد المشروع (ClinicSystem)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# أضف المسار الجذري للمشروع
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# أضف أيضًا المسار الفرعي app/ حتى يتمكن Alembic من رؤية app/core
APP_DIR = os.path.join(BASE_DIR, 'app')
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

# ========= استيراد إعدادات المشروع =========
from app.core.config import settings
from app.core.db import Base

# ========= إعداد Alembic =========
config = context.config

# استخدم DATABASE_URL من ملف .env
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# تهيئة اللوجر (اختياري)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# الميتاداتا الخاصة بالموديلات (لإنشاء الجداول تلقائيًا)
target_metadata = Base.metadata


# ========= تشغيل الترحيلات =========
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# تحديد وضع التنفيذ
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
