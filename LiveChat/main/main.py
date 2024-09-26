import random

from flask import render_template, Blueprint, request, session, redirect, url_for
from string import ascii_uppercase
from flask_socketio import join_room, leave_room, send, SocketIO
from LiveChat import socketio

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

        return redirect(url_for("rooom.room"))

    return render_template('home.html', title='Home')

@socketio.on('message')
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    content={
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content,to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said : {data['data']}")

@socketio.on('connect')
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"]+=1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")
