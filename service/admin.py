from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin
from service import app, db
from service.members.models import Member, Education, Visa, OccupationArea, Technology, Course, ExperienceTime, Gender


def init_admin():
    admin = Admin(app, name='service-api', template_mode='bootstrap3')
    admin.add_view(ModelView(Education, db.session))
    admin.add_view(ModelView(Visa, db.session))
    admin.add_view(ModelView(OccupationArea, db.session))
    admin.add_view(ModelView(Technology, db.session))
    admin.add_view(ModelView(Course, db.session))
    admin.add_view(ModelView(Gender, db.session))
    admin.add_view(ModelView(ExperienceTime, db.session))
    admin.add_view(ModelView(Member, db.session))
