import json
import re
import pytest
from flask import url_for


@pytest.mark.parametrize('test_case', [
    {'groups_meetup': json.dumps(['pythonireland'])},
    {'groups_meetup': json.dumps(['pythonireland', 'django-dublin'])},
])
def test_get_event_cards(client, test_case):
    response = client.get(url_for('api_v1.events_meetup'), query_string=test_case)
    for group in json.loads(test_case['groups_meetup']):
        url = "http://www.meetup.com/{0}/".format(group)
        assert re.search(url, response.json['html'])
