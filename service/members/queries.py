from service.members.models import Member


def get_members(*args, **kwargs):
    return Member.query.all()