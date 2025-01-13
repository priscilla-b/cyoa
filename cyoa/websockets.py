from flask_socketio import emit
from . import socketio

@socketio.on('connect', namespace='/cyoa')
def test_connection():
    pass

@socketio.on('disconnet', namespace='/cyoa')
def test_disconnet():
    pass