from league_api.api import ApiType
from typing import List, Mapping

from .MiniSeries import MiniSeries


class LeagueItem(ApiType):
    rank: str = None
    hotStreak: bool = None
    miniSeries: MiniSeries = None
    wins: int = None
    veteran: bool = None
    losses: int = None
    playerOrTeamId: str = None
    playerOrTeamName: str = None
    inactive: bool = None
    freshBlood: bool = None
    leaguePoints: int = None

    @property
    def hot_streak(self):
        return self.hotStreak

    @hot_streak.setter
    def hot_streak(self, value):
        self.hotStreak = value

    @property
    def mini_series(self):
        return self.miniSeries

    @mini_series.setter
    def mini_series(self, value):
        self.miniSeries = value

    @property
    def player_or_team_id(self):
        return self.playerOrTeamId

    @player_or_team_id.setter
    def player_or_team_id(self, value):
        self.playerOrTeamId = value

    @property
    def player_or_team_name(self):
        return self.playerOrTeamName

    @player_or_team_name.setter
    def player_or_team_name(self, value):
        self.playerOrTeamName = value

    @property
    def fresh_blood(self):
        return self.freshBlood

    @fresh_blood.setter
    def fresh_blood(self, value):
        self.freshBlood = value

    @property
    def league_points(self):
        return self.leaguePoints

    @league_points.setter
    def league_points(self, value):
        self.leaguePoints = value

