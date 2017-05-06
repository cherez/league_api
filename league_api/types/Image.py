from league_api.api import ApiType
from typing import List, Mapping



class Image(ApiType):
    full: str = None
    group: str = None
    sprite: str = None
    h: int = None
    w: int = None
    y: int = None
    x: int = None

