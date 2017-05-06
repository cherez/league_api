from league_api.api import ApiType
from typing import List, Mapping

from .Translation import Translation


class Message(ApiType):
    severity: str = None
    author: str = None
    created_at: str = None
    translations: List[Translation] = None
    updated_at: str = None
    content: str = None
    id: str = None

