from database import SessionLocal
from models.pawn import PawnItem

db = SessionLocal()

item = db.query(PawnItem).filter(PawnItem.id == 10).first()

if item:
    db.delete(item)
    db.commit()
