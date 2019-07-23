from league_api.api import ApiType
from typing import List, Mapping



class Summoner(ApiType):
    profileIconId: int = None  # ID of the summoner icon associated with the summoner.
    name: str = None  # Summoner name.
    puuid: str = None  # Encrypted PUUID. Exact length of 78 characters.
    summonerLevel: int = None  # Summoner level associated with the summoner.
    revisionDate: int = None  # Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change
    id: str = None  # Encrypted summoner ID. Max length 63 characters.
    accountId: str = None  # Encrypted account ID. Max length 56 characters.

    @property
    def profile_icon_id(self):
        return self.profileIconId

    @profile_icon_id.setter
    def profile_icon_id(self, value):
        self.profileIconId = value

    @property
    def summoner_level(self):
        return self.summonerLevel

    @summoner_level.setter
    def summoner_level(self, value):
        self.summonerLevel = value

    @property
    def revision_date(self):
        return self.revisionDate

    @revision_date.setter
    def revision_date(self, value):
        self.revisionDate = value

    @property
    def account_id(self):
        return self.accountId

    @account_id.setter
    def account_id(self, value):
        self.accountId = value

