from league_api.api import ApiType
from typing import List, Mapping

from .Participant import Participant
from .ParticipantIdentity import ParticipantIdentity
from .TeamStats import TeamStats


class Match(ApiType):
    seasonId: int = None
    queueId: int = None
    gameId: int = None
    participantIdentities: List[ParticipantIdentity] = None
    gameVersion: str = None
    platformId: str = None
    gameMode: str = None
    mapId: int = None
    gameType: str = None
    teams: List[TeamStats] = None
    participants: List[Participant] = None
    gameDuration: int = None
    gameCreation: int = None

    @property
    def season_id(self):
        return self.seasonId

    @season_id.setter
    def season_id(self, value):
        self.seasonId = value

    @property
    def queue_id(self):
        return self.queueId

    @queue_id.setter
    def queue_id(self, value):
        self.queueId = value

    @property
    def game_id(self):
        return self.gameId

    @game_id.setter
    def game_id(self, value):
        self.gameId = value

    @property
    def participant_identities(self):
        return self.participantIdentities

    @participant_identities.setter
    def participant_identities(self, value):
        self.participantIdentities = value

    @property
    def game_version(self):
        return self.gameVersion

    @game_version.setter
    def game_version(self, value):
        self.gameVersion = value

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
    def game_duration(self):
        return self.gameDuration

    @game_duration.setter
    def game_duration(self, value):
        self.gameDuration = value

    @property
    def game_creation(self):
        return self.gameCreation

    @game_creation.setter
    def game_creation(self, value):
        self.gameCreation = value

