from flask import Blueprint, render_template, request, redirect, session
from utils.encrypt_handler import encryption_check

auth_route = Blueprint("auth", __name__)

@auth_route.route('/', methods=["GET", "POST"])
def auth_router():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["code"]

        if email.lower() == "vex@menudocs.org" and encryption_check(password) == True:
            session['user'] = "vex"
            return redirect('/')
        else:
            return render_template("login.html")
