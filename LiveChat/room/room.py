from flask import Flask, Blueprint, render_template
from LiveChat.main.main import rooms, session

rooom = Blueprint('rooom', __name__)

@rooom.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return render_template('home.html', title='Home')

    return render_template("room.html", title="ro.om")
