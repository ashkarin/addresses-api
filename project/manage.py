import os
import yaml
import pandas as pd
import numpy as np

from flask_script import Manager
from sqlalchemy_utils import database_exists, create_database

from myapp import blueprint
from myapp import utils
from myapp.model import address
from myapp.app import create_app, database

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(app.config["APP_HOST"], port=int(app.config["APP_PORT"]))


@manager.option('-p', '--path', dest='path', 
                help='Path to a CSV file', default=None)
@manager.option('-c', '--conf', dest='conf_path', 
                help='Path to a column configuration file', default=None)
def export(path, conf_path):
    if not database_exists(db.engine.url):
        create_database(db.engine.url)

    db.create_all()

    df = pd.read_csv(path)
    df = df.head(20000)

    app.logger.info('Opening column configuration file: {}'.format(path))
    with open(conf_path, 'r') as f:
        col_config = yaml.load(f)

    df = utils.transform_columns(df, col_config)
    db.session.bulk_insert_mappings(address.Address, df.to_dict(orient='records'))
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    manager.run()
