from flask import Flask, Blueprint, render_template

rooms = Blueprint('rooms', __name__)

@rooms.route("/room")
def room():
    return render_template("room.html", title="ro.om")
