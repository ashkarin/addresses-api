from flask_restplus import Api
from flask import Blueprint

from .controller.address_controller import api as address_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Statistics on addresses',
          version='1.0',
          description='A web-service to get some statistics on addresses in Berlin.'
          )

api.add_namespace(address_ns, path='/address')