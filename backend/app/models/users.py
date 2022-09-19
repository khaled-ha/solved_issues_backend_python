from sqlalchemy import Column, String, Boolean, TIMESTAMP, Integer
from backend.app.models.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, index= True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

