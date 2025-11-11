from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# مجلد القوالب
templates = Jinja2Templates(directory="templates")

# يمكنك لاحقًا إضافة مجلد static للصور و CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

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

# صفحة تسجيل الدخول
@app.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def login_post(request: Request, email: str = Form(...), password: str = Form(...)):
    if email == "admin@altema.com" and password == "12345":
        return RedirectResponse(url="/admin", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "بيانات الدخول غير صحيحة ❌"})

# صفحة الإدارة
@app.get("/admin", response_class=HTMLResponse)
async def admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# لتشغيل التطبيق محلياً
# uvicorn app:app --host 0.0.0.0 --port 10000
