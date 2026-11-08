from fastapi import APIRouter ,Query , Body,Path ,Depends
from pydantic import BaseModel
from typing import Optional , List
from typing import Dict
from db import db_user
from schemas import UserBase ,UserDisplay
from db.database import get_db

router = APIRouter(prefix="/user", tags=["user"])

# crate user
@router.post('/' , response_model=UserDisplay)
def create_user(user:UserBase,db=Depends(get_db)):
    return db_user.create_user(db,user)


#read All User
@router.get('/' , response_model=List[UserDisplay])
def Create_All_Users(db=Depends(get_db)):
    return db_user.Read_All_Users(db)


#Read User
@router.get('/{id}' , response_model=UserDisplay)
def Create_User(id:int ,db=Depends(get_db)):
    return db_user.Read_User(id,db)

#delete User
@router.get('/Delete/{id}')
def Delete_User(id:int ,db=Depends(get_db)):
    return db_user.Delete_User(id,db)

#Update User
@router.post('/Update/{id}')
def Update_User(id:int ,user:UserBase,db=Depends(get_db)):
    return db_user.Update_User(id, db, user)
