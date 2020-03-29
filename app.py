from flask import Blueprint
from flask_restful import Api
from critterpedia import (Health, Fish, Bugs)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Health, '/health')
api.add_resource(Fish, '/fish')
api.add_resource(Bugs, '/bugs')
