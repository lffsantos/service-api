from flask import Flask, Blueprint
from flask.ext.cache import Cache
from flask.ext.cors import CORS


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

api_v1 = Blueprint('api_v1', __name__)

# then import views which use the blueprint
from service.events import views
from . import views

# now register the blueprint with the app
app.register_blueprint(api_v1, url_prefix='/api/v1')

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
