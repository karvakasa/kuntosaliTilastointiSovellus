from app import app
from db import db
from flask import render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
import statistics

@app.route("/")
def index():
    return render_template("index.html")
null
@app.route("/donewuser", methods=["POST"])
def donewuser():
    return render_template("newuser.html")
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()

    if user == None:
        return render_template("usernamenone.html")
    else:
        hash_value = user[0]
    if check_password_hash(hash_value, password):
        session["username"] = username

        """ save log in time and user id """
        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        usernameid = result.fetchone()[0]

        sql = "INSERT INTO userlog (usernameid, sent_at) VALUES (:userid, NOW())"
        db.session.execute(sql, {"userid": usernameid})
        db.session.commit()

        return redirect("/")
    else:
        return render_template("usernamenone.html")


@app.route("/newUser", methods=["POST"])
def newUser():
    username = request.form["username"]
    password = request.form["password"]
    sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
    hash_value = generate_password_hash(password)
    db.session.execute(sql, {"username": username, "password": hash_value})
    db.session.commit()
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")