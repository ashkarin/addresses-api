from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Statistics on addresses',
          version='1.0',
          description='A web-service to get some statistics on addresses in Berlin.'
          )
