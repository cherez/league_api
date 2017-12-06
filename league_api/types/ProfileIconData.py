from league_api.api import ApiType
from typing import List, Mapping

from .ProfileIconDetails import ProfileIconDetails


class ProfileIconData(ApiType):
    data: Mapping[str, ProfileIconDetails] = None
    version: str = None
    type: str = None

