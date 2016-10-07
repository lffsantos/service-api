import json
import re
from flask import url_for
import pytest
import service


@pytest.fixture
def app():
    service.app.config['SERVER_NAME'] = "TEST_SERVER"
    service.app.config['TESTING'] = True
    return service.app


@pytest.mark.parametrize('test_case', [
    {'groups_meetup': json.dumps(['pythonireland'])},
    {'groups_meetup': json.dumps(['pythonireland', 'django-dublin'])},
])
def test_get_event_cards(client, test_case):
    response = client.get(url_for('api_v1.events_meetup'), query_string=test_case)
    for group in json.loads(test_case['groups_meetup']):
        url = "http://www.meetup.com/{0}/".format(group)
        assert re.search(url, response.json['html'])
