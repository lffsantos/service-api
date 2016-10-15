import json
from flask import request, jsonify
from flask.ext.restplus import Resource

from service import cache, api_v1
from service.events.meetup_api import MeetupApi


@api_v1.route('/events_meetup', endpoint='events_meetup', doc=False)
class EventsMeetup(Resource):
    @cache.cached(timeout=3600, key_prefix='events_meetup')
    def get(self):
        """Receive a list of group and return a next meetup for this groups."""
        groups_meetup = json.loads(request.args.get('groups_meetup'))
        meetup_api = MeetupApi()
        card = ''
        for group in groups_meetup:
            card += meetup_api.get_event_cards(group)
        return jsonify({'html': card})


# @api_v1.route('/clear_all_caches', methods=['POST'])
def clear_all_caches():
    cache.delete('events_meetup')
    return jsonify({'ok': 'ok'})
