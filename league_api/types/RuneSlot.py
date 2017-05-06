from league_api.api import ApiType
from typing import List, Mapping



class RuneSlot(ApiType):
    runeSlotId: int = None  # Rune slot ID.
    runeId: int = None  # Rune ID associated with the rune slot. For static information correlating to rune IDs, please refer to the LoL Static Data API.

    @property
    def rune_slot_id(self):
        return self.runeSlotId

    @rune_slot_id.setter
    def rune_slot_id(self, value):
        self.runeSlotId = value

    @property
    def rune_id(self):
        return self.runeId

    @rune_id.setter
    def rune_id(self, value):
        self.runeId = value

