from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.pawn import PawnItem1
from models.customer import Customer
from models.user import User
from security import verify_password, create_token, get_current_user, require_admin
from datetime import date
from logger import create_log

app = FastAPI()

#dependency lay DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API pawn running"}

@app.post("/customer")
def create_customer(
    name: str,
    phone: str,
    db: Session = Depends(get_db)
):
    customer = Customer(
        name=name,
        phone=phone
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer

@app.post("/pawn")
def create_pawn(
        date: date,
        vehicle_num: str,
        pawn_price: int,
        storage: str,
        brand: str,
        is_owner: bool,
        customer_id: int,
        db: Session = Depends(get_db),
        user=Depends(get_current_user)

):
    item = PawnItem1(
        date=date,
        vehicle_num=vehicle_num,
        pawn_price=pawn_price,
        storage=storage,
        brand=brand,
        is_owner=is_owner,
        customer_id=customer_id
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    create_log(
        db,
        user_id=user["user_id"],
        action="CREATE",
        table_name="pawn_items1",
        record_id=item.id
    )
    db.commit()

    return item

@app.get("/pawn")
def get_pawns(
        db: Session = Depends(get_db),
        user = Depends(require_admin)
        ):
    items = db.query(PawnItem1).filter(PawnItem1.is_deleted==False).all()
    return items

@app.put("/pawn/{item_id}")
def update_pawn(
        item_id: int, date: date, pawn_price: int, storage: str, brand: str, is_owner: bool,
        db: Session = Depends(get_db),
        user = Depends(get_current_user)
):
    item = db.query(PawnItem1).filter(PawnItem1.id == item_id).first()

    if not item:
        return {"error": "Not found"}
        
    item.date=date
    item.pawn_price=pawn_price
    item.storage=storage
    item.brand=brand
    item.is_owner=is_owner
    
    db.commit()

    create_log(
        db,
        user_id=user["user_id"],
        action="UPDATE",
        table_name="pawn_item1",
        record_id=item_id
    )
    db.commit()
    return {"status": "updated"}

@app.delete("/pawn/{item_id}")
def delete_pawn(item_id: int, user = Depends(require_admin), db: Session = Depends(get_db)):
    item = db.query(PawnItem1).filter(PawnItem1.id == item_id).first()

    if not item:
        return {"error": "Not found"}

    item.is_deleted = True
    db.commit()

    return {"status":"deleted"}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Wrong password")

    token = create_token({
        "user_id": user.id,
        "role": user.role
    })

    return {"access_token": token}
