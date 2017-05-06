from league_api.api import ApiType
from typing import List, Mapping

from .Block import Block


class Recommended(ApiType):
    map: str = None
    blocks: List[Block] = None
    champion: str = None
    title: str = None
    priority: bool = None
    mode: str = None
    type: str = None

