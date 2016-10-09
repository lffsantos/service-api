from flask import Flask, Blueprint
from flask.ext.admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_cache import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from service.helper import MyJSONEncoder


app = Flask(__name__)
app.json_encoder = MyJSONEncoder
app.secret_key = config('SECRET_KEY')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api_v1 = Blueprint('api_v1', __name__)

# then import views which use the blueprint
from service.events import views
from service.members import views
from service import views

# now register the blueprint with the app
app.register_blueprint(api_v1, url_prefix='/api/v1')

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Admin
from service.members.models import Member, Education, Visa, OccupationArea, Technology, Course, MemberAdmin

if config('DEBUG', default=False, cast=bool):
    admin = Admin(app, name='service-api', template_mode='bootstrap3')
    admin.add_view(MemberAdmin(Member, db.session))
    admin.add_view(ModelView(Education, db.session))
    admin.add_view(ModelView(Visa, db.session))
    admin.add_view(ModelView(OccupationArea, db.session))
    admin.add_view(ModelView(Technology, db.session))
    admin.add_view(ModelView(Course, db.session))


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
