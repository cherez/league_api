from league_api.api import ApiType
from typing import List, Mapping



class LevelTip(ApiType):
    effect: List[str] = None
    label: List[str] = None

