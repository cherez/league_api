from league_api.api import ApiType
from typing import List, Mapping

from .MatchFrame import MatchFrame


class MatchTimeline(ApiType):
    frames: List[MatchFrame] = None
    frameInterval: int = None

    @property
    def frame_interval(self):
        return self.frameInterval

    @frame_interval.setter
    def frame_interval(self, value):
        self.frameInterval = value

