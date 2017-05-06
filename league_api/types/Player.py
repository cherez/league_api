from league_api.api import ApiType
from typing import List, Mapping



class Player(ApiType):
    currentPlatformId: str = None
    summonerName: str = None
    matchHistoryUri: str = None
    platformId: str = None
    currentAccountId: int = None
    profileIcon: int = None
    summonerId: int = None
    accountId: int = None

    @property
    def current_platform_id(self):
        return self.currentPlatformId

    @current_platform_id.setter
    def current_platform_id(self, value):
        self.currentPlatformId = value

    @property
    def summoner_name(self):
        return self.summonerName

    @summoner_name.setter
    def summoner_name(self, value):
        self.summonerName = value

    @property
    def match_history_uri(self):
        return self.matchHistoryUri

    @match_history_uri.setter
    def match_history_uri(self, value):
        self.matchHistoryUri = value

    @property
    def platform_id(self):
        return self.platformId

    @platform_id.setter
    def platform_id(self, value):
        self.platformId = value

    @property
    def current_account_id(self):
        return self.currentAccountId

    @current_account_id.setter
    def current_account_id(self, value):
        self.currentAccountId = value

    @property
    def profile_icon(self):
        return self.profileIcon

    @profile_icon.setter
    def profile_icon(self, value):
        self.profileIcon = value

    @property
    def summoner_id(self):
        return self.summonerId

    @summoner_id.setter
    def summoner_id(self, value):
        self.summonerId = value

    @property
    def account_id(self):
        return self.accountId

    @account_id.setter
    def account_id(self, value):
        self.accountId = value

