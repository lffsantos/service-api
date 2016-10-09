import json
import time
import slumber


class MeetupApi(object):

    def __init__(self):
        self.base_url_api = 'https://api.meetup.com'

    def get_event_cards(self, group_name):
        api = slumber.API(self.base_url_api, format="json", append_slash=False)
        event_card = api.oembed.get(url='http://www.meetup.com/{0}/events/'.format(group_name))
        # sometimes, ocurrer delay on server delay to retrieve data,
        # therefore this loop retry three times, after this, likely
        # is a real error
        retry = 3
        while retry >= 0:
            try:
                event_card = json.loads(event_card.decode('utf-8'))['html'].replace('\n', '')
                break
            except AttributeError:
                retry -= 1
                time.sleep(2)
        return event_card


