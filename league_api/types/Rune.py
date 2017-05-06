from league_api.api import ApiType
from typing import List, Mapping

from .BasicDataStats import BasicDataStats
from .Image import Image
from .MetaData import MetaData


class Rune(ApiType):
    count: int = None  # The count of this rune used by the participant
    runeId: int = None  # The ID of the rune
    rank: int = None
    plaintext: str = None
    hideFromAll: bool = None
    inStore: bool = None
    into: List[str] = None
    id: int = None
    stats: BasicDataStats = None
    colloq: str = None
    maps: Mapping[str, bool] = None
    specialRecipe: int = None
    image: Image = None
    description: str = None
    tags: List[str] = None
    requiredChampion: str = None
    _from: List[str] = None
    group: str = None
    consumeOnFull: bool = None
    name: str = None
    consumed: bool = None
    sanitizedDescription: str = None
    depth: int = None
    rune: MetaData = None
    stacks: int = None

    @property
    def rune_id(self):
        return self.runeId

    @rune_id.setter
    def rune_id(self, value):
        self.runeId = value

    @property
    def hide_from_all(self):
        return self.hideFromAll

    @hide_from_all.setter
    def hide_from_all(self, value):
        self.hideFromAll = value

    @property
    def in_store(self):
        return self.inStore

    @in_store.setter
    def in_store(self, value):
        self.inStore = value

    @property
    def special_recipe(self):
        return self.specialRecipe

    @special_recipe.setter
    def special_recipe(self, value):
        self.specialRecipe = value

    @property
    def required_champion(self):
        return self.requiredChampion

    @required_champion.setter
    def required_champion(self, value):
        self.requiredChampion = value

    @property
    def consume_on_full(self):
        return self.consumeOnFull

    @consume_on_full.setter
    def consume_on_full(self, value):
        self.consumeOnFull = value

    @property
    def sanitized_description(self):
        return self.sanitizedDescription

    @sanitized_description.setter
    def sanitized_description(self, value):
        self.sanitizedDescription = value

