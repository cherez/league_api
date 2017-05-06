from league_api.api import ApiType
from typing import List, Mapping

from .RuneSlot import RuneSlot


class RunePage(ApiType):
    current: bool = None  # Indicates if the page is the current page.
    slots: List[RuneSlot] = None  # Collection of rune slots associated with the rune page.
    name: str = None  # Rune page name.
    id: int = None  # Rune page ID.

