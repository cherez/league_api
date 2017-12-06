from league_api.api import ApiType
from typing import List, Mapping



class Perks(ApiType):
    perkStyle: int = None  # Primary runes path
    perkIds: List[int] = None  # IDs of the perks/runes assigned.
    perkSubStyle: int = None  # Secondary runes path

    @property
    def perk_style(self):
        return self.perkStyle

    @perk_style.setter
    def perk_style(self, value):
        self.perkStyle = value

    @property
    def perk_ids(self):
        return self.perkIds

    @perk_ids.setter
    def perk_ids(self, value):
        self.perkIds = value

    @property
    def perk_sub_style(self):
        return self.perkSubStyle

    @perk_sub_style.setter
    def perk_sub_style(self, value):
        self.perkSubStyle = value

