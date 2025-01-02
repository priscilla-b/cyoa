from gevent import monkey  # for handling concurrent I/O-bound tasks
monkey.patch_all()  # patches standard python libraries to make them async

import os
from cyoa import app, redis_db, socketio
import click


@app.shell_context_processor
def make_shell_context():
    return {'app': app}

# custom runserver command
@app.cli.command("runserver")
@click.option("--host", default="0.0.0.0", help="Host to run server on.")
@click.option("--port", default=5001, help="Port to run server on." )
def runserver(host, port):
    """Run the flask application with SocketIO"""
    print(f"server starting at: {host}:{port}")
    socketio.run(app, host=host, port=port)


if __name__=='__main__':
    app.run