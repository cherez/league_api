from league_api.api import ApiType
from typing import List, Mapping



class Info(ApiType):
    difficulty: int = None
    attack: int = None
    defense: int = None
    magic: int = None

