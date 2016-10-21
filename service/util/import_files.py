import csv
import json
import logging
import os

from service import db
from service.members.exceptions import AuxModelAlreadyExists, MemberAlreadyExists
from service.members.models import (
    Course, Education, OccupationArea, Technology, Visa, ExperienceTime, Gender,
    Member)
from sqlalchemy.exc import IntegrityError


logger = logging.getLogger(__name__)


def _format_row_member(member, row):
    row['confirmed'] = True if row['confirmed'] == 'true' else False
    row['is_working'] = True if row['is_working'] == 'true' else False
    convert_to_int = [
        'visa_id', 'gender_id', 'occupation_area_id', 'education_id',
        'course_id', 'experience_time_id'
    ]
    for name_row in convert_to_int:
        row[name_row] = int(row[name_row])
    for key, value in row.items():
        if key == 'technologies':
            continue
        setattr(member, key, value)

    return member


def save_row(cls, row):
    try:
        if cls is Member:
            member = cls()
            _format_row_member(member, row)
            member.save_or_update(row['technologies'])
        else:
            object = cls(**row)
            object.save_or_update()
    except (AuxModelAlreadyExists, MemberAlreadyExists) as error:
        msg = {'field_key': error.key, 'field_value': error.value}
        if error.__class__ is MemberAlreadyExists:
            msg['error'] = 'MemberAlreadyExists'
        else:
            msg['error'] = '{}AlreadyExists'.format(error.cls_name)
        print(msg)
        return False

    return True


def process_file(cls, file):
    insert_data = 0
    with open(file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if save_row(cls, row):
                insert_data += 1

    return insert_data


def run_importer():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../docs/"))
    model_file = [
        (Course, 'course.csv'),
        (Education, 'education.csv'),
        (OccupationArea, 'occupation_area.csv'),
        (Technology, 'technology.csv'),
        (Visa, 'visa.csv'),
        (Gender, 'gender.csv'),
        (ExperienceTime, 'experience_time.csv'),
        (Member, 'member.csv')
    ]
    save_data = []
    for model in model_file:
        cls, file_path = model
        logging.info('Processing file.... "{}" '.format(file_path))
        insert_data = process_file(cls, path+'/'+file_path)
        logging.info('File "{}" processed'.format(file_path))
        save_data.append((cls, insert_data))

    return save_data
