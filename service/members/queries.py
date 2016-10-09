from service.members.models import Member


def get_members(*args, **kwargs):
    return Member.query.all()


def add_member(gender, full_name, short_name, birth, email, about, linkedin, github,
               phone, experience_time, education_id, course_id, visa_id, occupation_area_id,
               technologies, is_working):
    pass