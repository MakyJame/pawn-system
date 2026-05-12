from database import SessionLocal
from models.pawn import PawnItem1
from sqlalchemy import text
db = SessionLocal()
db.execute(text("DROP TABLE pawn_items1"))
db.commit()
