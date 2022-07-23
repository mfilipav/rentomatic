from flask import Flask

from application.rest import room


def create_app(config_name):
    """
    Flask application can be configured using a plain Python object
    config defined in 'application/config.py'
    https://flask.palletsprojects.com/en/2.1.x/api/#flask.Config.from_object

    config_name: development, testing, production
    config_module: will become 'application.config.TestingConfig'
        - imported from config.TestingConfig
    """
    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    # app factories
    # https://flask.palletsprojects.com/en/2.1.x/config/#development-production
    app.config.from_object(config_module)
	
    # register the blueprint created in rest/room.py
    app.register_blueprint(room.blueprint)
	
    return app
