from flask import Flask, render_template, redirect, request
import jinja2
import model
from model import db_session

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.db_session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup", methods=["GET"])
def show_signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def process_sign_up():
    d = request.form
    # print "_____________%r" % d
    # 1) create a User object with form data
    new_user = model.User(email=d['email'], password=d['password'])
    # 2) add object to db
    model.db_session.add(new_user)
    # 3) commit
    model.db_session.commit()
    return render_template("signup.html")

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    user = model.db_session.query(model.User).filter_by(email=request.form['email']).filter_by(password=request.form['password']).one()
    print user

    return render_template("login.html")

if __name__== "__main__":
    app.run(debug=True)