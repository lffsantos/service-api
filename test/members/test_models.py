import copy
import pytest
from datetime import date

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
def test_create(session, test_case):
    session.add(test_case)
    session.commit()
    assert test_case.__class__.query.all()[0] == test_case


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
    session.add(test_case)
    session.commit()
    assert not test_case.__class__.query.all()[0].__dict__[attribute] == expected
    setattr(test_case, attribute, expected)
    session.add(test_case)
    session.commit()
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
    session.add(test_case)
    session.commit()
    assert test_case.__class__.query.all()[0] == test_case
    session.delete(test_case)
    session.commit()
    assert not test_case.__class__.query.all()


@pytest.mark.parametrize('test_case', [gen.fake_data()])
def test_save_member(session, test_case):
    database = copy.deepcopy(test_case['database'])
    if database.get('members'):
        del database['members']
    gen.insert_database(session, database)
    member = Member(
        full_name='Lucas Farias', gender_id=1, short_name='Lucas', birth=date.today(),
        email='example@gmail.com', is_working=False, visa_id=1, education_id=1, course_id=1,
        occupation_area_id=1
    )
    session.add(member)
    for tech in database['technologies']:
        member.technologies.append(tech)
    session.commit()

    result = Member.query.all()[0]
    for key, value in test_case['expected'].items():
        if key == 'technologies':
            assert all([r.name in value for r in result.technologies])
        else:
            assert result.__dict__[key] == value


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
