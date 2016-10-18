import re
from service import db
from service.members.exceptions import InvalidValueError, AuxModelAlreadyExists
from sqlalchemy.exc import IntegrityError


def _verify_type(field_name, value, expected_type):
    if not isinstance(value, expected_type):
        raise InvalidValueError(field_name, value, expected_type.__name__)


class BaseModel(db.Model):
    __abstract__ = True

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

    def save_or_update(self):
        _verify_type('name', self.name, str)
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except IntegrityError as e:
            db.session.rollback()
            m = re.search(r"\((?:(.*?))\)=\((?:(.*?))\)", e.args[0].split('\n')[1])
            key, value = m.group(1), m.group(2)
            raise AuxModelAlreadyExists(self.__class__.__name__, key, value)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Education(BaseModel):
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

    def save_or_update(self):
        _verify_type('level', self.level, str)
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except IntegrityError as e:
            db.session.rollback()
            m = re.search(r"\((?:(.*?))\)=\((?:(.*?))\)", e.args[0].split('\n')[1])
            key, value = m.group(1), m.group(2)
            raise AuxModelAlreadyExists(self.__class__.__name__, key, value)


class Course(BaseModel):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='course', lazy='dynamic')


class Visa(BaseModel):
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


class OccupationArea(BaseModel):
    __tablename__ = 'occupation_area'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='occupation_area', lazy='dynamic')


class Technology(BaseModel):
    __tablename__ = 'technology'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Gender(BaseModel):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='gender', lazy='dynamic')


class ExperienceTime(BaseModel):
    __tablename__ = 'experience_time'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    members = db.relationship('Member', backref='experience_time', lazy='dynamic')
