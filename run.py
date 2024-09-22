from LiveChat import create_app, SocketIO

app = create_app()

if __name__ == "__main__":
    SocketIO.run(app, host='0.0.0.0', debug=True)
