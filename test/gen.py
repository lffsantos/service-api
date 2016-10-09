from datetime import date
from service import Education, Course, Visa, OcupationArea, Technology, Member

__author__ = 'lucas'


def insert_database(session, models):

    for education in models.get('educations', []):
        session.add(education)
    for course in models.get('courses', []):
        session.add(course)
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
            'ocupations': [OcupationArea(name='Devops'), OcupationArea(name='Backend')],
            'technologies': [
                Technology(name='Java'), Technology(name='Python'), Technology(name='Django'), Technology(name='Flask')
            ],
            'members': [
                Member(
                    full_name='Lucas Farias', gender='male', short_name='Lucas', birth=date.today(),
                    email='example@gmail.com', is_work=False, visa_id=1, education_id=1, course_id=1,
                    ocupation_area_id=1
                )
            ]
        },
        'expected': {
            'full_name': 'Lucas Farias', 'gender': 'male', 'short_name': 'Lucas',
            'birth': date.today(), 'email': 'example@gmail.com',
            'education_id': 1, 'course_id': 1, 'visa_id': 1, 'ocupation_area_id': 1,
            'is_work': False,
            'technologies': ['Java', 'Python', 'Django', 'Flask'],
        },
    }
