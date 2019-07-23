from league_api.api import ApiType
from typing import List, Mapping



class TeamBans(ApiType):
    pickTurn: int = None  # Turn during which the champion was banned.
    championId: int = None  # Banned championId.

    @property
    def pick_turn(self):
        return self.pickTurn

    @pick_turn.setter
    def pick_turn(self, value):
        self.pickTurn = value

    @property
    def champion_id(self):
        return self.championId

    @champion_id.setter
    def champion_id(self, value):
        self.championId = value

