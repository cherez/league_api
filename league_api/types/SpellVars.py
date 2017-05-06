from league_api.api import ApiType
from typing import List, Mapping



class SpellVars(ApiType):
    ranksWith: str = None
    dyn: str = None
    link: str = None
    coeff: List[float] = None
    key: str = None

    @property
    def ranks_with(self):
        return self.ranksWith

    @ranks_with.setter
    def ranks_with(self, value):
        self.ranksWith = value

