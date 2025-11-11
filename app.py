from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# نربط المجلد الخاص بالقوالب
templates = Jinja2Templates(directory="templates")

# الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# صفحة تسجيل الدخول
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# معالجة بيانات تسجيل الدخول
@app.post("/login")
async def login_user(request: Request, email: str = Form(...), password: str = Form(...)):
    # تسجيل دخول بسيط كمثال (يتم تطويره لاحقًا مع قاعدة بيانات)
    if email == "admin@altema.com.sa" and password == "1234":
        response = RedirectResponse(url="/admin", status_code=303)
        return response
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "بيانات الدخول غير صحيحة"})

# لوحة المدير
@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})
