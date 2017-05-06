from league_api.api import ApiType
from typing import List, Mapping



class Gold(ApiType):
    sell: int = None
    total: int = None
    base: int = None
    purchasable: bool = None

