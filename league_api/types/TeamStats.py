from league_api.api import ApiType
from typing import List, Mapping

from .TeamBans import TeamBans


class TeamStats(ApiType):
    firstDragon: bool = None
    firstInhibitor: bool = None
    bans: List[TeamBans] = None
    baronKills: int = None
    firstRiftHerald: bool = None
    firstBaron: bool = None
    riftHeraldKills: int = None
    firstBlood: bool = None
    teamId: int = None
    firstTower: bool = None
    vilemawKills: int = None
    inhibitorKills: int = None
    towerKills: int = None
    dominionVictoryScore: int = None
    win: str = None
    dragonKills: int = None

    @property
    def first_dragon(self):
        return self.firstDragon

    @first_dragon.setter
    def first_dragon(self, value):
        self.firstDragon = value

    @property
    def first_inhibitor(self):
        return self.firstInhibitor

    @first_inhibitor.setter
    def first_inhibitor(self, value):
        self.firstInhibitor = value

    @property
    def baron_kills(self):
        return self.baronKills

    @baron_kills.setter
    def baron_kills(self, value):
        self.baronKills = value

    @property
    def first_rift_herald(self):
        return self.firstRiftHerald

    @first_rift_herald.setter
    def first_rift_herald(self, value):
        self.firstRiftHerald = value

    @property
    def first_baron(self):
        return self.firstBaron

    @first_baron.setter
    def first_baron(self, value):
        self.firstBaron = value

    @property
    def rift_herald_kills(self):
        return self.riftHeraldKills

    @rift_herald_kills.setter
    def rift_herald_kills(self, value):
        self.riftHeraldKills = value

    @property
    def first_blood(self):
        return self.firstBlood

    @first_blood.setter
    def first_blood(self, value):
        self.firstBlood = value

    @property
    def team_id(self):
        return self.teamId

    @team_id.setter
    def team_id(self, value):
        self.teamId = value

    @property
    def first_tower(self):
        return self.firstTower

    @first_tower.setter
    def first_tower(self, value):
        self.firstTower = value

    @property
    def vilemaw_kills(self):
        return self.vilemawKills

    @vilemaw_kills.setter
    def vilemaw_kills(self, value):
        self.vilemawKills = value

    @property
    def inhibitor_kills(self):
        return self.inhibitorKills

    @inhibitor_kills.setter
    def inhibitor_kills(self, value):
        self.inhibitorKills = value

    @property
    def tower_kills(self):
        return self.towerKills

    @tower_kills.setter
    def tower_kills(self, value):
        self.towerKills = value

    @property
    def dominion_victory_score(self):
        return self.dominionVictoryScore

    @dominion_victory_score.setter
    def dominion_victory_score(self, value):
        self.dominionVictoryScore = value

    @property
    def dragon_kills(self):
        return self.dragonKills

    @dragon_kills.setter
    def dragon_kills(self, value):
        self.dragonKills = value

