from fastapi import FastAPI, Depends, APIRouter ,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db import models
from db.database import get_db
from fastapi.exceptions import HTTPException
from db.hash import Hash
from auth import auth2

router = APIRouter(tags=["Authentication"])



@router.post("/token")
def get_token(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

    access_token = auth2.create_access_token(data={"sub": request.username})

    return {"access_token": access_token, "token_type": "bearer", "id": user.id}