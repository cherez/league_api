from league_api.api import ApiType
from typing import List, Mapping



class ChampionMastery(ApiType):
    chestGranted: bool = None  # Is chest granted for this champion or not in current season.
    championLevel: int = None  # Champion level for specified player and champion combination.
    championPoints: int = None  # Total number of champion points for this player and champion combination - they are used to determine championLevel.
    championId: int = None  # Champion ID for this entry.
    playerId: int = None  # Player ID for this entry.
    championPointsUntilNextLevel: int = None  # Number of points needed to achieve next level. Zero if player reached maximum champion level for this champion.
    championPointsSinceLastLevel: int = None  # Number of points earned since current level has been achieved. Zero if player reached maximum champion level for this champion.
    lastPlayTime: int = None  # Last time this champion was played by this player - in Unix milliseconds time format.

    @property
    def chest_granted(self):
        return self.chestGranted

    @chest_granted.setter
    def chest_granted(self, value):
        self.chestGranted = value

    @property
    def champion_level(self):
        return self.championLevel

    @champion_level.setter
    def champion_level(self, value):
        self.championLevel = value

    @property
    def champion_points(self):
        return self.championPoints

    @champion_points.setter
    def champion_points(self, value):
        self.championPoints = value

    @property
    def champion_id(self):
        return self.championId

    @champion_id.setter
    def champion_id(self, value):
        self.championId = value

    @property
    def player_id(self):
        return self.playerId

    @player_id.setter
    def player_id(self, value):
        self.playerId = value

    @property
    def champion_points_until_next_level(self):
        return self.championPointsUntilNextLevel

    @champion_points_until_next_level.setter
    def champion_points_until_next_level(self, value):
        self.championPointsUntilNextLevel = value

    @property
    def champion_points_since_last_level(self):
        return self.championPointsSinceLastLevel

    @champion_points_since_last_level.setter
    def champion_points_since_last_level(self, value):
        self.championPointsSinceLastLevel = value

    @property
    def last_play_time(self):
        return self.lastPlayTime

    @last_play_time.setter
    def last_play_time(self, value):
        self.lastPlayTime = value

