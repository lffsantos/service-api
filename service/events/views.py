import json
from flask import request
from service import api_v1
from service.events.meetup_api import MeetupApi
from flask_restful import Resource


class EventsMeetup(Resource):
    """Receive a list of group and return a next meetup for this groups."""
    def get(self):
        groups_meetup = json.loads(request.args.get('groups_meetup'))
        meetup_api = MeetupApi()
        card = ''
        for group in groups_meetup:
            card += meetup_api.get_event_cards(group)

        return {'html': card}


api_v1.add_resource(EventsMeetup, '/events_meetup')