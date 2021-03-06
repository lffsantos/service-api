import json
import copy
import pytest
from flask import url_for, jsonify

from service.members import queries
from service.members.models import *
from service.members.models.aux_models import Level
from test import gen
from test.gen import populate_database_for_members


class TestMembers:
    @pytest.mark.parametrize('test_case', [
        {
            'filters': {
                'ed_ids': json.dumps([1, 2]),
                'te_ids': json.dumps([4, 3])
            },
            'expected_result': 1
        },
        {
            'filters': {
                'co_ids': json.dumps([1, 2]),
                'vi_ids': json.dumps([1])
            },
            'expected_result': 2
        },
        {
            'filters': {
                'oc_ids': json.dumps([1, 2]),
                'ge_ids': json.dumps([2])
            },
            'expected_result': 1
        },
        {
            'filters': {
                'ex_ids': json.dumps([3, 4]),
                'oc_ids': json.dumps([2])
            },
            'expected_result': 0
        },
    ])
    def test_list_members(self, client, test_case, populate_database_for_members):
        response = client.get(
            url_for('api_v1.members'), query_string=test_case['filters']
        )
        members = queries.get_members(test_case['filters'])
        assert len(response.json) == len(members)
        assert response.status_code == 200

    @pytest.mark.parametrize('test_case', [
        {
            'database': {
                'educations': [
                    Education(name='Superior Completo'),
                    Education(name='Superior Incompleto')
                ],
                'courses': [Course(name='Engenharia'), Course(name='Analise de Sistema')],
                'visas': [
                    Visa(name='Stamp2'),
                    Visa(name='Stamp4')
                ],
                'occupations': [
                    OccupationArea(name='Devops'),
                    OccupationArea(name='Backend')
                ],
                'technologies': [
                    Technology(name='Java'), Technology(name='Python'),
                    Technology(name='Django'), Technology(name='Flask')
                ],
                'genders': [
                    Gender(name='Male'),
                    Gender(name='Female'),
                ],
                'experience_times': [
                    ExperienceTime(name='No Experience'),
                    ExperienceTime(name='< 1 year'),
                    ExperienceTime(name='1 - 2 years'),
                    ExperienceTime(name='2 - 4 years'),
                    ExperienceTime(name='4 - 6 years'),
                    ExperienceTime(name='6 - 8 years'),
                    ExperienceTime(name='8 - 10 years'),
                    ExperienceTime(name='> 10 years'),
                ],
            },
            'member': {
                'full_name': 'Teste', 'gender_id': 1, 'short_name': 'Lucas',
                'birth': '01012010', 'email': 'example@gmail.com', 'about': '',
                'is_working': False, 'education_id': 1, 'course_id': 1, 'visa_id': 1,
                'experience_time_id': 1, 'phone': '111', 'linkedin': '', 'github': '',
                'occupation_area_id': 1, 'technologies': "[1, 2, 3, 4]",
            }
        }
    ])
    def test_add_member(self, client, session, test_case):
        gen.insert_database(session, test_case['database'])
        data = test_case['member']
        response = client.post(
            url_for('api_v1.members'), data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 201

    @pytest.mark.parametrize('test_case', [
        {
            'database': {
                'educations': [
                    Education(name='Superior Completo'),
                ],
                'courses': [Course(name='Engenharia')],
                'visas': [
                    Visa(name='Stamp2'),
                ],
                'occupations': [
                    OccupationArea(name='Devops'),
                ],
                'technologies': [
                    Technology(name='Java'), Technology(name='Python')
                ],
                'genders': [
                    Gender(name='Male'),
                ],
                'experience_times': [
                    ExperienceTime(name='No Experience'),
                ],
            },
            'member': {
                'full_name1': 'Teste',
            }
        }
    ])
    def test_add_member_invalid_argument(self, client, session, test_case):
        gen.insert_database(session, test_case['database'])
        data = test_case['member']
        response = client.post(
            url_for('api_v1.members'), data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 400

    @pytest.mark.parametrize('test_case, payload', [
        (gen.fake_data(),
         {
             'full_name': 'Teste', 'gender_id': 'a', 'short_name': 'Lucas', 'visa_id': 1,
             'birth': '01012010', 'email': 'example@gmail.com', 'about': '',
             'is_working': False, 'education_id': 1, 'course_id': 1,
             'experience_time_id': 1, 'phone': '111', 'linkedin': '', 'github': '',
             'occupation_area_id': 1, 'technologies': [1, 2, 3, 4],
         }
        )
    ])
    def test_add_member_invalid_value(self, client, session, test_case, payload):
        database = copy.deepcopy(test_case)
        if database.get('members'):
            del database['members']
        gen.insert_database(session, database)
        data = payload
        response = client.post(
            url_for('api_v1.members'), data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 400

    @pytest.mark.parametrize('url, email, error', [
        ('api_v1.members', {'email': 'email@email.com'}, 'MemberNotFound'),
    ])
    def test_member_handle_not_found(self, session, client, url, email, error):
        response = client.get(
            url_for(url), query_string=email
        )
        assert response.json['error'] == error
        assert response.status_code == 404

    @pytest.mark.parametrize('test_case', [
        {
            'database': {
                'educations': [
                    Education(name='Superior Completo'),
                ],
                'courses': [Course(name='Engenharia'), Course(name='Analise de Sistema')],
                'visas': [
                    Visa(name='Stamp2'),
                ],
                'occupations': [
                    OccupationArea(name='Devops'),
                ],
                'technologies': [
                    Technology(name='Java'), Technology(name='Python'),
                ],
                'genders': [
                    Gender(name='Male'),
                ],
                'experience_times': [
                    ExperienceTime(name='No Experience'),
                ],
            },
            'member': {
                'full_name': 'Teste', 'gender_id': 1, 'short_name': 'Lucas',
                'birth': '01012010', 'email': 'example@gmail.com', 'about': '',
                'is_working': False, 'education_id': 1, 'course_id': 1, 'visa_id': 1,
                'experience_time_id': 1, 'phone': '111', 'linkedin': '', 'github': '',
                'occupation_area_id': 1, 'technologies': "[1, 2, 3, 4]",
            }
        }
    ])
    def test_member_handler_already_exist_and_invalid_key_constraint(self, client, session, test_case):
        gen.insert_database(session, test_case['database'])
        data = test_case['member']
        response = client.post(
            url_for('api_v1.members'), data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 201
        response = client.post(
            url_for('api_v1.members'), data=json.dumps(data),
            content_type='application/json'
        )
        assert response.json['error'] == 'MemberAlreadyExists'
        assert response.status_code == 409

        # invalid 'education_id' change email and full_name
        data['email'] = 'new_email@gmail.com'
        data['full_name'] = 'new_name'
        data['education_id'] = 0
        response = client.post(
            url_for('api_v1.members'), data=json.dumps(data),
            content_type='application/json'
        )
        assert response.json['error'] == 'InvalidKeyConstraint'
        assert response.status_code == 400


class TestAuxModels:
    @pytest.mark.parametrize('cls, url', [
        (Education, 'api_v1.educations'),
        (Visa, 'api_v1.visas'),
        (OccupationArea, 'api_v1.occupations'),
        (Technology, 'api_v1.technologies'),
        (Course, 'api_v1.courses'),
        (Gender, 'api_v1.genders'),
        (ExperienceTime, 'api_v1.experiences'),
        (Level, 'api_v1.levels'),
    ])
    def test_models_list(self, client, cls, url, populate_database_for_members):
        response = client.get(url_for(url))
        assert response.json == jsonify(cls.query.all()).json
        assert response.status_code == 200

    @pytest.mark.parametrize('cls, url, obj_id', [
        (Education, 'api_v1.education', 1),
        (Visa, 'api_v1.visa', 1),
        (OccupationArea, 'api_v1.occupation', 1),
        (Technology, 'api_v1.technology', 1),
        (Course, 'api_v1.course', 1),
        (Gender, 'api_v1.gender', 1),
        (ExperienceTime, 'api_v1.experience', 1),
        (Level, 'api_v1.level', 1),
    ])
    def test_models_get_item(self, client, cls, url, obj_id,
                             populate_database_for_members):
        response = client.get(url_for(url, obj_id=obj_id))
        assert response.json == jsonify(cls.query.get(obj_id).serialize).json
        assert response.status_code == 200

    @pytest.mark.parametrize('url, id, error', [
        ('api_v1.education', 1, 'EducationNotFound'),
        ('api_v1.visa', 1, 'VisaNotFound'),
        ('api_v1.occupation', 1, 'OccupationAreaNotFound'),
        ('api_v1.technology', 1, 'TechnologyNotFound'),
        ('api_v1.course', 1, 'CourseNotFound'),
        ('api_v1.gender', 1, 'GenderNotFound'),
        ('api_v1.experience', 1, 'ExperienceTimeNotFound'),
        ('api_v1.level', 1, 'LevelNotFound'),
    ])
    def test_models_handle_not_found(self, session, client, url, id, error):
        response = client.get(url_for(url, obj_id=id))
        assert response.json['error'] == error
        assert response.status_code == 404

    @pytest.mark.parametrize('url, args', [
        ('api_v1.educations', {'name': 'Superior Completo'}),
        ('api_v1.visas', {'name': 'Stamp2'}),
        ('api_v1.occupations', {'name': 'Backend'}),
        ('api_v1.technologies', {'name': 'Java'}),
        ('api_v1.courses', {'name': 'Engenharia'}),
        ('api_v1.genders', {'name': 'Male'}),
        ('api_v1.experiences', {'name': 'No Experience'}),
        ('api_v1.levels', {'name': 'Junior'}),
    ])
    def test_models_handle_already_exist(self, session, client, url, args):
        response = client.post(
            url_for(url), data=json.dumps(args), content_type='application/json'
        )
        assert response.status_code == 201

        response = client.post(
            url_for(url), data=json.dumps(args), content_type='application/json'
        )
        assert response.status_code == 409
