from fastapi import APIRouter ,Query , Body,Path ,Depends
from pydantic import BaseModel
from typing import Optional , List
from typing import Dict
from db import db_article
from db.models import DbArticle
from schemas import ArticleBase ,ArticleDisplay ,UserBase
from db.database import get_db
from auth.auth2 import get_current_user


router = APIRouter(prefix="/Article", tags=["Article"])

# crate Article
@router.post('/' , response_model=ArticleDisplay)
def create_Article(Article:ArticleBase,db=Depends(get_db)):
    return db_article.Create_Article(db,Article)

#read All Article
@router.get('/' , response_model=List[ArticleDisplay])
def get_All_Article(db=Depends(get_db)):
    return db_article.get_All_Article(db)


#Read Article
@router.get('/{id}')
def get_by_Id_Article(id:int ,db=Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return {
        "data":db_article.get_Article(id,db),
        "username":current_user.username # با این قسمت میتوانیم دیتا که برمیگردونه رو تغییر بدیم محدودیت بزاریم

    }
