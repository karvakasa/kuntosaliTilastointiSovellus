from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["POST"])
def add():
    paikka = request.form["paikka"]
    liike = request.form["liike"]
    maara = request.form["maara"]
    paino = request.form["paino"]
    sql = "INSERT INTO"

    return redirect("/")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user == None:
        return render_template("usernameNone.html")
    else:
        hash_value = user[0]
    if check_password_hash(hash_value,password):
        session["username"] = username
        return redirect("/")
    else:
        return render_template("usernameNone.html")

@app.route("/newUser",methods=["POST"])
def newUser():
    username = request.form["username"]
    password = request.form["password"]
    sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
    hash_value = generate_password_hash(password)
    db.session.execute(sql, {"username":username,"password":hash_value})
    db.session.commit()
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/userlog")
def userlog():
    return render_template("userlog.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")