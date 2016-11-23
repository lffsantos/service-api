from service.members.models import (
    Visa, Gender, ExperienceTime, Course, OccupationArea, Education, Technology
)

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
        for item in model.query.all():
            element['children'].append({
                'id': '{}_{}'.format(item.id, name),
                'text': item.name
            })
        data.append(element)

    return data