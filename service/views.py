from service import api_v1


@api_v1.route("/")
def hello():
    return "Hello World!"
