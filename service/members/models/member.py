import time
from datetime import datetime
from flask.ext.validator import ValidateString, ValidateInteger, ValidateEmail

from service import db
from sqlalchemy.orm import backref


member_technology = db.Table(
    'member_technology',
    db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
    db.Column('technology_id', db.Integer, db.ForeignKey('technology.id')),
    db.PrimaryKeyConstraint('member_id', 'technology_id')
)


class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
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

    # @classmethod
    # def __declare_last__(cls):
    #     ValidateString(Member.full_name, False, True)
    #     ValidateString(Member.short_name, True, True)
    #     ValidateInteger(Member.gender, False, True)
    #     ValidateInteger(Member.experience_time, True, True)
    #     ValidateInteger(Member.education_id, True, True)
    #     ValidateInteger(Member.course_id, True, True)
    #     ValidateInteger(Member.visa_id, True, True)
    #     ValidateInteger(Member.occupation_area_id, True, True)
    #     ValidateEmail(Member.email, allow_null=False, throw_exception=True)

    def age(self):
        return time.gmtime()[0] - self.birth.year

    def __repr__(self):
        return self.full_name
