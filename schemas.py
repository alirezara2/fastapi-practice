from typing import List

from pydantic import BaseModel


#-***************-#-***************-
# بخش یوزیر
#-***************-#-***************-
#user
# ورودی که کاربر میخواد وارد کنه
class UserBase(BaseModel):
    username: str
    password: str
    email: str


# برای نمایش محدود در برگشت ریکویست
class UserDisplay(BaseModel):
    class show_Article_User(BaseModel):
        title: str
        content: str
        published: bool

        class Config:
            orm_mode = True

    username: str
    email: str
    articles: List[show_Article_User]
    class Config:
        orm_mode = True

#-***************-#-***************-
# بخش مقاله
#-***************-#-***************-
# ساختار دریافت مقاله
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator: int
# نمایش مقاله
class ArticleDisplay(BaseModel):
    #نمایش اطلاعات یوزیر در مقاله
    class UserInfo(BaseModel):
        username: str
        email: str

        class Config:
            orm_mode = True

    title : str
    content: str
    published: bool
    user : UserInfo

    class Config:
        orm_mode = True

#-***************-#-***************-