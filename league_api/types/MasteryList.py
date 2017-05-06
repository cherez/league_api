from league_api.api import ApiType
from typing import List, Mapping

from .Mastery import Mastery
from .MasteryTree import MasteryTree


class MasteryList(ApiType):
    data: Mapping[str, Mastery] = None
    version: str = None
    tree: MasteryTree = None
    type: str = None

