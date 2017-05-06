from league_api.api import ApiType
from typing import List, Mapping

from .Service import Service


class ShardStatus(ApiType):
    name: str = None
    region_tag: str = None
    hostname: str = None
    services: List[Service] = None
    slug: str = None
    locales: List[str] = None

