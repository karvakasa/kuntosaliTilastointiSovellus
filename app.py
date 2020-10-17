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


@app.route("/add", methods=["POST"])
def add():
    username = session.get("username")
    gym_place = request.form["gym"]
    gym_equipment = request.form["gym_equipment"]
    do_amount = request.form["do_amount"]
    weight_amount = request.form["weight_amount"]
    sql = "SELECT id FROM equipment WHERE gym_equipment=:gym_equipment"
    result = db.session.execute(sql, {"gym_equipment": gym_equipment})
    equipment_id = result.fetchone()[0]
    
    sql = "SELECT id FROM gym WHERE gym_place=:gym_place"
    result = db.session.execute(sql, {"gym_place": gym_place})
    gym_place_id = result.fetchone()[0]

    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]
    

    sql = "INSERT INTO userstats (do_amount, weight_amount, date, equipment_id, users_id, gym_id) VALUES (:do_amount, :weight_amount, NOW(), :equipment_id, :username_id, :gym_place_id)"
    db.session.execute(sql, {"do_amount": do_amount, "weight_amount": weight_amount, "equipment_id": equipment_id, "username_id": username_id, "gym_place_id": gym_place_id})
    db.session.commit()

    return redirect("/")

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
        
        print(type(usernameid), 'usernameid', usernameid)

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


@app.route("/userlog")
def userlog():
    
    username = session.get("username")
    

    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]

    sql = "SELECT sent_at FROM userlog WHERE usernameid=:usernameid ORDER BY id DESC"
    result = db.session.execute(sql, {"usernameid":username_id})
    sent_at = result.fetchall()
    return render_template("userlog.html", sent_at=sent_at)


@app.route("/statistics")
def statistics():

    username = session.get("username")
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]
    sql = "SELECT gym_equipment, gym_place, date FROM userstats INNER JOIN gym ON userstats.gym_id=gym.id INNER JOIN equipment ON userstats.equipment_id=equipment.id WHERE users_id=:users_id ORDER BY date DESC"
    result = db.session.execute(sql, {"users_id":username_id})
    stats = result.fetchall()
    
    return render_template("statistics.html", stats=stats)

@app.route("/scottish_bench")
def scottish_bench():

    username = session.get("username")
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]
    sql = "SELECT date, do_amount, weight_amount, gym_place FROM userstats INNER JOIN gym ON userstats.gym_id=gym.id INNER JOIN equipment ON userstats.equipment_id=equipment.id WHERE users_id=:users_id AND equipment.id=2 ORDER BY date DESC"
    result = db.session.execute(sql, {"users_id":username_id})
    stats = result.fetchall()

    return render_template("scottish_bench.html", stats=stats)
    
@app.route("/deadlift")
def deadlift():
    username = session.get("username")
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]
    sql = "SELECT date, do_amount, weight_amount, gym_place FROM userstats INNER JOIN gym ON userstats.gym_id=gym.id INNER JOIN equipment ON userstats.equipment_id=equipment.id WHERE users_id=:users_id AND equipment.id=5 ORDER BY date DESC"
    result = db.session.execute(sql, {"users_id":username_id})
    stats = result.fetchall()
    return render_template("deadlift.html", stats=stats)

@app.route("/squat")
def squat():
    username = session.get("username")
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]
    sql = "SELECT date, do_amount, weight_amount, gym_place FROM userstats INNER JOIN gym ON userstats.gym_id=gym.id INNER JOIN equipment ON userstats.equipment_id=equipment.id WHERE users_id=:users_id AND equipment.id=3 ORDER BY date DESC"
    result = db.session.execute(sql, {"users_id":username_id})
    stats = result.fetchall()
    return render_template("squat.html", stats=stats)

@app.route("/footpress")
def footpress():
    username = session.get("username")
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]
    sql = "SELECT date, do_amount, weight_amount, gym_place FROM userstats INNER JOIN gym ON userstats.gym_id=gym.id INNER JOIN equipment ON userstats.equipment_id=equipment.id WHERE users_id=:users_id AND equipment.id=4 ORDER BY date DESC"
    result = db.session.execute(sql, {"users_id":username_id})
    stats = result.fetchall()
    return render_template("footpress.html", stats=stats)

@app.route("/bench_press")
def bench_press():
    username = session.get("username")
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    username_id = result.fetchone()[0]
    sql = "SELECT date, do_amount, weight_amount, gym_place FROM userstats INNER JOIN gym ON userstats.gym_id=gym.id INNER JOIN equipment ON userstats.equipment_id=equipment.id WHERE users_id=:users_id AND equipment.id=1 ORDER BY date DESC"
    result = db.session.execute(sql, {"users_id":username_id})
    stats = result.fetchall()
    return render_template("bench_press.html", stats=stats)