from database import Base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String) #CREATE/UPDATE/DELETE
    table_name = Column(String)
    record_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)


