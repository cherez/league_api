from league_api.api import ApiType
from typing import List, Mapping



class LanguageStrings(ApiType):
    data: Mapping[str, str] = None
    version: str = None
    type: str = None

