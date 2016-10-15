from datetime import date
import pytest
from service.members.models import Education, Course, Visa, OccupationArea, Technology, Gender, ExperienceTime, Member

__author__ = 'lucas'


def insert_database(session, models):

    for education in models.get('educations', []):
        session.add(education)
    for course in models.get('courses', []):
        session.add(course)
    for gender in models.get('genders', []):
        session.add(gender)
    for experience in models.get('experience_times', []):
        session.add(experience)
    for occupations in models.get('occupations', []):
        session.add(occupations)
    for visa in models.get('visas', []):
        session.add(visa)
    for technology in models.get('technologies', []):
        session.add(technology)
    for member in models.get('members', []):
        session.add(member)
    session.commit()


def fake_data():
    return {
        'database': {
            'educations': [Education(level='Superior Completo'), Education(level='Superior Incompleto')],
            'courses': [Course(name='Engenharia'), Course(name='Analise de Sistema')],
            'visas': [Visa(name='Stamp2', description='Estudante'), Visa(name='Stamp4', description='Work')],
            'occupations': [OccupationArea(name='Devops'), OccupationArea(name='Backend')],
            'technologies': [
                Technology(name='Java'), Technology(name='Python'), Technology(name='Django'), Technology(name='Flask')
            ],
            'genders': [
                Gender(name='Male'),
                Gender(name='Female'),
            ],
            'experience_times': [
                ExperienceTime(name='No Experience'),
                ExperienceTime(name='< 1 year'),
                ExperienceTime(name='1 - 2 years'),
                ExperienceTime(name='2 - 4 years'),
                ExperienceTime(name='4 - 6 years'),
                ExperienceTime(name='6 - 8 years'),
                ExperienceTime(name='8 - 10 years'),
                ExperienceTime(name='> 10 years'),
            ],
            'members': [
                Member(
                    full_name='Lucas Farias', gender_id=1, short_name='Lucas', birth=date.today(),
                    email='example@gmail.com', is_working=False, visa_id=1, education_id=1, course_id=1,
                    occupation_area_id=1
                )
            ]
        },
        'expected': {
            'full_name': 'Lucas Farias', 'gender_id': 1, 'short_name': 'Lucas',
            'birth': date.today(), 'email': 'example@gmail.com',
            'education_id': 1, 'course_id': 1, 'visa_id': 1, 'occupation_area_id': 1,
            'is_working': False,
            'technologies': ['Java', 'Python', 'Django', 'Flask'],
        },
    }


@pytest.fixture(scope='function')
def populate_database_for_members(session):
    data = {
        'database': {
            'educations': [
                Education(level='Superior Completo'),
                Education(level='Superior Incompleto'),
                Education(level='Pos Grad'),
                Education(level='no grad'),
            ],
            'courses': [
                Course(name='Engenharia de Computação'),
                Course(name='Analise de Sistema'),
                Course(name='Ciência da Computação'),
                Course(name='Rede de Computadores'),
            ],
            'visas': [
                Visa(name='Stamp2', description='Estudante'),
                Visa(name='Stamp4', description='Work Permit'),
                Visa(name='EU-Citizen', description='Passaporte Europeu'),
            ],
            'occupations': [
                OccupationArea(name='Devops'),
                OccupationArea(name='Backend'),
                OccupationArea(name='FrontEnd'),
                OccupationArea(name='Infra'),
                OccupationArea(name='Suporte'),
            ],
            'technologies': [
                Technology(name='Java'),
                Technology(name='Python'),
                Technology(name='Django'),
                Technology(name='.Net'),
                Technology(name='SAP'),
                Technology(name='C'),
                Technology(name='Android'),
                Technology(name='IOS'),
                Technology(name='Mobile'),
                Technology(name='TDD'),
                Technology(name='C#'),
                Technology(name='HTML'),
                Technology(name='SQL'),
            ],
            'genders': [
                Gender(name='Male'),
                Gender(name='Female'),
            ],
            'experience_times': [
                ExperienceTime(name='No Experience'),
                ExperienceTime(name='< 1 year'),
                ExperienceTime(name='1 - 2 years'),
                ExperienceTime(name='2 - 4 years'),
                ExperienceTime(name='4 - 6 years'),
                ExperienceTime(name='6 - 8 years'),
                ExperienceTime(name='8 - 10 years'),
                ExperienceTime(name='> 10 years'),
            ],
            'members': [
                Member(
                    full_name='Lucas Farias', gender_id=1, short_name='Lucas', birth=date.today(), confirmed=True,
                    email='example1@gmail.com', is_working=False, visa_id=1, education_id=1, course_id=1,
                    occupation_area_id=1, linkedin='xxx', github='xxxx', about='', phone='', experience_time_id=1
                ),
                Member(
                    full_name='Joana Maria', gender_id=2, short_name='Joana', birth=date.today(), confirmed=True,
                    email='example2@gmail.com', is_working=False, visa_id=2, education_id=1, course_id=2,
                    occupation_area_id=2, linkedin='', github='', about='', phone='', experience_time_id=2
                ),
                Member(
                    full_name='Jose Silva', gender_id=1, short_name='Jose', birth=date.today(), confirmed=False,
                    email='example3@gmail.com', is_working=True, visa_id=1, education_id=3, course_id=1,
                    occupation_area_id=3, linkedin='', github='', about='', phone='', experience_time_id=3
                ),
                Member(
                    full_name='João Paulo', gender_id=1, short_name='Joaao', birth=date.today(), confirmed=True,
                    email='example4@gmail.com', is_working=True, visa_id=1, education_id=4, course_id=3,
                    occupation_area_id=2, linkedin='', github='', about='', phone='', experience_time_id=2
                ),
                Member(
                    full_name='Pedro Paulo', gender_id=1, short_name='pedroa', birth=date.today(), confirmed=True,
                    email='example5@gmail.com', is_working=True, visa_id=2, education_id=2, course_id=3,
                    occupation_area_id=1, linkedin='', github='', about='', phone='', experience_time_id=3
                ),
            ],
            'member_technologies': [
                {1: [1, 2, 3, 4]},
                {2: [3, 7, 1, 5, 8]},
                {3: [9, 2, 6]},
                {4: [1, 2, 3, 4, 5, 6, 7, 8, 9]},
                {5: [12]}
            ]
        }
    }
    insert_database(session, data['database'])
    for member_tech in data['database'].get('member_technologies', []):
        for member_id, technologies in member_tech.items():
            member = Member.query.get(member_id)
            for tech_id in technologies:
                member.technologies.append(data['database']['technologies'][tech_id])
            session.commit()
