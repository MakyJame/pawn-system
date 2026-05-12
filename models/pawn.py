from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from database import Base

class PawnItem1(Base):
    __tablename__ = "pawn_items1"

    id = Column(Integer, primary_key = True, index= True)
    date = Column(Date)
    vehicle_num = Column(String,unique=True)
    pawn_price = Column(Integer)
    storage = Column(String)
    brand = Column(String)
    is_deleted=Column(Boolean, default=False)
    is_owner = Column(Boolean, default=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))
