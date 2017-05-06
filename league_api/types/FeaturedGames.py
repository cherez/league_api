from league_api.api import ApiType
from typing import List, Mapping

from .FeaturedGameInfo import FeaturedGameInfo


class FeaturedGames(ApiType):
    clientRefreshInterval: int = None  # The suggested interval to wait before requesting FeaturedGames again
    gameList: List[FeaturedGameInfo] = None  # The list of featured games

    @property
    def client_refresh_interval(self):
        return self.clientRefreshInterval

    @client_refresh_interval.setter
    def client_refresh_interval(self, value):
        self.clientRefreshInterval = value

    @property
    def game_list(self):
        return self.gameList

    @game_list.setter
    def game_list(self, value):
        self.gameList = value

