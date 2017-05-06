from league_api.api import ApiType
from typing import List, Mapping

from .MatchPosition import MatchPosition


class MatchEvent(ApiType):
    eventType: str = None
    towerType: str = None
    teamId: int = None
    ascendedType: str = None
    killerId: int = None
    levelUpType: str = None
    pointCaptured: str = None
    assistingParticipantIds: List[int] = None
    wardType: str = None
    monsterType: str = None
    type: str = None  # (Legal values:  CHAMPION_KILL,  WARD_PLACED,  WARD_KILL,  BUILDING_KILL,  ELITE_MONSTER_KILL,  ITEM_PURCHASED,  ITEM_SOLD,  ITEM_DESTROYED,  ITEM_UNDO,  SKILL_LEVEL_UP,  ASCENDED_EVENT,  CAPTURE_POINT,  PORO_KING_SUMMON)
    skillSlot: int = None
    victimId: int = None
    timestamp: int = None
    afterId: int = None
    monsterSubType: str = None
    laneType: str = None
    itemId: int = None
    participantId: int = None
    buildingType: str = None
    creatorId: int = None
    position: MatchPosition = None
    beforeId: int = None

    @property
    def event_type(self):
        return self.eventType

    @event_type.setter
    def event_type(self, value):
        self.eventType = value

    @property
    def tower_type(self):
        return self.towerType

    @tower_type.setter
    def tower_type(self, value):
        self.towerType = value

    @property
    def team_id(self):
        return self.teamId

    @team_id.setter
    def team_id(self, value):
        self.teamId = value

    @property
    def ascended_type(self):
        return self.ascendedType

    @ascended_type.setter
    def ascended_type(self, value):
        self.ascendedType = value

    @property
    def killer_id(self):
        return self.killerId

    @killer_id.setter
    def killer_id(self, value):
        self.killerId = value

    @property
    def level_up_type(self):
        return self.levelUpType

    @level_up_type.setter
    def level_up_type(self, value):
        self.levelUpType = value

    @property
    def point_captured(self):
        return self.pointCaptured

    @point_captured.setter
    def point_captured(self, value):
        self.pointCaptured = value

    @property
    def assisting_participant_ids(self):
        return self.assistingParticipantIds

    @assisting_participant_ids.setter
    def assisting_participant_ids(self, value):
        self.assistingParticipantIds = value

    @property
    def ward_type(self):
        return self.wardType

    @ward_type.setter
    def ward_type(self, value):
        self.wardType = value

    @property
    def monster_type(self):
        return self.monsterType

    @monster_type.setter
    def monster_type(self, value):
        self.monsterType = value

    @property
    def skill_slot(self):
        return self.skillSlot

    @skill_slot.setter
    def skill_slot(self, value):
        self.skillSlot = value

    @property
    def victim_id(self):
        return self.victimId

    @victim_id.setter
    def victim_id(self, value):
        self.victimId = value

    @property
    def after_id(self):
        return self.afterId

    @after_id.setter
    def after_id(self, value):
        self.afterId = value

    @property
    def monster_sub_type(self):
        return self.monsterSubType

    @monster_sub_type.setter
    def monster_sub_type(self, value):
        self.monsterSubType = value

    @property
    def lane_type(self):
        return self.laneType

    @lane_type.setter
    def lane_type(self, value):
        self.laneType = value

    @property
    def item_id(self):
        return self.itemId

    @item_id.setter
    def item_id(self, value):
        self.itemId = value

    @property
    def participant_id(self):
        return self.participantId

    @participant_id.setter
    def participant_id(self, value):
        self.participantId = value

    @property
    def building_type(self):
        return self.buildingType

    @building_type.setter
    def building_type(self, value):
        self.buildingType = value

    @property
    def creator_id(self):
        return self.creatorId

    @creator_id.setter
    def creator_id(self, value):
        self.creatorId = value

    @property
    def before_id(self):
        return self.beforeId

    @before_id.setter
    def before_id(self, value):
        self.beforeId = value

