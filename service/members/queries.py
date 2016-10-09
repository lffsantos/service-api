from service.members.models import Member


def get_members(*args, **kwargs):
    education_id = kwargs.get('education_id')
    visa_id = kwargs.get('visa_id')
    occupation_area = kwargs.get('occupation_area_id')
    technologies = kwargs.get('technologies')
    is_working = kwargs.get('is_working')
    confirmed = kwargs.get('confirmed')
    return Member.query.all()


def add_member(gender, full_name, short_name, birth, email, confirmed, about, linkedin, github,
               phone, experience_time, education_id, course_id, visa_id, occupation_area_id,
               technologies, is_working):

    pass


def add_course():
    pass


def add_education():
    pass


def add_visa():
    pass


def add_occupation_area():
    pass


def add_technology():
    pass