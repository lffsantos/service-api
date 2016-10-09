from service import db


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
