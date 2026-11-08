from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime ,timedelta
from jose import jwt, JWTError
from fastapi import Depends ,status
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi.exceptions import HTTPException
from db.db_user import Read_Username



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = 'fba012a2a0c9c3d884fdf15843f2aa438bac1b5e8527875ecd7187e3ce494158'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# data = {'sub' : username}
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ما با این فاکشن میتوانیم به راحتی به اطلاعات کاربر رو از سمت کروم بگیریم
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                          detail="Not found",
                          headers={"WWW-Authenticate": "Bearer"},)

    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = _dict.get('sub')
        if not username:
            raise error
    except JWTError:
        raise error

    user = Read_Username(username, db)
    return user
