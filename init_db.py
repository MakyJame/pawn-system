from database import engine, Base
import models.pawn
import models.customer
import models.user
import models.log

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Tables created!")
