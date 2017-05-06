from league_api.api import ApiType
from typing import List, Mapping

from .ChampionSpell import ChampionSpell
from .Image import Image
from .Info import Info
from .Passive import Passive
from .Recommended import Recommended
from .Skin import Skin
from .Stats import Stats


class Champion(ApiType):
    info: Info = None
    enemytips: List[str] = None
    stats: Stats = None
    name: str = None
    title: str = None
    image: Image = None
    tags: List[str] = None
    partype: str = None
    skins: List[Skin] = None
    passive: Passive = None
    recommended: List[Recommended] = None
    allytips: List[str] = None
    key: str = None
    lore: str = None
    id: int = None
    blurb: str = None
    spells: List[ChampionSpell] = None
    rankedPlayEnabled: bool = None  # Ranked play enabled flag.
    botEnabled: bool = None  # Bot enabled flag (for custom games).
    botMmEnabled: bool = None  # Bot Match Made enabled flag (for Co-op vs. AI games).
    active: bool = None  # Indicates if the champion is active.
    freeToPlay: bool = None  # Indicates if the champion is free to play. Free to play champions are rotated periodically.

    @property
    def ranked_play_enabled(self):
        return self.rankedPlayEnabled

    @ranked_play_enabled.setter
    def ranked_play_enabled(self, value):
        self.rankedPlayEnabled = value

    @property
    def bot_enabled(self):
        return self.botEnabled

    @bot_enabled.setter
    def bot_enabled(self, value):
        self.botEnabled = value

    @property
    def bot_mm_enabled(self):
        return self.botMmEnabled

    @bot_mm_enabled.setter
    def bot_mm_enabled(self, value):
        self.botMmEnabled = value

    @property
    def free_to_play(self):
        return self.freeToPlay

    @free_to_play.setter
    def free_to_play(self, value):
        self.freeToPlay = value

