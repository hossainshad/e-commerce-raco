from sqlalchemy import Column, Integer, String,  DateTime,Boolean
from app.database import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_admin = Column(Boolean, default=False)
    is_active   = Column(Boolean, default=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
