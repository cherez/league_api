from league_api.api import ApiType
from typing import List, Mapping

from .MiniSeries import MiniSeries


class LeagueItem(ApiType):
    summonerName: str = None
    hotStreak: bool = None
    miniSeries: MiniSeries = None
    wins: int = None  # Winning team on Summoners Rift. First placement in Teamfight Tactics.
    veteran: bool = None
    losses: int = None  # Losing team on Summoners Rift. Second through eighth placement in Teamfight Tactics.
    freshBlood: bool = None
    inactive: bool = None
    rank: str = None
    summonerId: str = None  # Player's summonerId (Encrypted)
    leaguePoints: int = None

    @property
    def summoner_name(self):
        return self.summonerName

    @summoner_name.setter
    def summoner_name(self, value):
        self.summonerName = value

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
    def fresh_blood(self):
        return self.freshBlood

    @fresh_blood.setter
    def fresh_blood(self, value):
        self.freshBlood = value

    @property
    def summoner_id(self):
        return self.summonerId

    @summoner_id.setter
    def summoner_id(self, value):
        self.summonerId = value

    @property
    def league_points(self):
        return self.leaguePoints

    @league_points.setter
    def league_points(self, value):
        self.leaguePoints = value

