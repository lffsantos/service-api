from flask import Flask, Blueprint
from flask.ext import restful
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
api_v1 = restful.Api(blueprint, prefix="/api/v1")

from service.events.resources.views import EventsMeetup
from service.members.resources.views import (
    Education, EducationItem, EducationList, CourseItem, CourseList, VisaItem, VisaList,
    TechnologyItem, TechnologyList, OccupationAreaItem, OccupationAreaList,
    MemberItem, MemberList)

api_v1.add_resource(EventsMeetup, "/events_meetup", endpoint='events_meetup')
api_v1.add_resource(MemberItem, "/members/<int:member_id>", endpoint='member')
api_v1.add_resource(MemberList, "/members", endpoint='members')
api_v1.add_resource(EducationItem, "/educations/<int:obj_id>", endpoint='education')
api_v1.add_resource(EducationList, "/educations", endpoint='educations')
api_v1.add_resource(CourseItem, "/courses/<int:obj_id>", endpoint='course')
api_v1.add_resource(CourseList, "/courses", endpoint='courses')
api_v1.add_resource(VisaItem, "/visas/<int:obj_id>", endpoint='visa')
api_v1.add_resource(VisaList, "/visas", endpoint='visas')
api_v1.add_resource(TechnologyItem, "/technologies/<int:obj_id>", endpoint='technology')
api_v1.add_resource(TechnologyList, "/technologies", endpoint='technologies')
api_v1.add_resource(OccupationAreaItem, "/occupations/<int:obj_id>", endpoint='occupation')
api_v1.add_resource(OccupationAreaList, "/occupations", endpoint='occupations')

app.register_blueprint(blueprint)

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
