from league_api.api import ApiType
from typing import List, Mapping

from .Image import Image
from .MetaData import MetaData
from .RuneStats import RuneStats


class Rune(ApiType):
    runeId: int = None
    rank: int = None
    stats: RuneStats = None
    name: str = None
    tags: List[str] = None
    image: Image = None
    sanitizedDescription: str = None
    rune: MetaData = None
    id: int = None
    description: str = None

    @property
    def rune_id(self):
        return self.runeId

    @rune_id.setter
    def rune_id(self, value):
        self.runeId = value

    @property
    def sanitized_description(self):
        return self.sanitizedDescription

    @sanitized_description.setter
    def sanitized_description(self, value):
        self.sanitizedDescription = value

