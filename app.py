from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

# من نحن
@app.route('/about')
def about():
    return render_template('about.html')

# الخدمات
@app.route('/services')
def services():
    return render_template('services.html')

# تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "admin@altema.com.sa" and password == "1234":
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="بيانات الدخول غير صحيحة")
    return render_template('login.html')

# صفحة الإدارة
@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
