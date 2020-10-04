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
    punttisalinnimi = request.form["paikka"]
    liike = request.form["liike"]
    maara = request.form["maara"]
    paino = request.form["paino"]
    sql = "SELECT id FROM liike WHERE liike=:liike"
    result = db.session.execute(sql, {"liike": liike})
    liikeid = result.fetchone()[0]
    
    sql = "SELECT id FROM paikka WHERE punttisalinnimi=:punttisalinnimi"
    result = db.session.execute(sql, {"punttisalinnimi": punttisalinnimi})
    punttisalinnimiid = result.fetchone()[0]

    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    usernameid = result.fetchone()[0]

    print(type(maara), 'maara', maara)

    sql = "INSERT INTO userstats (maara, painomaara, paivamaara, liike_id, users_id, paikka_id) VALUES (:maara, :paino, NOW(), :liikeid, :usernameid, :punttisalinnimiid)"
    db.session.execute(sql, {"maara": maara, "paino": paino, "liikeid": liikeid, "usernameid": usernameid, "punttisalinnimiid": punttisalinnimiid})
    db.session.commit()

    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()

    if user == None:
        return render_template("usernameNone.html")
    else:
        hash_value = user[0]
    if check_password_hash(hash_value, password):
        session["username"] = username

        """ tallennetaan muistiin kirjautumishetki ja käyttäjän id """
        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        usernameid = result.fetchone()[0]
        
        print(type(usernameid), 'usernameid', usernameid)

        sql = "INSERT INTO userlog (usernameid, sent_at) VALUES (:userid, NOW())"
        db.session.execute(sql, {"userid": usernameid})
        db.session.commit()

        return redirect("/")
    else:
        return render_template("usernameNone.html")


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
    usernameid = result.fetchone()[0]

    sql = "SELECT sent_at FROM userlog WHERE usernameid=:usernameid ORDER BY id DESC"
    result = db.session.execute(sql, {"usernameid":usernameid})
    sent_at = result.fetchall()
    return render_template("userlog.html", sent_at=sent_at)


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")
