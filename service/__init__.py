from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api_v1 = Api(app, prefix='/api/v1')

# then import views which use the blueprint
from service.events import views


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response