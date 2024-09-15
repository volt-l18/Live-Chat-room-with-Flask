from flask import Flask, request, session, redirect
from LiveChat.config import Config
from flask_socketio import join_room, leave_room, SocketIO
import random
from string import ascii_uppercase

socketio=SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from LiveChat.main.routes import main
    app.register_blueprint(main)
    return app