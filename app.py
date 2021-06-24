import os

from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api

from config.db_connect import DBConnector

from config.settings import DevConfig
from utils.middlewares import OperationLogMiddleware
from apps import product
from utils.utils import MongoJSONEncoder, ObjectIdConverter


# Flask app creation
app = Flask(__name__)
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

app.config.from_object(DevConfig())

# CORS 
cors = CORS(app, resources={r"/api/*": {"origins": '*'}})

# middleware
app.wsgi_app = OperationLogMiddleware(app.wsgi_app)

# Falsk -RestApi
api = Api(app, prefix='/api/v1')



# datbase connect
mongo = DBConnector.connect_with_pool(app)

#init urls
from config.routers import initialize_routes
initialize_routes(api)
app.url_map.strict_slashes = False

