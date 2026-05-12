from database import SessionLocal
from models.pawn import PawnItem1

db = SessionLocal()

items = db.query(PawnItem1).filter(PawnItem1.pawn_price < 4000000).all()

if items:
    for item in items:
        item.is_deleted = True;
    db.commit()
    print("Deleted")
