from service import db
from service.members.models import (
    Visa, Gender, ExperienceTime, Course, OccupationArea, Education, Technology,
    Member)
from service.members.models.member import member_technology
from sqlalchemy import distinct
from sqlalchemy.orm.session import Session

__author__ = 'lucas'


def filter_tree():
    aux_models = {
        'visa': Visa,
        'gender': Gender,
        'occupation': OccupationArea,
        'experience': ExperienceTime,
        'course': Course,
        'technology': Technology,
        'education': Education
    }

    data = []
    for name, model in aux_models.items():
        element = {
            'text': name,
            'id': 'hidden_'+name,
            'state': {
                'opened': False
            },
            'a_attr': {
                'class': "no_checkbox"
            },
            'children': [],
        }
        if name == 'technology':
            list_filter = db.session.query(Technology).distinct(Technology.id).join(member_technology)
        else:
            list_filter = model.query.distinct().join(Member).filter(Member.confirmed)

        for item in list_filter:
            element['children'].append({
                'id': '{}_{}'.format(item.id, name),
                'text': item.name
            })
        data.append(element)

    return data