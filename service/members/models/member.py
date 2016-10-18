import re
import time
from datetime import datetime
from service import db
from service.members.models import Technology
from service.members.exceptions import InvalidValueError, MemberAlreadyExists
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import backref


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

    def __repr__(self):
        return self.full_name

    def save_or_update(self, technologies=None):
        _verify_type('full_name', self.full_name, str)
        _verify_type('short)name', self.short_name, str, True)
        _verify_type('email', self.email, str)
        _verify_type('linkedin', self.linkedin, str, True)
        _verify_type('github', self.github, str, True)
        _verify_type('phone', self.phone, str, True)
        _verify_type('gender_id', self.gender_id, int)
        _verify_type('experience_time_id', self.experience_time_id, int)
        _verify_type('education_id', self.education_id, int)
        _verify_type('visa_id', self.visa_id, int)
        _verify_type('course_id', self.course_id, int)
        _verify_type('occupation_area_id', self.occupation_area_id, int)
        _verify_type('birth', self.birth, str)
        try:
            self.birth = datetime.strptime(self.birth, '%d%m%Y')
        except ValueError:
            raise InvalidValueError(Member.__name__, self.birth, 'ddmmyyyy')

        db.session.add(self)
        try:
            if technologies:
                for tech in Technology.query.filter(Technology.id.in_(technologies)):
                    self.technologies.append(tech)
            db.session.commit()
            return self
        except IntegrityError as e:
            m = re.search(r"\((?:(.*?))\)=\((?:(.*?))\)", e.args[0].split('\n')[1])
            key, value = m.group(1), m.group(2)
            raise MemberAlreadyExists(key, value)
