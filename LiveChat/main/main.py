import random

from flask import render_template, Blueprint, request, session, redirect, url_for
from string import ascii_uppercase

main = Blueprint('main' , __name__)

rooms={}

def genrate_unique_code(length):
    while True:
        code = ""
        for i in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code

@main.route("/", methods = ['GET', 'POST'])
@main.route("/home", methods = ['GET', 'POST'])
def home():
    session.clear()
    if request.method == 'POST':
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("home.html", title='Home', error="Please enter a name", code=code, name=name)

        if join != False and not code:
            return render_template("home.html", title='Home', error="Please enter a room code", code=code, name=name)

        room = code
        if create != False:
            room = genrate_unique_code(6)
            rooms[room]={"members":0, "messages":[]}
        elif code not in rooms:
            return render_template("home.html", title='Home', error="Room does not exist!", code=code, name=name)

        session["room"] = room
        session["name"] = name

        return redirect(url_for("rooms.room"))

    return render_template('home.html', title='Home')