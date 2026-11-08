from fastapi import APIRouter ,Query , Body,Path
from pydantic import BaseModel
from typing import Optional , List
from typing import Dict

router = APIRouter(prefix="/blog", tags=["post"])

class BlogModel(BaseModel):
    title: str
    comment: str
    nb_number: int
    published: Optional[bool]
    #برای دریافت لیست از کاربر
    tag: List[str]
    # برای گرفتن لیست پیشرفته
    metdata: Dict[str, str] = {'key1','value1'}


@router.post('/new')
def carate_blog(blog: BlogModel, id:int ,version:int=1):
    return {"message": "all post","data":blog,'id':id,'version':version}


#کار کردن با دستور هایی کوری برای هر بخش و مثالش رو یک بخش زده میشه

@router.post('/new/{id}/comment')
def crate_comment(id:int , blog:BlogModel ,id_comment:int =Query(None,
                                                                 title="title", #برای این بخش تام میزاریم
                                                                 description="description", # برای این بخش توضیحات میزاریم
                                                                 alias="alias", # برای این قسمت اسم اصلی متغییر نمایش نده
                                                                 deprecated=True #  اینم برای این نشون بدیم این دستور منسوخ شده یا خیر
                                                                 )):
    return {
        'blog':blog,
        'comment':id_comment,
        'id':id
    }

#Body Validator
#میتوان توضیحات دریافت کرد و محدودیت برای ان تایین کردن
@router.post('/new/{id}/Body')
def crate_Body_Validator(id:int ,
                         blog:BlogModel ,
                         id_comment:int =Query(None,
                                                title="title", #برای این بخش تام میزاریم
                                                description="description", # برای این بخش توضیحات میزاریم
                                                alias="alias", # برای این قسمت اسم اصلی متغییر نمایش نده
                                                deprecated=True #  اینم برای این نشون بدیم این دستور منسوخ شده یا خیر
                                                ),
                         content:str=Body(...,
                                          max_length=25, # بیشتر کارکتر میشه وارد کرد
                                          min_length=8, # کمترین کارکتر میشه وارد کرد
                                          pattern='^[A-Z].*' # باید اولش حروف بزرگ شروع بشه
                                          )
                         ):
    return {
        'blog':blog,
        'comment':id_comment,
        'id':id,
        'content':content
    }

# List  یا دریافت کردن چند استرینگ
@router.post('/new/{id}/List')
def crate_List(id:int ,
                         blog:BlogModel ,
                         id_comment:int =Query(None,
                                                title="title", #برای این بخش تام میزاریم
                                                description="description", # برای این بخش توضیحات میزاریم
                                                alias="alias", # برای این قسمت اسم اصلی متغییر نمایش نده
                                                deprecated=True #  اینم برای این نشون بدیم این دستور منسوخ شده یا خیر
                                                ),
                         content:str=Body(...,
                                          max_length=25, # بیشتر کارکتر میشه وارد کرد
                                          min_length=8, # کمترین کارکتر میشه وارد کرد
                                          pattern='^[A-Z].*' # باید اولش حروف بزرگ شروع بشه
                                          ),
                         v : Optional[List[str]]=Query(None)
                         ):
    return {
        'blog':blog,
        'comment':id_comment,
        'id':id,
        'content':content,
        'version': v,
    }
# روش جدید برای گرفتن عدد ها بزرگ تر و کوچیک تر
# gt = >
# ge = >=
# lt = <
# le = <=
@router.post('/new/{id}/int/{id_number}')
def crate_int(id:int ,
                         blog:BlogModel ,
                         title:int =Query(None,
                                                title="title", #برای این بخش تام میزاریم
                                                description="description", # برای این بخش توضیحات میزاریم
                                                alias="title", # برای این قسمت اسم اصلی متغییر نمایش نده
                                                deprecated=True #  اینم برای این نشون بدیم این دستور منسوخ شده یا خیر
                                                ),
                         content:str=Body(...,
                                          max_length=25, # بیشتر کارکتر میشه وارد کرد
                                          min_length=8, # کمترین کارکتر میشه وارد کرد
                                          pattern='^[A-Z].*' # باید اولش حروف بزرگ شروع بشه
                                          ),
                         v : Optional[List[str]]=Query(None),
                         id_number:int =Path(gt=5)
                         ):
    return {
        'blog':blog,
        'title':title,
        'id':id,
        'content':content,
        'version': v,
        'id_number': id_number
    }