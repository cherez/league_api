from league_api.api import ApiType
from typing import List, Mapping

from .Mastery import Mastery


class MasteryPage(ApiType):
    current: bool = None  # Indicates if the mastery page is the current mastery page.
    masteries: List[Mastery] = None  # Collection of masteries associated with the mastery page.
    name: str = None  # Mastery page name.
    id: int = None  # Mastery page ID.

