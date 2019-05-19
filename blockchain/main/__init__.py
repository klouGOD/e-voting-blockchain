from flask import Flask, Blueprint
from flask_restful import Api
from flask_bcrypt import Bcrypt
from uuid import uuid4

from .config import Config
from .model.blockchain import Blockchain
from .controller.transaction import TransactionVC

flask_bcrypt = Bcrypt()

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(TransactionVC, '/transaction')

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  app.register_blueprint(api_bp, url_prefix='/api')
  flask_bcrypt.init_app(app)
  
  return app