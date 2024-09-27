from flask import Flask
from LiveChat.config import Config
from flask_socketio import SocketIO

socketio=SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from LiveChat.room.room import rooom
    app.register_blueprint(rooom)

    from LiveChat.main.main import main
    app.register_blueprint(main)

    socketio.init_app(app)
    return app
