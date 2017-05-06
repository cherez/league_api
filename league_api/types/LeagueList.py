from league_api.api import ApiType
from typing import List, Mapping

from .LeagueItem import LeagueItem


class LeagueList(ApiType):
    tier: str = None
    queue: str = None
    name: str = None
    entries: List[LeagueItem] = None

