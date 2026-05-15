from database import SessionLocal
from models.pawn import PawnItem1
from models.customer import Customer
from datetime import date

db = SessionLocal()

#create customer
cust1 = Customer(name="Mr.Minh", phone="0789606414")
cust2 = Customer(name="Mr.Van", phone="0972823112")
cust3 = Customer(name="Mr.Tuan", phone="078961112")
cust4 = Customer(name="Mr.Phu", phone="0972878787")


db.add_all([cust1,cust2,cust3,cust4])
db.commit()
#create pawn item
item1 = PawnItem1(
    date = date(2025,12,16),
    vehicle_num = '59X1-0001',
    pawn_price = 3000000,
    storage = "A8-N1",
    brand = "waveA",
    is_owner = True,
    customer_id=cust1.id,
)
item2 = PawnItem1(
    date = date(2026,2,26),
    vehicle_num = '59X1-0002',
    pawn_price = 2000000,
    storage = "A8-N2",
    brand = "waveTQ",
    is_owner = False,
    customer_id=cust2.id,
)
item3 = PawnItem1(
    date = date(2026,2,1),
    vehicle_num = '59X1-0003',
    pawn_price =13000000,
    storage = "A8-N3",
    brand = "AB",
    is_owner = True,
    customer_id=cust4.id,
)
item4 = PawnItem1(
    date = date(2025,2,16),
    vehicle_num = '59X1-0004',
    pawn_price = 23000000,
    storage = "A8-K1",
    brand = "winnerX",
    is_owner = True,
    customer_id=cust2.id,
)

db.add_all([item1,item2,item3,item4])
db.commit()

print("Inserted with relationship!")
