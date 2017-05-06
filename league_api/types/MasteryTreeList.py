from league_api.api import ApiType
from typing import List, Mapping

from .MasteryTreeItem import MasteryTreeItem


class MasteryTreeList(ApiType):
    masteryTreeItems: List[MasteryTreeItem] = None

    @property
    def mastery_tree_items(self):
        return self.masteryTreeItems

    @mastery_tree_items.setter
    def mastery_tree_items(self, value):
        self.masteryTreeItems = value

