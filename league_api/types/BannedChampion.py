from league_api.api import ApiType
from typing import List, Mapping



class BannedChampion(ApiType):
    pickTurn: int = None  # The turn during which the champion was banned
    championId: int = None  # The ID of the banned champion
    teamId: int = None  # The ID of the team that banned the champion

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

    @property
    def team_id(self):
        return self.teamId

    @team_id.setter
    def team_id(self, value):
        self.teamId = value

