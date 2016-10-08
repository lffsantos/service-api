from service import api_v1, db
from service.members.db.models import Member


@api_v1.route("/oi")
def hello():
    return "Hello World!"