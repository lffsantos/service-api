import json

import re
from flask import url_for, render_template
from service.email import send_email, generate_confirmation_token
from service.members.exceptions import (
    AuxModelNotFound, InvalidArgument,
    MemberNotFound)
from service.members.models import Member, Technology


def get_members(args):
    query = ()
    filter_tech = False
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
            filter_tech = True
            query += (Technology.id.in_(values), )
        elif key == 'ge_ids':
            query += (Member.gender_id.in_(values), )
        elif key == 'ex_ids':
            query += (Member.experience_time_id.in_(values), )

    query += (Member.confirmed==True, )
    if filter_tech:
        result = list(Member.query.join(Member.technologies).filter(*query).order_by(
            Member.full_name.asc())
        )
    else:
        result = list(Member.query.filter(*query).order_by(Member.full_name.asc()))

    return result


def add_member(gender_id, full_name, short_name, birth, email, about, linkedin, github,
               phone, experience_time_id, education_id, course_id, visa_id,
               occupation_area_id, technologies, is_working):

    member = Member(
        gender_id=gender_id, full_name=full_name, short_name=short_name,  birth=birth,
        email=email, confirmed=False, about=about, phone=phone, linkedin=linkedin,
        github=github, course_id=course_id,  visa_id=visa_id, education_id=education_id,
        experience_time_id=experience_time_id, is_working=is_working,
        occupation_area_id=occupation_area_id
    )

    member.save_or_update(technologies)

    token = generate_confirmation_token(member.email)
    confirm_url = url_for('api_v1.confirm_email', token=token, _external=True)
    template = render_template('confirm_email.html', confirm_url=confirm_url)
    send_email(member.email, subject="Please confirm you email", template=template)
    return member


def add_aux_model(cls, *args):
    param = args[0]
    try:
        instance = cls(**param)
        return instance.save_or_update()
    except TypeError as error:
        m = re.search(r"'(?:(.+?))'", error.args[0])
        value = m.group(1)
        raise InvalidArgument(cls.__name__, value)


def get_aux_model_by_id(cls, id_model):
    result = cls.query.get(id_model)
    if result:
        return result

    raise AuxModelNotFound(cls.__name__, 'id', id_model)


def get_member_by_email(email):
    result = Member.query.filter_by(email=email).first()
    if result:
        return result

    raise MemberNotFound(email=email)


def get_all(cls):
    return cls.query.all()