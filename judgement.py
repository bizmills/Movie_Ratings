from flask import Flask, render_template, redirect, request, session
import jinja2
import model

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup", methods=["GET"])
def show_signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def process_sign_up():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__== "__main__":
    app.run(debug=True)