import cgi
from flask import render_template, abort, request
from jinja2 import TemplateNotFound
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from .config import TWILIO_NUMBER

from . import app, redis_db, socketio

@app.route('/<presentation_name>/', methods=['GET'])
def landing(presentation_name):
    """
    Accepts presentation name input passed to the url and then checks in the cyoa/cyoa/templates
    directory for an html file matching the name and renders it if found.

    Args:
        presentation_name (str): The name of the presentation(template) to be rendered

    Returns:
        Response: The rendered html template with the given presentation name.
        Will return 404 if there's no template that corresponds to the given
        presentation name
    """
    try:
        return render_template(presentation_name + '.html')
    except TemplateNotFound:
        abort(404)
        
        
@app.route('/cyoa/twilio/webhook', methods=['POST'])
def twilio_callback():
    to = request.form.get('To', '')
    from_ = request.form.get('From', '')
    message = request.form.get('Body', '').lower()
    
    if to == TWILIO_NUMBER:
        redis_db.incr(cgi.escape(message))
    
    resp = MessagingResponse()
    resp.message('Thanks for your vote!')
    return str(resp)
    