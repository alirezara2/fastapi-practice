from urllib import request

from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from exceptions import EmailNotValid
#ساخت مدل که کاربر ریکویست که ارسال کرده رو با اطلاعات دیتابیس هم خوانی کند
def create_user(db:Session, request:UserBase):
    if "@" not in request.email:
        raise EmailNotValid('Email is not valid')
    user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),

    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#Read All User
def Read_All_Users(db:Session):
    return db.query(DbUser).all()

#Read User
def Read_User(id, db:Session):
    return db.query(DbUser).filter(DbUser.id == id).first()
#Read Username
def Read_Username(username, db:Session):
    return db.query(DbUser).filter(DbUser.username == username).first()


def Delete_User(id, db:Session):
    user = Read_User(id, db)
    db.delete(user)
    db.commit()
    return 'ok'

def Update_User(id, db:Session, request:UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password:Hash.bcrypt(request.password)

    })
    db.commit()
    return 'ok'