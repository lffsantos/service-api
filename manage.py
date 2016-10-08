from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from service import app, db

from service.members.db import models

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()