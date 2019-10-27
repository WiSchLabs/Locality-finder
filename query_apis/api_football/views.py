import requests

from django.conf import settings
from django.http import HttpResponse

from query_apis.api_football.models import League
from query_apis.apis import API



class FootballAPI(API):

    def __init__(self, api_url=settings.FOOTBALL_API['API_URL'], api_key=settings.FOOTBALL_API['API_KEY']):
        self.api_url = api_url
        self.headers = {
            'X-RapidAPI-Key': api_key,
        }

    def get_provided_objects(self):
        return [
            League.__class__,
        ]

    def update_provided_objects(self):
        leagues = self.__query_endpoint('/leagues/', 'leagues')

        self.__update_leagues(leagues)

        for league in leagues:
            teams = self.__query_endpoint(
                endpoint_url='/teams/league/{}/',
                endpoint_object_name='teams',
                endpoint_args=[league['league_id']]
            )

            rounds = self.__query_endpoint(
                endpoint_url='/fixtures/rounds/{}/',
                endpoint_object_name='fixtures',
                endpoint_args=[league['league_id']]
            )

            events = self.__query_endpoint(
                endpoint_url='/fixtures/league/{}/',
                endpoint_object_name='fixtures',
                endpoint_args=[league['league_id']]
            )

    def __query_endpoint(self, endpoint_url, endpoint_object_name, endpoint_args=[]):
        return requests.get(
            settings.FOOTBALL_API.get('API_URL') + endpoint_url.format(*endpoint_args),
            headers=self.headers
        ).json()['api'][endpoint_object_name]

    @staticmethod
    def __update_leagues(leagues):
        for league in leagues:
            League.objects.get_or_create(name=league.get('name'))


def index(_):
    f_api = FootballAPI()
    f_api.update_provided_objects()
    return HttpResponse("<br>---<br>".join(map(str, League.objects.all())))

