from league_api.api import ApiType
from typing import List, Mapping



class MiniSeries(ApiType):
    wins: int = None
    losses: int = None
    target: int = None
    progress: str = None

