from decouple import config
from flask import request, jsonify
from service import api_v1
from service.members.models import Education, Visa, Course, OccupationArea, Technology
from itsdangerous import BadSignature
from itsdangerous import URLSafeSerializer as Serializer
from service.members.queries import get_members, add_aux_model, add_member


@api_v1.route("/members", methods=['GET'])
def members():
    # TODO: apply filter later
    payload = request.get_json()
    return jsonify({'members': get_members()}), 200


@api_v1.route("/member/create", methods=['POST'])
def member_create():
    payload = request.get_json()
    args = payload.get('args')
    member = add_member(**args)
    return jsonify({'ok': 'ok'}), 200


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


@api_v1.route("/education/create", methods=['POST'])
def education_create():
    payload = request.get_json()
    args = payload.get('args')
    add_aux_model(Education, args)
    return jsonify({'ok': 'ok'}), 200


@api_v1.route("/visa/create", methods=['POST'])
def visa_create():
    payload = request.get_json()
    args = payload.get('args')
    add_aux_model(Visa, args)
    return jsonify({'ok': 'ok'}), 200


@api_v1.route("/course/create", methods=['POST'])
def course_create():
    payload = request.get_json()
    args = payload.get('args')
    add_aux_model(Course, args)
    return jsonify({'ok': 'ok'}), 200


@api_v1.route("/occupation/create", methods=['POST'])
def occupation_area_create():
    payload = request.get_json()
    args = payload.get('args')
    add_aux_model(OccupationArea, args)
    return jsonify({'ok': 'ok'}), 200


@api_v1.route("/technology/create", methods=['POST'])
def technology_create():
    payload = request.get_json()
    args = payload.get('args')
    add_aux_model(Technology, args)
    return jsonify({'ok': 'ok'}), 200


