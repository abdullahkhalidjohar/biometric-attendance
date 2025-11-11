from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# إنشاء تطبيق FastAPI
app = FastAPI()

# ربط مجلد القوالب
templates = Jinja2Templates(directory="templates")

# يمكنك إضافة مجلد للملفات الثابتة مثل الصور أو CSS لاحقًا إن أردت
# app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ صفحة "من نحن"
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# ✅ صفحة "الخدمات"
@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse("services.html", {"request": request})

# ✅ صفحة تسجيل الدخول (GET)
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# ✅ معالجة تسجيل الدخول (POST)
@app.post("/login")
async def login_user(request: Request, email: str = Form(...), password: str = Form(...)):
    # مثال بسيط لتسجيل الدخول (ممكن تطويره لاحقًا بقاعدة بيانات)
    if email == "admin@altema.com.sa" and password == "1234":
        response = RedirectResponse(url="/admin", status_code=303)
        return response
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "بيانات الدخول غير صحيحة"
        })

# ✅ لوحة المدير
@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# ✅ صفحة الخطأ 404 (اختياري)
@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "error": "الصفحة غير موجودة"},
        status_code=404
    )

# ✅ تشغيل التطبيق محليًا
# للأجهزة المحلية فقط، لا تستخدم هذا في Render
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
