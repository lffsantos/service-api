from decouple import config
from flask import request, jsonify
from service import api_v1
from service.members.models import Member
from itsdangerous import BadSignature
from itsdangerous import URLSafeSerializer as Serializer


@api_v1.route("/members", methods=['GET'])
def members():
    payload = request.get_json()
    # TODO: apply filter later
    result = {'members': Member.query.all()}
    return jsonify(result), 200


@api_v1.route("/member/create", methods=['POST'])
def member_create():
    pass


@api_v1.route("/member/<token>/update", methods=['PUT'])
def member_update(token):
    pass


@api_v1.route("/member/<hash_id>/detail", methods=['GET'])
def member_detail(hash_id):
    s = Serializer(config('SECRET_KEY'))
    try:
        id = s.loads(hash_id)
    except BadSignature:
        raise Exception("Invalid Id")




