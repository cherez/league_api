from league_api.api import ApiType
from typing import List, Mapping

from .Player import Player


class ParticipantIdentity(ApiType):
    player: Player = None  # Player information.
    participantId: int = None

    @property
    def participant_id(self):
        return self.participantId

    @participant_id.setter
    def participant_id(self, value):
        self.participantId = value

