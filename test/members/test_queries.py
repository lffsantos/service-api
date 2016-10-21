import copy
import pytest

from service.members.exceptions import (
    InvalidArgument, InvalidValueError, AuxModelNotFound, MemberNotFound
)
from service.members.queries import add_member, add_aux_model, get_aux_model_by_id, \
    get_member_by_email
from service.members.models import *

from test import gen


@pytest.mark.parametrize('test_case', [
    {
        'data': gen.fake_data(),
        'args': (1, 'lucas farias', 'lucas', '01101987', 'test@gmail.com', '',  '',  '',
                 '', 1, 1, 1, 1, 1, "[1, 2, 3]", True),
        'expected_error': False,
    },
    {
        'data': gen.fake_data(),
        'args': (1, 'lucas farias', 'lucas', '1111111111', 'test@gmail.com', '',  '',  '',
                 '', 1, 1, 1, 1, 1, "[1, 2, 3]", True),
        'expected_error': InvalidValueError,
    },
    {
        'data': gen.fake_data(),
        'args': {
            'full_name': 'Teste', 'gender_id': 'a', 'short_name': 'Lucas', 'visa_id': 1,
            'birth': '01012010', 'email': 'example@gmail.com', 'about': '',
            'is_working': False, 'education_id': 1, 'course_id': 1,
            'experience_time_id': 1, 'phone': '111', 'linkedin': '', 'github': '',
            'occupation_area_id': 1, 'technologies': "[1, 2, 3, 4]",
        },
        'unpack': dict,
        'expected_error': InvalidValueError,
    }
])
def test_add_member(session, test_case):
    database = copy.deepcopy(test_case['data']['database'])
    database.pop('members')
    gen.insert_database(session, database)
    if test_case['expected_error']:
        with pytest.raises(test_case['expected_error']):
            if test_case.get('unpack') is dict:
                add_member(**test_case['args'])
            else:
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


@pytest.mark.parametrize('cls, args', [
    (Education, {'level': 'teste', 'sds': 'teste'}),
    (Visa, {'name2': 'stamp2', 'description': 'Estudante'}),
    (OccupationArea, {'nadsds': 'devops'}),
    (Technology, {'namdsdds': 'java'}),
    (Course, {'nawww': 'ti'}),
    (Gender, {'invalidww': 'male'}),
    (ExperienceTime, {'invalid': 'n experience'}),
    (Member, {'invalid': 'n experience'}),
])
def test_save_invalid_argument_error(session, cls, args):
    with pytest.raises(InvalidArgument):
        add_aux_model(cls, args)


@pytest.mark.parametrize('cls, id', [
    (Education, 1),
    (Visa, 2),
    (OccupationArea, 1),
    (Technology, 1),
    (Course, 1),
    (Gender, 1),
    (ExperienceTime, 1),
])
def test_aux_model_not_found(session, cls, id):
    with pytest.raises(AuxModelNotFound):
        get_aux_model_by_id(cls, id)


@pytest.mark.parametrize('fake_data, email, exception', [
    (gen.fake_data(), 'example@gmail.com', False),
    (gen.fake_data(), 'not@gmail.com', MemberNotFound),
])
def test_get_member_by_email(session, email, exception, fake_data):
    gen.insert_database(session, fake_data['database'])
    if exception:
        with pytest.raises(MemberNotFound):
            get_member_by_email(email)
    else:
        assert get_member_by_email(email)
