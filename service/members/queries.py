import json
import re

from flask import url_for, render_template
from service.email import send_email, generate_confirmation_token, is_email_address_valid
from service.members.exceptions import (
    AuxModelNotFound, InvalidArgument, MemberNotFound,
    InvalidValueError)
from service.members.models import Member, Technology


def get_members(args):
    query = ()
    filter_tech = False
    for key, values in args.items():
        values = json.loads(values)
        if values:
            if key == 'education_ids':
                query += (Member.education_id.in_(values), )
            elif key == 'course_ids':
                query += (Member.course_id.in_(values), )
            elif key == 'visa_ids':
                query += (Member.visa_id.in_(values), )
            elif key == 'occupation_ids':
                query += (Member.occupation_area_id.in_(values), )
            elif key == 'technology_ids':
                filter_tech = True
                query += (Technology.id.in_(values), )
            elif key == 'gender_ids':
                query += (Member.gender_id.in_(values), )
            elif key == 'experience_ids':
                query += (Member.experience_time_id.in_(values), )

    query += (Member.confirmed, )
    if filter_tech:
        result = list(Member.query.join(Member.technologies).filter(*query).order_by(
            Member.full_name.asc())
        )
    else:
        result = list(Member.query.filter(*query).order_by(Member.full_name.asc()))

    return result


def add_member(args):
    email = args.get('email')
    if not email or not is_email_address_valid(email):
        raise InvalidValueError('email', email, None, reason='invalid email')
    full_name = args.get('full_name')
    if not full_name:
        raise InvalidValueError('full_name', full_name, None, reason='can not be None')
    elif len(full_name) < 5:
        raise InvalidValueError('full_name', full_name, None, reason='too short')

    member = Member()
    technologies = args.pop('technologies', None)
    member.fill_member(args)
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