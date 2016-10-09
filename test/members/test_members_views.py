import pytest
from flask import url_for
from service.members.models import Member
from test import gen


@pytest.mark.parametrize('test_case', [gen.fake_data()])
def test_members(client, session, test_case):
    gen.insert_database(session, test_case['database'])
    member = Member.query.all()[0]
    for tech in test_case['database']['technologies']:
        member.technologies.append(tech)
    session.commit()
    response = client.get(url_for('api_v1.members'))

    assert response.status_code == 200

