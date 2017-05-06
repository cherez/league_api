from league_api.api import ApiType
from typing import List, Mapping

from .RunePage import RunePage


class RunePages(ApiType):
    pages: List[RunePage] = None  # Collection of rune pages associated with the summoner.
    summonerId: int = None  # Summoner ID.

    @property
    def summoner_id(self):
        return self.summonerId

    @summoner_id.setter
    def summoner_id(self, value):
        self.summonerId = value

