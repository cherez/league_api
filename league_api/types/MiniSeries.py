from league_api.api import ApiType
from typing import List, Mapping



class MiniSeries(ApiType):
    progress: str = None
    losses: int = None
    target: int = None
    wins: int = None

