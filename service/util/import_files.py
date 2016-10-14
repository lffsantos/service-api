import csv
import logging

import os
from service import db
from service.members.models import Course, Education, OccupationArea, Technology, Visa
from sqlalchemy.exc import IntegrityError


logger = logging.getLogger(__name__)


def save_row(cls, row):
    object = cls(**row)
    session = db.session
    session.add(object)
    try:
        session.commit()
    except IntegrityError as msg:
        session.rollback()
        print(msg)


def process_file(cls, file):
    with open(file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            save_row(cls, row)


if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../docs/"))
    model_file = {
        Course: 'course.csv',
        Education: 'education.csv',
        OccupationArea: 'occupation_area.csv',
        Technology: 'technology.csv',
        Visa: 'visa.csv'
    }
    for cls, file_path in model_file.items():
        logger.info('Processing file.... "{}" '.format(file_path))
        process_file(cls, path+'/'+file_path)
        logger.info('File "{}" processed'.format(file_path))
