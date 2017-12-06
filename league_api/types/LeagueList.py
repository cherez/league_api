from league_api.api import ApiType
from typing import List, Mapping

from .LeagueItem import LeagueItem


class LeagueList(ApiType):
    leagueId: str = None
    tier: str = None
    entries: List[LeagueItem] = None
    queue: str = None
    name: str = None

    @property
    def league_id(self):
        return self.leagueId

    @league_id.setter
    def league_id(self, value):
        self.leagueId = value

