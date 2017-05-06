from league_api.api import ApiType
from typing import List, Mapping



class Group(ApiType):
    MaxGroupOwnable: str = None
    key: str = None

    @property
    def max_group_ownable(self):
        return self.MaxGroupOwnable

    @max_group_ownable.setter
    def max_group_ownable(self, value):
        self.MaxGroupOwnable = value

