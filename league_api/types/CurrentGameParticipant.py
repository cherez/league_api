from league_api.api import ApiType
from typing import List, Mapping

from .GameCustomizationObject import GameCustomizationObject
from .Perks import Perks


class CurrentGameParticipant(ApiType):
    profileIconId: int = None  # The ID of the profile icon used by this participant
    championId: int = None  # The ID of the champion played by this participant
    summonerName: str = None  # The summoner name of this participant
    gameCustomizationObjects: List[GameCustomizationObject] = None  # List of Game Customizations
    bot: bool = None  # Flag indicating whether or not this participant is a bot
    perks: Perks = None  # Perks/Runes Reforged Information
    spell2Id: int = None  # The ID of the second summoner spell used by this participant
    teamId: int = None  # The team ID of this participant, indicating the participant's team
    spell1Id: int = None  # The ID of the first summoner spell used by this participant
    summonerId: str = None  # The encrypted summoner ID of this participant

    @property
    def profile_icon_id(self):
        return self.profileIconId

    @profile_icon_id.setter
    def profile_icon_id(self, value):
        self.profileIconId = value

    @property
    def champion_id(self):
        return self.championId

    @champion_id.setter
    def champion_id(self, value):
        self.championId = value

    @property
    def summoner_name(self):
        return self.summonerName

    @summoner_name.setter
    def summoner_name(self, value):
        self.summonerName = value

    @property
    def game_customization_objects(self):
        return self.gameCustomizationObjects

    @game_customization_objects.setter
    def game_customization_objects(self, value):
        self.gameCustomizationObjects = value

    @property
    def spell2_id(self):
        return self.spell2Id

    @spell2_id.setter
    def spell2_id(self, value):
        self.spell2Id = value

    @property
    def team_id(self):
        return self.teamId

    @team_id.setter
    def team_id(self, value):
        self.teamId = value

    @property
    def spell1_id(self):
        return self.spell1Id

    @spell1_id.setter
    def spell1_id(self, value):
        self.spell1Id = value

    @property
    def summoner_id(self):
        return self.summonerId

    @summoner_id.setter
    def summoner_id(self, value):
        self.summonerId = value

