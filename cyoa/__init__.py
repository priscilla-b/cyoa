from flask import Flask
from flask_socketio import SocketIO
import redis
from .config import REDIS_SERVER, REDIS_PORT, REDIS_DB

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

redis_db = redis.StrictRedis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)

socketio = SocketIO(app)


from . import views
from . import websockets


