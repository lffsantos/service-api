import json

from flask import request, jsonify
from service import api_v1, cache
from service.events.meetup_api import MeetupApi


@api_v1.route('/events_meetup', methods=['GET'])
@cache.cached(timeout=3600, key_prefix='events_meetup')
def events_meetup():
    """Receive a list of group and return a next meetup for this groups."""
    groups_meetup = json.loads(request.args.get('groups_meetup'))
    meetup_api = MeetupApi()
    card = ''
    for group in groups_meetup:
        card += meetup_api.get_event_cards(group)
    return jsonify({'html': card}), 200


@api_v1.route('/clear_all_caches', methods=['POST'])
def clear_all_caches():
    cache.delete('events_meetup')
    return jsonify({'ok': 'ok'})
