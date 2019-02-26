import os
from flask import Flask
from .errors import not_found, not_allowed
from flask_sapb1 import SAPB1Adaptor
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp
import logging


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

jwt = JWT(authentication_handler=authenticate, identity_handler=identity)

sapb1Adaptor = SAPB1Adaptor()

def create_app(config_module=None):
    app = Flask(__name__)
    app.secret_key = "byrkNHdlH6ux"
    app.config.from_object(config_module or
                           os.environ.get('FLASK_CONFIG') or
                           'config')

    jwt.init_app(app)

    # connect to sapb1
    sapb1Adaptor.init_app(app)

    from api.v1 import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/v1')

    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config['LOGGING_LEVEL'])

    @app.errorhandler(404)
    def not_found_error(e):
        return not_found('item not found')

    @app.errorhandler(405)
    def method_not_allowed_error(e):
        return not_allowed()

    return app
