from league_api.api import ApiType
from typing import List, Mapping

from .Image import Image


class ProfileIconDetails(ApiType):
    image: Image = None
    id: int = None

