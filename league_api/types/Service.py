from league_api.api import ApiType
from typing import List, Mapping

from .Incident import Incident


class Service(ApiType):
    status: str = None
    incidents: List[Incident] = None
    name: str = None
    slug: str = None

