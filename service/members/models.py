from datetime import datetime
from flask.ext.admin.contrib import sqlamodel

from service import db
from sqlalchemy.orm import backref
from sqlalchemy_utils import ChoiceType


class Education(db.Model):
    __tablename__ = 'education'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='education', lazy='dynamic')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'level': self.level,
        }

    def __repr__(self):
        return self.level


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='course', lazy='dynamic')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return self.name


class Visa(db.Model):
    __tablename__ = 'visa'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text)
    members = db.relationship('Member', backref='visa', lazy='dynamic')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

    def __repr__(self):
        return self.name


class OccupationArea(db.Model):
    __tablename__ = 'occupation_area'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='occupation_area', lazy='dynamic')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return self.name


class Technology(db.Model):
    __tablename__ = 'technology'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return self.name


member_technology = db.Table(
    'member_technology',
    db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
    db.Column('technology_id', db.Integer, db.ForeignKey('technology.id')),
    db.PrimaryKeyConstraint('member_id', 'technology_id')
)


class Member(db.Model):
    __tablename__ = 'member'

    GENDER = [
        (u'male', u'Male'),
        (u'female', u'Female')
    ]
    EXPERIENCE_TIME = [
        ('0', u'Sem experiência'),
        ('1', u' < 1 ano')
    ]

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(ChoiceType(GENDER), nullable=False)
    full_name = db.Column(db.String, unique=True, nullable=False)
    short_name = db.Column(db.String)
    birth = db.Column(db.Date)
    email = db.Column(db.String, unique=True, nullable=False)
    about = db.Column(db.Text)
    confirmed = db.Column(db.Boolean, default=False)
    update_at = db.Column(db.DateTime, default=datetime.now())
    linkedin = db.Column(db.String)
    github = db.Column(db.String)
    phone = db.Column(db.String)
    experience_time = db.Column(ChoiceType(EXPERIENCE_TIME, impl=db.String()))
    education_id = db.Column(db.Integer, db.ForeignKey('education.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    visa_id = db.Column(db.Integer, db.ForeignKey('visa.id'))
    occupation_area_id = db.Column(db.Integer, db.ForeignKey('occupation_area.id'))
    technologies = db.relationship(
        'Technology', secondary=member_technology, backref=backref('members', lazy='dynamic')
    )
    is_work = db.Column(db.Boolean)

    @property
    def serialize_technologies(self):
        """
        Return object's relations in easily serializeable format.
        Calls many2many's serialize property.
        """
        return [tech.serialize for tech in self.technologies]

    def __repr__(self):
        return self.full_name


class MemberAdmin(sqlamodel.ModelView):
    form_choices = {
        'gender': Member.GENDER,
        'experience_time': Member.EXPERIENCE_TIME
    }
