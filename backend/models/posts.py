from sqlalchemy import Column, String, Boolean, TIMESTAMP, Integer
from . import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
