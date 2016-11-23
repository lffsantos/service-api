from flask.json import JSONEncoder

from service.members.models import *
from service.members.models.aux_models import BaseModel


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Member) or isinstance(obj, BaseModel):
            return obj.serialize

        return super(MyJSONEncoder, self).default(obj)
