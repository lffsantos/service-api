from flask.ext.validator import ValidateString
from service import db


class Education(db.Model):
    __tablename__ = 'education'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='education', lazy='dynamic')

    def __init__(self, level):
        self.level = level

    @property
    def serialize(self):
        return {
            'id': self.id,
            'level': self.level,
        }

    def __repr__(self):
        return self.level

    @classmethod
    def __declare_last__(cls):
        ValidateString(Education.level, False, True)


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='course', lazy='dynamic')

    def __init__(self, name):
        self.name = name

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

    def __init__(self, name, description):
        self.name = name
        self.description = description

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

    def __init__(self, name):
        self.name = name

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

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return self.name


class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='gender', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return self.name


class ExperienceTime(db.Model):
    __tablename__ = 'experience_time'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='experience_time', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return self.name