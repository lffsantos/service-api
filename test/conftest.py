import pytest
import service

from decouple import config
from flask.ext.mail import Mail


TEST_DATABASE_URI = config('DATABASE') + '_test'


@pytest.fixture(scope='function')
def app(request):
    """Session-wide test `Flask` application."""
    app = service.app
    app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DATABASE_URI
    app.config['TESTING'] = True
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def db(app, request):
    """Session-wide test database."""

    service.db.drop_all()

    def teardown():
        service.db.drop_all()

    service.db.app = app
    service.db.create_all()

    request.addfinalizer(teardown)
    return service.db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        session.rollback()
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.yield_fixture
def mail():
    service.app.config['TESTING'] = True
    with service.app.app_context():
        service.mail = Mail(service.app)
        yield service.mail