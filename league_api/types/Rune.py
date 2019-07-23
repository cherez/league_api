from league_api.api import ApiType
from typing import List, Mapping



class Rune(ApiType):
    runeId: int = None
    rank: int = None

    @property
    def rune_id(self):
        return self.runeId

    @rune_id.setter
    def rune_id(self, value):
        self.runeId = value

