import os
from flask import Flask
from .auth import auth
from .errors import not_found, not_allowed
from flask_sapb1 import SAPB1Adaptor
import logging

sapb1Adaptor = SAPB1Adaptor()

def create_app(config_module=None):
    app = Flask(__name__)
    app.config.from_object(config_module or
                           os.environ.get('FLASK_CONFIG') or
                           'config')

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
    @auth.login_required
    def not_found_error(e):
        return not_found('item not found')

    @app.errorhandler(405)
    def method_not_allowed_error(e):
        return not_allowed()

    return app
