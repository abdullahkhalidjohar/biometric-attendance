from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# صفحة من نحن
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# صفحة الخدمات
@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse("services.html", {"request": request})

# صفحة الاتصال
@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post("/contact", response_class=HTMLResponse)
async def send_message(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # (يمكن لاحقاً ربطها بإرسال بريد إلكتروني)
    success = "تم إرسال رسالتك بنجاح!"  
    return templates.TemplateResponse("contact.html", {"request": request, "success": success})

# تسجيل الدخول
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_user(request: Request, email: str = Form(...), password: str = Form(...)):
    if email == "admin@altema.com.sa" and password == "1234":
        return RedirectResponse(url="/admin", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "بيانات الدخول غير صحيحة"})

# لوحة المدير
@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})
