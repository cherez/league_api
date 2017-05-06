from league_api.api import ApiType
from typing import List, Mapping



class MatchReference(ApiType):
    lane: str = None
    gameId: int = None
    champion: int = None
    platformId: str = None
    season: int = None
    queue: int = None
    role: str = None
    timestamp: int = None

    @property
    def game_id(self):
        return self.gameId

    @game_id.setter
    def game_id(self, value):
        self.gameId = value

    @property
    def platform_id(self):
        return self.platformId

    @platform_id.setter
    def platform_id(self, value):
        self.platformId = value

