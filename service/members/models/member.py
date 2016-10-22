import json
import re
import time

from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import backref

from service import db
from service.members.models import Technology
from service.members.exceptions import (
    InvalidValueError, MemberAlreadyExists, InvalidConstraint,
    InvalidArgument
)


member_technology = db.Table(
    'member_technology',
    db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
    db.Column('technology_id', db.Integer, db.ForeignKey('technology.id')),
    db.PrimaryKeyConstraint('member_id', 'technology_id')
)


def _verify_type(field_name, value, expected_type, can_be_none=False):
    if can_be_none:
        return

    if not isinstance(value, expected_type):
        raise InvalidValueError(field_name, value, expected_type.__name__)


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
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
    experience_time_id = db.Column(db.Integer, db.ForeignKey('experience_time.id'))
    education_id = db.Column(db.Integer, db.ForeignKey('education.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    visa_id = db.Column(db.Integer, db.ForeignKey('visa.id'))
    occupation_area_id = db.Column(db.Integer, db.ForeignKey('occupation_area.id'))
    technologies = db.relationship(
        'Technology', secondary=member_technology, backref=backref('members', lazy='dynamic')
    )
    is_working = db.Column(db.Boolean)

    @property
    def serialize_technologies(self):
        """
        Return object's relations in easily serializeable format.
        Calls many2many's serialize property.
        """
        return [tech.serialize for tech in self.technologies]

    def age(self):
        return time.gmtime()[0] - self.birth.year

    def avatar(self):
        if self.github:
            username = self.github.split('/')
            return 'https://avatars.githubusercontent.com/{}'.format(username[-1])
        return None

    @property
    def serialize(self):
        return {
            'id': self.id,
            'gender': self.gender.serialize,
            'full_name': self.full_name,
            'short_name': self.short_name,
            'birth': dump_datetime(self.birth),
            'age': self.age(),
            'avatar': self.avatar(),
            'email': self.email,
            'about': self.about,
            'confirmed': self.confirmed,
            'update_at': dump_datetime(self.update_at),
            'github': self.github,
            'linkedin': self.linkedin,
            'phone': self.phone,
            'experience_time': self.experience_time.serialize,
            'education': self.education.serialize,
            'course': self.course.serialize,
            'visa': self.visa.serialize,
            'occupation_area': self.occupation_area.serialize,
            'technologies': self.serialize_technologies,
            'is_working': self.is_working,
        }

    def fill_member(self, args):
        fields = ['gender_id', 'full_name', 'short_name', 'birth', 'email', 'confirmed',
                  'about', 'linkedin', 'github', 'phone', 'experience_time_id',
                  'course_id', 'education_id', 'visa_id', 'occupation_area_id',
                  'is_working']

        for key, value in args.items():
            if key not in fields:
                raise InvalidArgument(Member, key)
            setattr(self, key, value)
        self.validate()
        return self

    def save_or_update(self, technologies=None):
        self.validate()
        if isinstance(self.birth, str):
            try:
                self.birth = datetime.strptime(self.birth, '%d%m%Y')
            except ValueError:
                raise InvalidValueError('birth', self.birth, 'ddmmyyyy')

        db.session.add(self)
        try:
            if technologies:
                technologies = json.loads(technologies)
                for tech in Technology.query.filter(Technology.id.in_(technologies)):
                    self.technologies.append(tech)
            db.session.commit()
            return self
        except IntegrityError as e:
            db.session.rollback()
            m = re.search(r"\((?:(.*?))\)=\((?:(.*?))\)", e.args[0].split('\n')[1])
            key, value = m.group(1), m.group(2)
            regexp = re.compile(r'violates foreign key')
            if regexp.search(e.args[0]) is not None:
                raise InvalidConstraint(key, value)
            else:
                raise MemberAlreadyExists(key, value)

    def validate(self):
        _verify_type('full_name', self.full_name, str)
        _verify_type('short_name', self.short_name, str, True)
        _verify_type('email', self.email, str)
        _verify_type('linkedin', self.linkedin, str, True)
        _verify_type('github', self.github, str, True)
        _verify_type('phone', self.phone, str, True)
        _verify_type('gender_id', self.gender_id, int)
        _verify_type('experience_time_id', self.experience_time_id, int, True)
        _verify_type('education_id', self.education_id, int, True)
        _verify_type('visa_id', self.visa_id, int, True)
        _verify_type('course_id', self.course_id, int, True)
        _verify_type('occupation_area_id', self.occupation_area_id, int, True)
        _verify_type('birth', self.birth, str)

    def __repr__(self):
        return self.full_name
