from league_api.api import ApiType
from typing import List, Mapping

from .MapDetails import MapDetails


class MapData(ApiType):
    data: Mapping[str, MapDetails] = None
    version: str = None
    type: str = None

