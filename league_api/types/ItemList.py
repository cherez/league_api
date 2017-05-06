from league_api.api import ApiType
from typing import List, Mapping

from .BasicData import BasicData
from .Group import Group
from .Item import Item
from .ItemTree import ItemTree


class ItemList(ApiType):
    data: Mapping[str, Item] = None
    tree: List[ItemTree] = None
    version: str = None
    groups: List[Group] = None
    basic: BasicData = None
    type: str = None

