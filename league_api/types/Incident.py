from league_api.api import ApiType
from typing import List, Mapping

from .Message import Message


class Incident(ApiType):
    active: bool = None
    created_at: str = None
    id: int = None
    updates: List[Message] = None

