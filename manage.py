from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from service import app, db
from service.util.import_files import run_importer

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def import_files():
    run_importer()

if __name__ == '__main__':
    manager.run()