from league_api.api import ApiType
from typing import List, Mapping



class MetaData(ApiType):
    tier: str = None
    type: str = None
    isRune: bool = None

    @property
    def is_rune(self):
        return self.isRune

    @is_rune.setter
    def is_rune(self, value):
        self.isRune = value

