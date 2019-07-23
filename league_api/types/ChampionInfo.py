from league_api.api import ApiType
from typing import List, Mapping



class ChampionInfo(ApiType):
    freeChampionIdsForNewPlayers: List[int] = None
    freeChampionIds: List[int] = None
    maxNewPlayerLevel: int = None

    @property
    def free_champion_ids_for_new_players(self):
        return self.freeChampionIdsForNewPlayers

    @free_champion_ids_for_new_players.setter
    def free_champion_ids_for_new_players(self, value):
        self.freeChampionIdsForNewPlayers = value

    @property
    def free_champion_ids(self):
        return self.freeChampionIds

    @free_champion_ids.setter
    def free_champion_ids(self, value):
        self.freeChampionIds = value

    @property
    def max_new_player_level(self):
        return self.maxNewPlayerLevel

    @max_new_player_level.setter
    def max_new_player_level(self, value):
        self.maxNewPlayerLevel = value

