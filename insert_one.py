from database import SessionLocal
from models.pawn import PawnItem1
from models.customer import Customer

#1. Create session(connect to DB)
db = SessionLocal()
#2. Create object
item = PawnItem1(
    date = '2025-12-30',
    vehicle_num = '59X1-0001',
    pawn_price = 3000000
)
item2 = PawnItem1(
    date = '2025-12-30',
    vehicle_num = '59X1-0002',
    pawn_price = 7000000
)

item3 = PawnItem1(
    date = '2025-12-30',
    vehicle_num = '59X1-0003',
    pawn_price = 3000000
)
item4 = PawnItem1(
    date = '2025-12-30',
    vehicle_num = '59X1-0004',
    pawn_price = 1000000
)

item5 = PawnItem1(
    date = '2025-12-30',
    vehicle_num = '59X1-0005',
    pawn_price = 2000000
)
item6 = PawnItem1(
    date = '2025-12-30',
    vehicle_num = '59X1-0006',
    pawn_price = 4000000
)



#3. Add to DB
db.add(item)
db.add(item2)
db.add(item3)
db.add(item4)
db.add(item5)
db.add(item6)

#4. commit to save to DB
db.commit()

print("Inserted ok!")

