from enum import unique
from sqlalchemy import Column, String, Boolean, TIMESTAMP
from app.models.base import Base

class USer(Base):
    __tablename__ = 'users'
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

