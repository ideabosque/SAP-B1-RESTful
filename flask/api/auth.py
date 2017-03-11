from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from .errors import unauthorized

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == current_app.config['USERNAME'] and password == current_app.config['PASSWORD']

@auth.error_handler
def unauthorized_error():
    return unauthorized()
