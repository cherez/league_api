from league_api.api import ApiType
from typing import List, Mapping

from .Image import Image


class ProfileIconData(ApiType):
    data: Mapping[str, Image] = None
