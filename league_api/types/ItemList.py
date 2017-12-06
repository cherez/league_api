from league_api.api import ApiType
from typing import List, Mapping

from .Group import Group
from .Item import Item
from .ItemTree import ItemTree


class ItemList(ApiType):
    data: Mapping[str, Item] = None
    version: str = None
    tree: List[ItemTree] = None
    groups: List[Group] = None
    type: str = None

