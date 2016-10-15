import json
import copy
import pytest
from flask import url_for, jsonify

from service.members import queries
from service.members.models import *
from test.gen import populate_database_for_members


class TestMembers:

    def test_list_members(self, client, populate_database_for_members):
        response = client.get(url_for('api_v1.members'))
        members = queries.get_members({})
        assert response.json == jsonify({'members': members}).json
        assert response.status_code == 200


class TestAuxModels:

    @pytest.mark.parametrize('cls, url', [
        (Education, 'api_v1.educations'),
        (Visa, 'api_v1.visas'),
        (OccupationArea, 'api_v1.occupations'),
        (Technology, 'api_v1.technologies'),
        (Course, 'api_v1.courses'),
        (Gender, 'api_v1.genders'),
        (ExperienceTime, 'api_v1.experiences'),
    ])
    def test_models_list(self, client, cls, url, populate_database_for_members):
        response = client.get(url_for(url))
        assert response.json == jsonify({cls.__name__: list(cls.query.all())}).json
        assert response.status_code == 200

    @pytest.mark.parametrize('cls, url, obj_id', [
        (Education, 'api_v1.education', 1),
        (Visa, 'api_v1.visa', 1),
        (OccupationArea, 'api_v1.occupation', 1),
        (Technology, 'api_v1.technology', 1),
        (Course, 'api_v1.course', 1),
        (Gender, 'api_v1.gender', 1),
        (ExperienceTime, 'api_v1.experience', 1),
    ])
    def test_models_get_item(self, client, cls, url, obj_id, populate_database_for_members):
        response = client.get(url_for(url, obj_id=obj_id))
        assert response.json == jsonify(cls.query.get(obj_id).serialize).json
        assert response.status_code == 200

    @pytest.mark.parametrize('url, args', [
        ('api_v1.educations', {'level': 'teste'}),
        ('api_v1.visas', {'name': 'teste', 'description': 'desc'}),
        ('api_v1.occupations', {'name': 'test'}),
        ('api_v1.technologies', {'name': 'test'}),
        ('api_v1.courses', {'name': 'test'}),
        ('api_v1.genders', {'name': 'test'}),
        ('api_v1.experiences', {'name': 'test'}),
    ])
    def test_models_post(self, session, client, url, args):
        expected = copy.copy(args)
        expected['id'] = 1
        response = client.post(
            url_for(url), data=json.dumps(args), content_type='application/json'
        )
        assert response.json == expected
        assert response.status_code == 201
