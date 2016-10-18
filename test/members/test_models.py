import copy
import pytest

from service.members.exceptions import (
    AuxModelAlreadyExists, InvalidValueError, MemberAlreadyExists
)

from service.members.models import *
from test import gen


@pytest.mark.parametrize('test_case', [
    (Education(level='Superior')),
    (Visa(name='Stamp2', description='Estudante')),
    (OccupationArea(name='Devops')),
    (Technology(name='Java')),
    (Course(name='Engenharia')),
    (Gender(name='Male')),
    (ExperienceTime(name='No experience')),
])
def test_save(session, test_case):
    test_case.save_or_update()
    assert test_case.__class__.query.all()[0] == test_case


@pytest.mark.parametrize('cls, args', [
    (Education, {'level': 'superior'}),
    (Visa, {'name': 'Stamp2', 'description': 'Estudante'}),
    (OccupationArea, {'name': 'Devops'}),
    (Technology, {'name': 'Java'}),
    (Course, {'name': 'Engenharia'}),
    (Gender, {'name': 'Male'}),
    (ExperienceTime, {'name': 'No Experience'}),
])
def test_save_exist_value(session, cls, args):
    instance = cls(**args)
    instance.save_or_update()
    with pytest.raises(AuxModelAlreadyExists):
        repeat_instance = cls(**args)
        repeat_instance.save_or_update()


@pytest.mark.parametrize('cls, args', [
    (Education, {'level': 1}),
    (Visa, {'name': 2.5, 'description': 'Estudante'}),
    (OccupationArea, {'name': 34}),
    (Technology, {'name': 1}),
    (Course, {'name': 333}),
    (Gender, {'name': 122}),
    (ExperienceTime, {'name': 454}),
])
def test_save_invalid_value_error(session, cls, args):
    with pytest.raises(InvalidValueError):
        instance = cls(**args)
        instance.save_or_update()


@pytest.mark.parametrize('test_case, attribute, expected', [
    (Education(level='Superior'), 'level', 'doutorado'),
    (Visa(name='Stamp2', description='Estudante'), 'name', 'stamp4'),
    (OccupationArea(name='Devops'), 'name', 'backend'),
    (Technology(name='Java'), 'name', 'python'),
    (Course(name='Engenharia'), 'name', 'Ciencia'),
    (Gender(name='Male'), 'name', 'Female'),
    (ExperienceTime(name='No experience'), 'name', '> 1 year'),
])
def test_edit(session, test_case, attribute, expected):
    test_case.save_or_update()
    assert not test_case.__class__.query.all()[0].__dict__[attribute] == expected
    setattr(test_case, attribute, expected)
    test_case.save_or_update()
    assert test_case.__class__.query.all()[0].__dict__[attribute] == expected


@pytest.mark.parametrize('test_case', [
    (Education(level='Superior')),
    (Visa(name='Stamp2', description='Estudante')),
    (OccupationArea(name='Devops')),
    (Technology(name='Java')),
    (Course(name='Engenharia')),
    (Gender(name='Male')),
    (ExperienceTime(name='No experience')),
])
def test_delete(session, test_case):
    test_case.save_or_update()
    assert test_case.__class__.query.all()[0] == test_case
    test_case.delete()
    assert not test_case.__class__.query.all()


@pytest.mark.parametrize('test_case', [gen.fake_data()])
def test_save_member(session, test_case):
    database = copy.deepcopy(test_case['database'])
    if database.get('members'):
        del database['members']
    gen.insert_database(session, database)
    member = Member(
        full_name='Lucas Farias', gender_id=1, short_name='Lucas', birth='01012000',
        email='example@gmail.com', is_working=False, visa_id=1, education_id=1,
        course_id=1, occupation_area_id=1, experience_time_id=1
    )
    member.save_or_update([i for i in range(1, len(database['technologies'])+1)])

    result = Member.query.all()[0]
    for key, value in test_case['expected'].items():
        if key == 'technologies':
            assert all([r.name in value for r in result.technologies])
        else:
            if key == 'birth':
                assert result.birth == member.birth
            else:
                assert result.__dict__[key] == value


@pytest.mark.parametrize('test_case', [gen.fake_data()])
def test_save_member_already_exist(session, test_case):
    database = copy.deepcopy(test_case['database'])
    if database.get('members'):
        del database['members']
    gen.insert_database(session, database)
    member = Member(
        full_name='Lucas Farias', gender_id=1, short_name='Lucas', birth='01012000',
        email='example@gmail.com', is_working=False, visa_id=1, education_id=1,
        course_id=1, occupation_area_id=1, experience_time_id=1
    )
    member.save_or_update([i for i in range(1, len(database['technologies'])+1)])
    member_repeat = Member(
        full_name='Lucas Farias', gender_id=1, short_name='Lucas', birth='01012000',
        email='example@gmail.com', is_working=False, visa_id=1, education_id=1,
        course_id=1, occupation_area_id=1, experience_time_id=1
    )
    with pytest.raises(MemberAlreadyExists):
        member_repeat.save_or_update()


@pytest.mark.parametrize('test_case', [gen.fake_data()])
def test_edit_member(session, test_case):
    gen.insert_database(session, test_case['database'])
    session.commit()
    member = Member.query.all()[0]
    for tech in test_case['database']['technologies']:
        member.technologies.append(tech)
    session.commit()
    result = Member.query.all()[0]
    for key, value in test_case['expected'].items():
        if key == 'technologies':
            assert all([r.name in value for r in result.technologies])
        else:
            assert result.__dict__[key] == value

    result.is_working = True
    technology_3 = test_case['database']['technologies'][2]
    result.technologies.remove(technology_3)
    session.commit()
    member = Member.query.all()[0]
    assert member.is_working
    assert len(member.technologies) == 3
    assert technology_3 not in member.technologies


@pytest.mark.parametrize('test_case', [gen.fake_data()])
def test_delete_member(session, test_case):
    gen.insert_database(session, test_case['database'])
    session.commit()
    member = Member.query.all()[0]
    for tech in test_case['database']['technologies']:
        member.technologies.append(tech)
    session.commit()
    result = Member.query.all()[0]
    assert result
    session.delete(result)
    session.commit()
    assert not Member.query.all()
    for tech in test_case['database']['technologies']:
        assert not tech.members.all()
