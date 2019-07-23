from league_api.api import ApiType
from typing import List, Mapping

from .Mastery import Mastery
from .ParticipantStats import ParticipantStats
from .ParticipantTimeline import ParticipantTimeline
from .Rune import Rune


class Participant(ApiType):
    profileIconId: int = None  # The ID of the profile icon used by this participant
    championId: int = None  # The ID of the champion played by this participant
    summonerName: str = None  # The summoner name of this participant
    bot: bool = None  # Flag indicating whether or not this participant is a bot
    spell2Id: int = None  # The ID of the second summoner spell used by this participant
    teamId: int = None  # The team ID of this participant, indicating the participant's team
    spell1Id: int = None  # The ID of the first summoner spell used by this participant
    stats: ParticipantStats = None  # Participant statistics.
    participantId: int = None
    runes: List[Rune] = None  # List of legacy Rune information. Not included for matches played with Runes Reforged.
    timeline: ParticipantTimeline = None  # Participant timeline data.
    masteries: List[Mastery] = None  # List of legacy Mastery information. Not included for matches played with Runes Reforged.
    highestAchievedSeasonTier: str = None  # Highest ranked tier achieved for the previous season in a specific subset of queueIds, if any, otherwise null. Used to display border in game loading screen. Please refer to the Ranked Info documentation.	             (Legal values:  CHALLENGER,  MASTER,  DIAMOND,  PLATINUM,  GOLD,  SILVER,  BRONZE,  UNRANKED)

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
    def participant_id(self):
        return self.participantId

    @participant_id.setter
    def participant_id(self, value):
        self.participantId = value

    @property
    def highest_achieved_season_tier(self):
        return self.highestAchievedSeasonTier

    @highest_achieved_season_tier.setter
    def highest_achieved_season_tier(self, value):
        self.highestAchievedSeasonTier = value

