from league_api.api import ApiType
from typing import List, Mapping

from .Image import Image


class MapDetails(ApiType):
    mapName: str = None
    image: Image = None
    mapId: int = None
    unpurchasableItemList: List[int] = None

    @property
    def map_name(self):
        return self.mapName

    @map_name.setter
    def map_name(self, value):
        self.mapName = value

    @property
    def map_id(self):
        return self.mapId

    @map_id.setter
    def map_id(self, value):
        self.mapId = value

    @property
    def unpurchasable_item_list(self):
        return self.unpurchasableItemList

    @unpurchasable_item_list.setter
    def unpurchasable_item_list(self, value):
        self.unpurchasableItemList = value

