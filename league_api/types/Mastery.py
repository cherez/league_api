from league_api.api import ApiType
from typing import List, Mapping



class Mastery(ApiType):
    masteryId: int = None
    rank: int = None

    @property
    def mastery_id(self):
        return self.masteryId

    @mastery_id.setter
    def mastery_id(self, value):
        self.masteryId = value

