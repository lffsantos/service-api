from datetime import datetime
from service import db
from service.members.models import Member, Technology


def get_members(*args, **kwargs):
    education_id = kwargs.get('education_id')
    visa_id = kwargs.get('visa_id')
    occupation_area = kwargs.get('occupation_area_id')
    technologies = kwargs.get('technologies')
    is_working = kwargs.get('is_working')
    confirmed = kwargs.get('confirmed')
    return Member.query.all()


def add_member(gender, full_name, short_name, birth, email, about, linkedin, github,
               phone, experience_time, education_id, course_id, visa_id, occupation_area_id,
               technologies, is_working):

    session = db.session
    if isinstance(birth, str):
        # birth receive date in string format ddmmyyyy
        try:
            birth = datetime.strptime(birth, '%d%m%Y')
        except ValueError:
            raise ValueError('invalid format for birth receive {} expected {}'.format(birth, 'ddmmyyy'))

    member = Member(gender=gender, full_name=full_name, short_name=short_name, birth=birth, email=email,
                    confirmed=False, about=about, linkedin=linkedin, github=github, phone=phone,
                    experience_time=experience_time, education_id=education_id, course_id=course_id,
                    visa_id=visa_id, occupation_area_id=occupation_area_id, is_working=is_working
                    )

    session.add(member)

    if technologies:
        for tech in Technology.query.filter(Technology.id.in_(technologies)):
            member.technologies.append(tech)

    session.commit()

    return member


def add_aux_model(cls, *args):
    session = db.session
    param = args[0]
    instance = cls(**param)
    session.add(instance)
    session.commit()
    return instance
