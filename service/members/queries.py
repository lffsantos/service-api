import json

from datetime import datetime
from service import db
from service.members.models import Member, Technology


def get_members(args):
    query = ()
    for key, values in args.items():
        values = json.loads(values)
        if key == 'ed_ids':
            query += (Member.education_id.in_(values), )
        elif key == 'co_ids':
            query += (Member.course_id.in_(values), )
        elif key == 'vi_ids':
            query += (Member.visa_id.in_(values), )
        elif key == 'oc_ids':
            query += (Member.occupation_area_id.in_(values), )
        elif key == 'te_ids':
            query += (Member.technologies.in_(values), )
        elif key == 'ge_ids':
            query += (Member.gender_id.in_(values), )
        elif key == 'ex_ids':
            query += (Member.experience_time_id.in_(values), )

    query += (Member.confirmed==True, )
    return list(Member.query.filter(*query).order_by(Member.full_name.asc()))


def add_member(gender_id, full_name, short_name, birth, email, about, linkedin, github,
               phone, experience_time_id, education_id, course_id, visa_id, occupation_area_id,
               technologies, is_working):

    session = db.session
    if isinstance(birth, str):
        # birth receive date in string format ddmmyyyy
        try:
            birth = datetime.strptime(birth, '%d%m%Y')
        except ValueError:
            raise ValueError('invalid format for birth receive {} expected {}'.format(birth, 'ddmmyyy'))

    member = Member(gender_id=gender_id, full_name=full_name, short_name=short_name, birth=birth, email=email,
                    confirmed=False, about=about, linkedin=linkedin, github=github, phone=phone,
                    experience_time_id=experience_time_id, education_id=education_id, course_id=course_id,
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


def get_aux_model_by_id(cls, id_model):
    return cls.query.get(id_model)


def get_all(cls):
    return cls.query.all()