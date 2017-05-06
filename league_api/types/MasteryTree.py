from league_api.api import ApiType
from typing import List, Mapping

from .MasteryTreeList import MasteryTreeList


class MasteryTree(ApiType):
    Resolve: List[MasteryTreeList] = None
    Ferocity: List[MasteryTreeList] = None
    Cunning: List[MasteryTreeList] = None

    @property
    def resolve(self):
        return self.Resolve

    @resolve.setter
    def resolve(self, value):
        self.Resolve = value

    @property
    def ferocity(self):
        return self.Ferocity

    @ferocity.setter
    def ferocity(self, value):
        self.Ferocity = value

    @property
    def cunning(self):
        return self.Cunning

    @cunning.setter
    def cunning(self, value):
        self.Cunning = value

