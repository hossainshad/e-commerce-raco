from app.database import Base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime,ForeignKey
from sqlalchemy.sql import func

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    name =  Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    stock = Column(Integer, nullable=False, default=0)
    status = Column(String, nullable=False, default="active") 
    category_id = Column(Integer,ForeignKey("categories.id"), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())