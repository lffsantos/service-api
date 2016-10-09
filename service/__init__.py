from flask import Flask, Blueprint
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


api_v1 = Blueprint('api_v1', __name__)

# then import views which use the blueprint
from service.events import views
from service.members import views

# now register the blueprint with the app
app.register_blueprint(api_v1, url_prefix='/api/v1')

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
