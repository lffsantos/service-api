import json
import slumber


class MeetupApi(object):

    def __init__(self):
        self.base_url_api = 'https://api.meetup.com'

    def get_event_cards(self, group_name):
        api = slumber.API(self.base_url_api, format="json", append_slash=False)
        event_card = api.oembed.get(url='http://www.meetup.com/{0}/events/'.format(group_name))
        event_card = json.loads(event_card.decode('utf-8'))['html'].replace('\n', '')
        return event_card


