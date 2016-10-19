from flask.json import JSONEncoder

from service.members.models import *


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Member) or isinstance(obj, Education) or isinstance(obj, Visa) \
                or isinstance(obj, Course) or isinstance(obj, Technology) \
                or isinstance(obj, OccupationArea) or isinstance(obj, Gender) \
                or isinstance(obj, ExperienceTime):

            return obj.serialize

        return super(MyJSONEncoder, self).default(obj)
