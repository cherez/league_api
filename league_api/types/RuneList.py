from league_api.api import ApiType
from typing import List, Mapping

from .Rune import Rune


class RuneList(ApiType):
    data: Mapping[str, Rune] = None
    version: str = None
    type: str = None

