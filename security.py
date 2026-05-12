from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

# 🔐 hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# 🔑 JWT config
SECRET_KEY = "secret123"   # ❗ sau này nên dùng env
ALGORITHM = "HS256"

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=2)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 🔒 protect API
security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        print("TOKEN: ",token.credentials) #debug
        payload = jwt.decode(
            token.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        print("PAYLOAD:", payload) #debug
        return payload
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=403, detail="Invalid token")

def require_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise Exception("No permission")
    return user
