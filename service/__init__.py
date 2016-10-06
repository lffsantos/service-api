from flask import Flask
from flask.ext.cors import CORS
from flask_restful import Api

app = Flask(__name__)
api_v1 = Api(app, prefix='/api/v1')

# then import views which use the blueprint
from service.events import views

# now register the blueprint with the app
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})