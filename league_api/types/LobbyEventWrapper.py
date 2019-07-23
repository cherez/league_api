from league_api.api import ApiType
from typing import List, Mapping

from .LobbyEvent import LobbyEvent


class LobbyEventWrapper(ApiType):
    eventList: List[LobbyEvent] = None

    @property
    def event_list(self):
        return self.eventList

    @event_list.setter
    def event_list(self, value):
        self.eventList = value

