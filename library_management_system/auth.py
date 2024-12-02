from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from models import User
from logger import logger

SECRET_KEY = "6a7097b421b6ff6b5ce4c48a9d5f4a2c746db99b5d73884dc0f6941f91e0b835"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as err:
        logger.error(f"Error - {err}")
        

def get_password_hash(password):
    try:
        return pwd_context.hash(password)
    except Exception as err:
        logger.error(f"Error - {err}")

def create_access_token(data: dict):
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    except Exception as err:
        logger.error(f"Error - {err}")

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception as err:
        logger.error(f"Error - {err}")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        user = db.query(User).filter(User.email == payload.get("sub")).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except Exception as err:
        logger.error(f"Error - {err}")

def is_librarian(current_user: User = Depends(get_current_user)):
    try:
        if current_user.role != "librarian":
            raise HTTPException(status_code=403, detail="You are not authorized to perform this action.")
        return current_user
    except Exception as err:
        logger.error(f"Error - {err}")
