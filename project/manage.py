import os

from flask_script import Manager

from myapp import blueprint
from myapp.app import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(app.config["APP_HOST"], port=int(app.config["APP_PORT"]))


@manager.option('-c', '--conf', dest='conf_path', 
                help='Path to a column configuration file', default=None)
def export(path, conf_path):
    pass


if __name__ == '__main__':
    manager.run()
