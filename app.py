from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # لتشفير الجلسات

# الصفحة الرئيسية
@app.route("/")
def index():
    return render_template("index.html")

# صفحة تسجيل الدخول
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # تحقق بسيط مؤقت (يمكن تطويره لاحقاً مع قاعدة بيانات)
        if email == "admin@altema.com.sa" and password == "123456":
            flash("تم تسجيل الدخول بنجاح ✅", "success")
            return redirect(url_for("index"))
        else:
            flash("البريد أو كلمة المرور غير صحيحة ❌", "danger")

    return render_template("login.html")

# API لتسجيل الدخول عبر الباركود
@app.route("/api/login/barcode", methods=["POST"])
def login_barcode():
    data = request.get_json()
    barcode = data.get("barcode")

    if barcode == "EMP-2025":
        return jsonify({"status": "success", "message": "تم تسجيل الدخول عبر الباركود ✅"})
    else:
        return jsonify({"status": "error", "message": "رمز غير صالح ❌"}), 401


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
