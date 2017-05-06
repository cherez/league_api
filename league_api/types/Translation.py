from league_api.api import ApiType
from typing import List, Mapping



class Translation(ApiType):
    locale: str = None
    content: str = None
    updated_at: str = None

