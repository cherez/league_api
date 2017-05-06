from league_api.api import ApiType
from typing import List, Mapping

from .Champion import Champion


class ChampionList(ApiType):
    keys: Mapping[str, str] = None
    data: Mapping[str, Champion] = None
    version: str = None
    type: str = None
    format: str = None
    champions: List[Champion] = None  # The collection of champion information.

