from league_api.api import ApiType
from typing import List, Mapping



class GameCustomizationObject(ApiType):
    category: str = None  # Category identifier for Game Customization
    content: str = None  # Game Customization content

