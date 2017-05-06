from league_api.api import ApiType
from typing import List, Mapping

from .BasicData import BasicData
from .Rune import Rune


class RuneList(ApiType):
    data: Mapping[str, Rune] = None
    version: str = None
    type: str = None
    basic: BasicData = None

