from league_api.api import ApiType
from typing import List, Mapping

from .MatchReference import MatchReference


class Matchlist(ApiType):
    matches: List[MatchReference] = None
    totalGames: int = None
    startIndex: int = None
    endIndex: int = None

    @property
    def total_games(self):
        return self.totalGames

    @total_games.setter
    def total_games(self, value):
        self.totalGames = value

    @property
    def start_index(self):
        return self.startIndex

    @start_index.setter
    def start_index(self, value):
        self.startIndex = value

    @property
    def end_index(self):
        return self.endIndex

    @end_index.setter
    def end_index(self, value):
        self.endIndex = value

