from fastapi import APIRouter ,Response , Cookie , Header, Form
from typing import Optional,List
from fastapi.responses import HTMLResponse, PlainTextResponse
from sqlalchemy.util.cython import returns

router = APIRouter(prefix="/product", tags=["product"])

products = ["medad","pakon","jeled"]

# ارسال دیتا به صورت تکست به صفحه
@router.get("/")
def get_all_products():
    data = " ".join(products)
    response =  Response(content=data,media_type="text/plain")
    #response.headers["myheader"] = "test !" # ارسال هدر از سرور به کلاینت
    response.set_cookie(key="products",value="data")
    return response
    return response

@router.post("/create")
def create_product(data:str = Form(...)):
    products.append(data)
    return products




@router.get("/withheader")
def get_product(custom_header:Optional[List[str]] = Header(None) ,cookie:str = Cookie(None)):
    print(custom_header)
    return {'data':products , 'header':custom_header}# ارسال هدر از کلاینت به سرور



# ارسال دیتا به صورت فایل اچ تی ام ال
@router.get("/{id}",responses={
    404:{"content":{"text/plain":{'example':"product not found"}},
         "description":"product not found"},
    200:{"content":{"text/html":{'example':"<div> data </div>"}},
         "description":"html code data"},
})
def get_product(id:int):
    if id >len(products):
        text = "product not found"
        return PlainTextResponse(content=text,media_type="text/plain")
    data = products[id]
    return HTMLResponse(content=f"<div>{data}</div>",media_type="text/html")

