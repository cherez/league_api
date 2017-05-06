from league_api.api import ApiType
from typing import List, Mapping

from .BlockItem import BlockItem


class Block(ApiType):
    items: List[BlockItem] = None
    recMath: bool = None
    type: str = None

    @property
    def rec_math(self):
        return self.recMath

    @rec_math.setter
    def rec_math(self, value):
        self.recMath = value

