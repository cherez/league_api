from league_api.api import ApiType
from typing import List, Mapping

from .SummonerSpell import SummonerSpell


class SummonerSpellList(ApiType):
    data: Mapping[str, SummonerSpell] = None
    version: str = None
    type: str = None

