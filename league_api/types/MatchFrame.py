from league_api.api import ApiType
from typing import List, Mapping

from .MatchEvent import MatchEvent
from .MatchParticipantFrame import MatchParticipantFrame


class MatchFrame(ApiType):
    timestamp: int = None
    participantFrames: Mapping[str, MatchParticipantFrame] = None
    events: List[MatchEvent] = None

    @property
    def participant_frames(self):
        return self.participantFrames

    @participant_frames.setter
    def participant_frames(self, value):
        self.participantFrames = value

