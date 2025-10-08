# app/api/deps.py
from typing import Generator
from fastapi import Depends
from app.core.db import SessionLocal
from sqlalchemy.orm import Session

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
