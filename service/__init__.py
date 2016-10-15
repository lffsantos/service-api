from flask import Flask, Blueprint
from flask_restplus import Api
from flask_cache import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from decouple import config

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = config('SECRET_KEY')


cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from service.serializer import MyJSONEncoder
app.json_encoder = MyJSONEncoder

blueprint = Blueprint('api_v1', __name__)
api_v1 = Api(blueprint, prefix="/api/v1")

from service.events.resources.views import *
from service.members.resources.views import *

app.register_blueprint(blueprint)

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
