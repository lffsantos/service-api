from service import api_v1
from flask_restful import Resource


class HelloWord(Resource):
    """TEST"""
    def get(self):
        return {'ok': 'ok'}


api_v1.add_resource(HelloWord, '/')
