from database import SessionLocal
from models.pawn import PawnItem1
from models.customer import Customer
from datetime import date

db = SessionLocal()

#create customer
#cust1 = Customer(name="Mr.Minh", phone="0789606414")
#cust2 = Customer(name="Mr.Van", phone="0972823112")
#cust3 = Customer(name="Mr.Tuan", phone="078961112")
#cust4 = Customer(name="Mr.Phu", phone="0972878787")


#db.add_all([cust1,cust2,cust3,cust4])
#db.commit()
#create pawn item
item1 = PawnItem1(
    date = date(205,12,16),
    vehicle_num = '59X1-0005',
    pawn_price = 3000000,
    customer_id=cust1.id,
)
item2 = PawnItem1(
    date = date(2026,2,6),
    vehicle_num = '59X1-0006',
    pawn_price = 7000000,
    customer_id=cust3.id
)
item3 = PawnItem1(
    date = date(2026,1,16),
    vehicle_num = '59X1-0007',
    pawn_price = 11000000,
    customer_id=cust4.id
)
item4 = PawnItem1(
    date = date(2026,4,16),
    vehicle_num = '59X1-0008',
    pawn_price = 21000000,
    customer_id=cust1.id
)
db.add_all([item1,item2,item3,item4])
db.commit()

print("Inserted with relationship!")
