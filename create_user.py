from database import SessionLocal
from models.user import User
from security import hash_password

db = SessionLocal()

user1 = User(
    username="minhstaff",
    password=hash_password("123456"),
    role="staff"
)
user2 = User(
    username="minhdev",
    password=hash_password("123456"),
    role="admin"
)
db.add(user1)
db.add(user2)
db.commit()

print("Created user")
