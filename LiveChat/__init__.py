from flask import Flask, request, session, redirect
from LiveChat.config import Config
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

socketio=SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from LiveChat.main.main import main
    from LiveChat.room.room import rooms

    app.register_blueprint(rooms)
    app.register_blueprint(main)
    return app
