from fastapi import APIRouter ,status ,Response
from enum import Enum


router = APIRouter(prefix="/blog", tags=["blog"])


class typeblog(str, Enum):
    Mesal1 = 'Mesal1'
    Mesal2 = 'Mesal2'
    Mesal3 = 'Mesal3'


#خواندن همه بلاگ ها
@router.get('/all')
def get_all_blog():
    return {"message": "all blog"}
# تایپ بلاگ میخونیم فقط تایپ ها مشخص شده
@router.get('/blog/type/{type}',tags=['type'])
def get_type_blog(type:typeblog):
    return {"message": f"blog type {type}"}
# ایدی بلاگ رو میدیم برمیگردونه
@router.get('/{id}')
def get_blog(id: int):
    return {"message": f"blog {id}"}

#گرفتن پیچ و سایز پیج بلاگ
@router.get('/page',tags=['page'])
def get_page_blog(page:int,page_size:str):
    return {"message": f"{page=}--{page_size=}"}

# وارد کردن دو مقدار اجباری و دو مقدار اختیاری
@router.get('/{id}/comment/{comment_id}' , tags=['comment', ]
         ,description='comment')
def get_comment(id:int,comment_id:int , valid:bool=True,username:str=None):
    return {"message": f"comment {id} blog id {comment_id} {valid=} {username=}"}

# شرط گذاشتن برای که ارور یا مقدار با مقدار ما سازگار داشته باشد
@router.get('/Response/{id}' , status_code=status.HTTP_200_OK , tags=['Response'], summary="yessss")
def blog_id(id:int , responses:Response):
    if id > 5:
        responses.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "id bozorg tar az 5 hast"}
    return {"message": f"blog_id {id}"}

# دستور تگ برای گروه بندی  هست tag
# سامری هم برای توضیحات کوچیک هست summary
# برای توضیحات کامل هم باید  description