from league_api.api import ApiType
from typing import List, Mapping

from .MatchPosition import MatchPosition


class MatchParticipantFrame(ApiType):
    totalGold: int = None
    teamScore: int = None
    participantId: int = None
    level: int = None
    currentGold: int = None
    minionsKilled: int = None
    dominionScore: int = None
    position: MatchPosition = None
    xp: int = None
    jungleMinionsKilled: int = None

    @property
    def total_gold(self):
        return self.totalGold

    @total_gold.setter
    def total_gold(self, value):
        self.totalGold = value

    @property
    def team_score(self):
        return self.teamScore

    @team_score.setter
    def team_score(self, value):
        self.teamScore = value

    @property
    def participant_id(self):
        return self.participantId

    @participant_id.setter
    def participant_id(self, value):
        self.participantId = value

    @property
    def current_gold(self):
        return self.currentGold

    @current_gold.setter
    def current_gold(self, value):
        self.currentGold = value

    @property
    def minions_killed(self):
        return self.minionsKilled

    @minions_killed.setter
    def minions_killed(self, value):
        self.minionsKilled = value

    @property
    def dominion_score(self):
        return self.dominionScore

    @dominion_score.setter
    def dominion_score(self, value):
        self.dominionScore = value

    @property
    def jungle_minions_killed(self):
        return self.jungleMinionsKilled

    @jungle_minions_killed.setter
    def jungle_minions_killed(self, value):
        self.jungleMinionsKilled = value

