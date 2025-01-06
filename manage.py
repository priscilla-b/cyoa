from gevent import monkey  # for handling concurrent I/O-bound tasks
monkey.patch_all()  # patches standard python libraries to make them async

from cyoa import app, redis_db, socketio
import click
import redis


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'redis_db': redis_db}

# custom runserver command
@app.cli.command("runserver")
@click.option("--host", default="127.0.0.1", help="Host to run server on.")
@click.option("--port", default=8080, help="Port to run server on." )
def runserver(host, port):
    """Run the flask application with SocketIO"""
    
    url = f"http://{host}:{port}"
    print(f"server starting at: {url}")
    
    
    socketio.run(app, host=host, port=port)

# command to clear votes stored with redis
@app.cli.command("clear_redis")
def clear_redis():
    redis_cli = redis.StrictRedis(host='localhost', port='6379', db='0')
    redis_cli.delete('left')
    redis_cli.delete('right')

if __name__=='__main__':
    print("running file directly")
    socketio.run(app, host="127.0.0.1", port=5001, debug=True)