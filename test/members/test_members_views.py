from flask import url_for, jsonify
from service.members.models import Member
from test.gen import populate_database_for_members


# def test_members(client, populate_database_for_members):
#     response = client.get(url_for('api_v1.members'))
#     members = Member.query.all()
#     assert response.json == jsonify({'members': members}).json
#     assert response.status_code == 200
