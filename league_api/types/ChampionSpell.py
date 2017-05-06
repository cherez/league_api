from league_api.api import ApiType
from typing import List, Mapping

from .Image import Image
from .LevelTip import LevelTip
from .SpellVars import SpellVars


class ChampionSpell(ApiType):
    cooldownBurn: str = None
    resource: str = None
    leveltip: LevelTip = None
    vars: List[SpellVars] = None
    costType: str = None
    image: Image = None
    sanitizedDescription: str = None
    sanitizedTooltip: str = None
    effect: List[object] = None  # This field is a List of List of Double.
    tooltip: str = None
    maxrank: int = None
    costBurn: str = None
    rangeBurn: str = None
    range: object = None  # This field is either a List of Integer or the String 'self' for spells that target one's own champion.
    cooldown: List[float] = None
    cost: List[int] = None
    key: str = None
    description: str = None
    effectBurn: List[str] = None
    altimages: List[Image] = None
    name: str = None

    @property
    def cooldown_burn(self):
        return self.cooldownBurn

    @cooldown_burn.setter
    def cooldown_burn(self, value):
        self.cooldownBurn = value

    @property
    def cost_type(self):
        return self.costType

    @cost_type.setter
    def cost_type(self, value):
        self.costType = value

    @property
    def sanitized_description(self):
        return self.sanitizedDescription

    @sanitized_description.setter
    def sanitized_description(self, value):
        self.sanitizedDescription = value

    @property
    def sanitized_tooltip(self):
        return self.sanitizedTooltip

    @sanitized_tooltip.setter
    def sanitized_tooltip(self, value):
        self.sanitizedTooltip = value

    @property
    def cost_burn(self):
        return self.costBurn

    @cost_burn.setter
    def cost_burn(self, value):
        self.costBurn = value

    @property
    def range_burn(self):
        return self.rangeBurn

    @range_burn.setter
    def range_burn(self, value):
        self.rangeBurn = value

    @property
    def effect_burn(self):
        return self.effectBurn

    @effect_burn.setter
    def effect_burn(self, value):
        self.effectBurn = value

