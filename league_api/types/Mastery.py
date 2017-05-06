from league_api.api import ApiType
from typing import List, Mapping

from .Image import Image


class Mastery(ApiType):
    masteryId: int = None  # The ID of the mastery
    rank: int = None  # The number of points put into this mastery by the user
    id: int = None  # Mastery ID. For static information correlating to masteries, please refer to the LoL Static Data API.
    prereq: str = None
    masteryTree: str = None  # (Legal values:  Cunning,  Ferocity,  Resolve)
    name: str = None
    ranks: int = None
    image: Image = None
    sanitizedDescription: List[str] = None
    description: List[str] = None

    @property
    def mastery_id(self):
        return self.masteryId

    @mastery_id.setter
    def mastery_id(self, value):
        self.masteryId = value

    @property
    def mastery_tree(self):
        return self.masteryTree

    @mastery_tree.setter
    def mastery_tree(self, value):
        self.masteryTree = value

    @property
    def sanitized_description(self):
        return self.sanitizedDescription

    @sanitized_description.setter
    def sanitized_description(self, value):
        self.sanitizedDescription = value

