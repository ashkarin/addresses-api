from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myapp.config import CONFIG_BY_NAME


database = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(CONFIG_BY_NAME[config_name])
    database.init_app(app)
    return app
