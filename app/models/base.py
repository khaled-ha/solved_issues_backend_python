from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, TIMESTAMP

class Baseclass:
    created_at = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=datetime.now)


Base = declarative_base(cls=Baseclass)