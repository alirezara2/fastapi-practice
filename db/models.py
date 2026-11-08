from sqlalchemy.orm import relationship

from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class DbUser(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    articles  = relationship('DbArticle', back_populates='user')

class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)

    # این قسمت ایدی کاربری که این مقاله رو نوشته
    user_id = Column(Integer, ForeignKey('user.id'))
    # ارتباط گرفتن بین جدول یوزیر و مقاله
    user = relationship('DbUser', back_populates='articles')