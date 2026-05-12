from database import Base
from sqlalchemy import Column, String, Integer

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key = True)
    name  = Column(String)
    phone = Column(String)
