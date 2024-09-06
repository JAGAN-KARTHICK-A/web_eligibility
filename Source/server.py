from flask import Flask, render_template, redirect, request, make_response
from utils import DB

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "GET":
        return render_template("registration.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        phone = request.form.get("number")
        address = request.form.get("address")
        db = DB()
        db.makeConnection()
        res = db.registerNewStudent(name, email, phone, address, password)
        if res == False: return {"status":"failed"}
        encodedString = db.generateEncodedString(email, password)
        response = make_response({"status":"success"})
        response.set_cookie('uid', encodedString)
        return response


@app.route("/login", methods = ["GET", "POST"])
def login_page():
    if request.method == "GET":
        if ("uid" in request.cookies):
            encodedString = request.cookies.get("uid")
            db = DB()
            db.makeConnection()
            res = db.loginWithEncodedString(encodedString)
            if res[0] == True and res[1] == True:
                return redirect("/student/dashboard")
            else:
                resp = make_response(redirect("/login"))
                resp.set_cookie("uid", '', expires=0)
                return resp
        else:
            return render_template("login.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        db = DB()
        db.makeConnection()
        res = db.loginWithCred(email, password)
        if res == True:
            resp = make_response({"status":"success"})
            encodedString = db.generateEncodedString(email, password)
            resp.set_cookie("uid", encodedString)
            return resp
        else:
            return {"status":"failed"}

@app.route("/logout", methods = ["GET"])
def logout_page():
    if request.method == "GET":
        resp = make_response(redirect("/login"))
        resp.set_cookie("uid", '', expires=0)
        return resp

@app.route("/student/dashboard", methods = ["GET"])
def student_dashboard():
    if request.method == "GET":
        if ("uid" in request.cookies):
            encodedString = request.cookies.get("uid")
            db = DB()
            db.makeConnection()
            res = db.loginWithEncodedString(encodedString)
            if res[0] == True and res[1] == True:
                data = db.getStudentDetails(res[2])[0]
                return render_template("dashboard.html", studentname = data[1], studentemail = data[2], studentphone = data[3], studentaddress = data[5])
            else:
                resp = make_response(redirect("/login"))
                resp.set_cookie("uid", '', expires=0)
                return resp
        else:
            return redirect("/login")

if __name__ == "__main__":
    app.run(debug = False)


