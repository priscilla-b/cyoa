from flask import render_template, abort
from jinja2 import TemplateNotFound

from . import app

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