from fastapi.requests import Request
from fastapi import FastAPI ,status
from starlette.responses import JSONResponse
from exceptions import EmailNotValid
from router import blog_get
from router import blog_post
from router import user
from router import Article
from router import product
from router import file
from db import models
from db.database import engine
from auth import authentication

from fastapi.staticfiles import StaticFiles #برای نمایش دایرکتوری فایل ها

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(Article.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(file.router)

models.Base.metadata.create_all(engine)

#صفحه اصلی
@app.get("/")
def hello():
    return "hello world"
@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request , exc: EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)

# بخش نمایش فولدر فایل
app.mount('/files',StaticFiles(directory='files'),name='files')