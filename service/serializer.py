from flask.json import JSONEncoder
from service.members.models import Member, Education, Visa, Course, Technology, OccupationArea


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


def dump_choice(value):
    """Deserialize Choide object into string form for JSON processing."""
    if value is None:
        return None
    return value.code


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Member):
            return {
                'id': obj.id,
                'gender': dump_choice(obj.gender),
                'full_name': obj.full_name,
                'short_name': obj.short_name,
                'birth': obj.age(),
                'email': obj.email,
                'about': obj.about,
                'confirmed': obj.confirmed,
                'update_at': dump_datetime(obj.update_at),
                'linkedin': obj.linkedin,
                'phone': obj.phone,
                'experience_time': dump_choice(obj.experience_time),
                'education': obj.education.serialize,
                'course': obj.course.serialize,
                'visa': obj.visa.serialize,
                'occupation_area': obj.occupation_area.serialize,
                'technologies': obj.serialize_technologies,
                'is_working': obj.is_working,
            }
        if isinstance(obj, Education) or isinstance(obj, Visa) or isinstance(obj, Course) \
                or isinstance(obj, Technology) or isinstance(obj, OccupationArea):
            return obj.serialize

        return super(MyJSONEncoder, self).default(obj)
