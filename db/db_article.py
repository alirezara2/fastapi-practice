from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle
from fastapi.exceptions import HTTPException
from fastapi import status

def Create_Article(db: Session, request:ArticleBase):
    article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


#get All Article
def get_All_Article(db:Session):
    return db.query(DbArticle).all()

#get Article
def get_Article(id, db:Session):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Article {id} not found")
    return article
