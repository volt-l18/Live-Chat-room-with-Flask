from LiveChat import create_app, socketio

app = create_app()
socketio.init_app(app)

if __name__ == "__main__":
    socketio.run(app)
