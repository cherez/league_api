from league_api.api import ApiType
from typing import List, Mapping



class MasteryTreeItem(ApiType):
    masteryId: int = None
    prereq: str = None

    @property
    def mastery_id(self):
        return self.masteryId

    @mastery_id.setter
    def mastery_id(self, value):
        self.masteryId = value

