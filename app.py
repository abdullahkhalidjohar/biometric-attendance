from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

# صفحة من نحن
@app.route('/about')
def about():
    return render_template('about.html')

# صفحة الخدمات
@app.route('/services')
def services():
    return render_template('services.html')

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # تحقق تجريبي
        if email == "admin@altema.com" and password == "12345":
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="بيانات الدخول غير صحيحة ❌")
    return render_template('login.html')

# صفحة الإدارة
@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
