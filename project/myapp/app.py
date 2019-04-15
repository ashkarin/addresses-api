from flask import Flask
from myapp.config import CONFIG_BY_NAME


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(CONFIG_BY_NAME[config_name])
    return app
