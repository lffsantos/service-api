import copy
import pytest
from service.members.models import Member, Education, Course, Visa, OccupationArea, Technology, ExperienceTime, Gender
from service.members.queries import add_member, add_aux_model
from test import gen


@pytest.mark.parametrize('test_case', [
    {
        'data': gen.fake_data(),
        'args': (1, 'lucas farias', 'lucas', '01101987', 'test@gmail.com', '',  '',  '', '',
                 1, 1, 1, 1, 1, [1, 2, 3], True),
        'expected_error': False,
    },
    {
        'data': gen.fake_data(),
        'args': (1, 'lucas farias', 'lucas', '1111111111', 'test@gmail.com', '',  '',  '', '',
                 1, 1, 1, 1, 1, [1, 2, 3], True),
        'expected_error': ValueError,
    }
])
def test_add_member(session, test_case):
    database = copy.deepcopy(test_case['data']['database'])
    database.pop('members')
    gen.insert_database(session, database)
    if test_case['expected_error']:
        with pytest.raises(test_case['expected_error']):
            add_member(*test_case['args'])
    else:
        member = add_member(*test_case['args'])
        assert Member.query.get(member.id)


@pytest.mark.parametrize('test_case', [
    {
        'cls': Education,
        'args': {'level': 'superior'},
        'expected_error': False,
    },
    {
        'cls': Course,
        'args': {'name': 'Engenharia'},
        'expected_error': False,
    },
    {
        'cls': Visa,
        'args': {'name': 'Stamp2', 'description': 'estudante'},
        'expected_error': False,
    },
    {
        'cls': OccupationArea,
        'args': {'name': 'backend'},
        'expected_error': False,
    },
    {
        'cls': Technology,
        'args': {'name': 'Java'},
        'expected_error': False,
    },
    {
        'cls': Gender,
        'args': {'name': 'Male'},
        'expected_error': False,
    },
    {
        'cls': ExperienceTime,
        'args': {'name': 'No Experience'},
        'expected_error': False,
    },
])
def test_add_aux_models(session, test_case):
    cls = test_case['cls']
    model = add_aux_model(cls, test_case['args'])
    assert cls.query.get(model.id).serialize == model.serialize