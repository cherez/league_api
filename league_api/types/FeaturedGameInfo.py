from league_api.api import ApiType
from typing import List, Mapping

from .BannedChampion import BannedChampion
from .Observer import Observer
from .Participant import Participant


class FeaturedGameInfo(ApiType):
    gameId: int = None  # The ID of the game
    gameStartTime: int = None  # The game start time represented in epoch milliseconds
    platformId: str = None  # The ID of the platform on which the game is being played
    gameMode: str = None  # The game mode	             (Legal values:  CLASSIC,  ODIN,  ARAM,  TUTORIAL,  ONEFORALL,  ASCENSION,  FIRSTBLOOD,  KINGPORO)
    mapId: int = None  # The ID of the map
    gameType: str = None  # The game type	             (Legal values:  CUSTOM_GAME,  MATCHED_GAME,  TUTORIAL_GAME)
    bannedChampions: List[BannedChampion] = None  # Banned champion information
    observers: Observer = None  # The observer information
    participants: List[Participant] = None  # The participant information
    gameLength: int = None  # The amount of time in seconds that has passed since the game started
    gameQueueConfigId: int = None  # The queue type (queue types are documented on the Game Constants page)

    @property
    def game_id(self):
        return self.gameId

    @game_id.setter
    def game_id(self, value):
        self.gameId = value

    @property
    def game_start_time(self):
        return self.gameStartTime

    @game_start_time.setter
    def game_start_time(self, value):
        self.gameStartTime = value

    @property
    def platform_id(self):
        return self.platformId

    @platform_id.setter
    def platform_id(self, value):
        self.platformId = value

    @property
    def game_mode(self):
        return self.gameMode

    @game_mode.setter
    def game_mode(self, value):
        self.gameMode = value

    @property
    def map_id(self):
        return self.mapId

    @map_id.setter
    def map_id(self, value):
        self.mapId = value

    @property
    def game_type(self):
        return self.gameType

    @game_type.setter
    def game_type(self, value):
        self.gameType = value

    @property
    def banned_champions(self):
        return self.bannedChampions

    @banned_champions.setter
    def banned_champions(self, value):
        self.bannedChampions = value

    @property
    def game_length(self):
        return self.gameLength

    @game_length.setter
    def game_length(self, value):
        self.gameLength = value

    @property
    def game_queue_config_id(self):
        return self.gameQueueConfigId

    @game_queue_config_id.setter
    def game_queue_config_id(self, value):
        self.gameQueueConfigId = value

