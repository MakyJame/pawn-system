from database import SessionLocal
from models.pawn import PawnItem1

db = SessionLocal()

items = db.query(PawnItem1).filter(PawnItem1.is_deleted == True).all()

if items:
    for item in items:
        print("Item is deleted:", item.vehicle_num)
