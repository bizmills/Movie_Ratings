from flask import Flask, render_template, redirect, request, flash, session
from model import db_session, User, Rating, Movie
import os

app = Flask(__name__)
SECRET_KEY = "monkey"
app.config.from_object(__name__)

@app.route("/")
def index():
    user_list = db_session.query(User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup", methods=["GET"])
def show_signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def process_sign_up():
    d = request.form
    # print "_____________%r" % d
    # 1) create a User object with form data
    new_user = User(email=d['email'], password=d['password'])
    # 2) add object to db
    db_session.add(new_user)
    # 3) commit
    db_session.commit()
    return render_template("signup.html")

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    print session
    email = request.form['email']
    password = request.form['password']
    query = db_session.query(User)
    user = query.filter_by(email=email).first()
    print user

#if user not found, does db return None?
    if user == None:
        flash("You are not in the database.")
    elif user.password != password:
        flash("Password incorrect. Unable to log in.")
    else:
        #add customer to cookie session, which is a dictionary
        session["customer"] = user.id
        flash("You've successfully logged in.")
    return redirect("/")

@app.route("/user_details/<int:user_id>")
def get_details(user_id):
    # ratings = db_session.query(Rating).filter_by(user_id=user, movie_id=id).all()

    #This returns all rating objects from a user
    user_ratings = db_session.query(Rating).filter_by(user_id=user_id).all()
    # for rating in user_ratings:
    #     #all rating objects have a movie object in them, with attributes, as well as user objects
    #     print rating.rating, rating.user.id, rating.movie.name
    # return "Boo"
    return render_template("user_details.html", user_ratings= user_ratings, user_id=user_id)
if __name__== "__main__":
    app.run(debug=True)