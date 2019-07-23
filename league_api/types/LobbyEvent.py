from league_api.api import ApiType
from typing import List, Mapping



class LobbyEvent(ApiType):
    eventType: str = None  # The type of event that was triggered
    summonerId: str = None  # The summonerId that triggered the event (Encrypted)
    timestamp: str = None  # Timestamp from the event

    @property
    def event_type(self):
        return self.eventType

    @event_type.setter
    def event_type(self, value):
        self.eventType = value

    @property
    def summoner_id(self):
        return self.summonerId

    @summoner_id.setter
    def summoner_id(self, value):
        self.summonerId = value

